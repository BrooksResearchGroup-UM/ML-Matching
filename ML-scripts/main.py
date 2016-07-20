__author__ = "Xinqiang Ding <xqding@umich.edu>"
__date__ = "2016/07/20 03:35:53"

## remembe to module load gcc/4.8.4 before import xgboost
import sys
sys.path.append("../scripts/")
from ReadPara import *
import xgboost as xgb
import cPickle
import numpy as np
from numpy import random
from collections import defaultdict
from itertools import permutations

### read cgenff parameter files
paraFileName = "../CGENFF3.0.1/par_all36_cgenff.prm"
atomType = {}
mass = {}
epsilon = {}
epsilon14 = {}
sigma = {}
sigma14 = {}
bond = {}
angle = {}
diheral = {}
improper = {}
ReadPara(paraFileName, atomType,
         mass, epsilon, sigma, epsilon14, sigma14,
         bond, angle, diheral, improper)

## read in data
f = open("../data/feature.pkl", 'r')
feature = cPickle.load(f)
f.close()
f = open("../data/charmmAtomType.pkl", 'r')
charmmAtomType = cPickle.load(f)
f.close()
f = open("../data/charmmCharge.pkl", 'r')
charmmCharge = cPickle.load(f)
f.close()

## some statistic about the data
countAtomTypes = []
countElement = defaultdict(int)
elementTypeCount = defaultdict(int)
for t in atomType.itervalues():
    elementTypeCount[t[0:2]] += 1
    
for t in atomType.keys():
    c = charmmAtomType.count(t)
    countAtomTypes.append([t,atomType[t],c])
    countElement[atomType[t][0:2]] += c
countAtomTypes = np.array(countAtomTypes)

## augment data
feature_ext = np.zeros((feature.shape[0]*24, feature.shape[1]), dtype = int)
charmmAtomType_ext = []
charmmCharge_ext = []
for i in range(feature.shape[0]):
    print i
    k = 0
    for p in permutations(range(1,5)):
        tmp = list(feature[i,0:32])
        for j in p:
            tmp += list(feature[i,(32*j):(32*(j+1))])
        feature_ext[i*24 + k,:] = tmp
        charmmAtomType_ext.append(charmmAtomType[i])
        charmmCharge_ext.append(charmmCharge[i])
        k += 1

## for carbon atoms
feature_carbon = []
charmmAtomType_carbon = []
charmmCharge_carbon = []
for i in range(feature_ext.shape[0]):
    print i
    if atomType[charmmAtomType_ext[i]][0:2] == "CG":
        feature_carbon.append(feature_ext[i,:])
        charmmAtomType_carbon.append(charmmAtomType_ext[i])
        charmmCharge_carbon.append(charmmCharge_ext[i])
        
feature_carbon = np.array(feature_carbon)

## convert atom type to index of class needed by xgboost
type2index = {}
k = 0
for i in set(charmmAtomType_carbon):
    type2index[i] = k
    k += 1
for i in range(len(charmmAtomType_carbon)):
    charmmAtomType_carbon[i] = type2index[charmmAtomType_carbon[i]]

charmmAtomType_carbon = np.array(charmmAtomType_carbon)
charmmCharge_carbon = np.array(charmmCharge_carbon)

## split into training and testing
n_train = int(feature_carbon.shape[0] * 0.8)
idxs_train = list(random.choice(range(feature_carbon.shape[0]), n_train, False))
idxs_test = list(set(range(feature_carbon.shape[0])) - set(idxs_train))
feature_carbon_train = feature_carbon[idxs_train,:]
charmmAtomType_carbon_train = np.array(charmmAtomType_carbon[idxs_train])
charmmCharge_carbon_train = np.array(charmmCharge_carbon[idxs_train])
feature_carbon_test = feature_carbon[idxs_test,:]
charmmAtomType_carbon_test = np.array(charmmAtomType_carbon[idxs_test])
charmmCharge_carbon_test = np.array(charmmCharge_carbon[idxs_test])

# ## xgboost for atom type
# dtrain = xgb.DMatrix(feature_carbon_train, label = charmmAtomType_carbon_train)
# dtest = xgb.DMatrix(feature_carbon_test, label = charmmAtomType_carbon_test)
# param = {'max_depth':3, 'eta':0.1, 'silent':1, 'objective':'multi:softmax', 'num_class':54}
# watchlist  = [(dtest,'eval'), (dtrain,'train')]
# num_round = 200
# bst_atomType = xgb.train(param, dtrain, num_round, watchlist)

dtrain = xgb.DMatrix(feature_carbon_train, label = charmmCharge_carbon_train)
dtest = xgb.DMatrix(feature_carbon_test, label = charmmCharge_carbon_test)
param = {'max_depth':3, 'eta':0.1, 'silent':1, 'objective':'reg:linear'}
watchlist  = [(dtest,'eval'), (dtrain,'train')]
num_round = 3000
bst_charge = xgb.train(param, dtrain, num_round, watchlist)
