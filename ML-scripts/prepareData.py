__author__ = "Xinqiang Ding <xqding@umich.edu>"
__date__ = "2016/07/20 21:55:44"

import sys
sys.path.append("../scripts/")
from ReadPara import *
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

## augment data through permutation
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
        
## seperate data according to elements and split into training and testing data
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
charmmAtomType_carbon = np.array(charmmAtomType_carbon)
charmmCharge_carbon = np.array(charmmCharge_carbon)
n_train = int(feature_carbon.shape[0] * 0.8)
idxs_train = list(random.choice(range(feature_carbon.shape[0]), n_train, False))
idxs_test = list(set(range(feature_carbon.shape[0])) - set(idxs_train))
feature_carbon_train = feature_carbon[idxs_train,:]
charmmAtomType_carbon_train = np.array(charmmAtomType_carbon[idxs_train])
charmmCharge_carbon_train = np.array(charmmCharge_carbon[idxs_train])
feature_carbon_test = feature_carbon[idxs_test,:]
charmmAtomType_carbon_test = np.array(charmmAtomType_carbon[idxs_test])
charmmCharge_carbon_test = np.array(charmmCharge_carbon[idxs_test])
np.savetxt("../data/feature_carbon_train.csv", feature_carbon_train,fmt = "%d", delimiter = ",")
np.savetxt("../data/charmmAtomType_carbon_train.csv", charmmAtomType_carbon_train,fmt = "%d", delimiter = ",")
np.savetxt("../data/charmmCharge_carbon_train.csv", charmmCharge_carbon_train,fmt = "%d", delimiter = ",")
np.savetxt("../data/feature_carbon_test.csv", feature_carbon_test,fmt = "%d", delimiter = ",")
np.savetxt("../data/charmmAtomType_carbon_test.csv", charmmAtomType_carbon_test,fmt = "%d", delimiter = ",")
np.savetxt("../data/charmmCharge_carbon_test.csv", charmmCharge_carbon_test,fmt = "%d", delimiter = ",")

## for nitrogen atoms
feature_nitrogen = []
charmmAtomType_nitrogen = []
charmmCharge_nitrogen = []
for i in range(feature_ext.shape[0]):
    print i
    if atomType[charmmAtomType_ext[i]][0:2] == "NG":
        feature_nitrogen.append(feature_ext[i,:])
        charmmAtomType_nitrogen.append(charmmAtomType_ext[i])
        charmmCharge_nitrogen.append(charmmCharge_ext[i])
feature_nitrogen = np.array(feature_nitrogen)
charmmAtomType_nitrogen = np.array(charmmAtomType_nitrogen)
charmmCharge_nitrogen = np.array(charmmCharge_nitrogen)
n_train = int(feature_nitrogen.shape[0] * 0.8)
idxs_train = list(random.choice(range(feature_nitrogen.shape[0]), n_train, False))
idxs_test = list(set(range(feature_nitrogen.shape[0])) - set(idxs_train))
feature_nitrogen_train = feature_nitrogen[idxs_train,:]
charmmAtomType_nitrogen_train = np.array(charmmAtomType_nitrogen[idxs_train])
charmmCharge_nitrogen_train = np.array(charmmCharge_nitrogen[idxs_train])
feature_nitrogen_test = feature_nitrogen[idxs_test,:]
charmmAtomType_nitrogen_test = np.array(charmmAtomType_nitrogen[idxs_test])
charmmCharge_nitrogen_test = np.array(charmmCharge_nitrogen[idxs_test])
np.savetxt("../data/feature_nitrogen_train.csv", feature_nitrogen_train,fmt = "%d", delimiter = ",")
np.savetxt("../data/charmmAtomType_nitrogen_train.csv", charmmAtomType_nitrogen_train,fmt = "%d", delimiter = ",")
np.savetxt("../data/charmmCharge_nitrogen_train.csv", charmmCharge_nitrogen_train,fmt = "%d", delimiter = ",")
np.savetxt("../data/feature_nitrogen_test.csv", feature_nitrogen_test,fmt = "%d", delimiter = ",")
np.savetxt("../data/charmmAtomType_nitrogen_test.csv", charmmAtomType_nitrogen_test,fmt = "%d", delimiter = ",")
np.savetxt("../data/charmmCharge_nitrogen_test.csv", charmmCharge_nitrogen_test,fmt = "%d", delimiter = ",")

## for oxygen atoms
feature_oxygen = []
charmmAtomType_oxygen = []
charmmCharge_oxygen = []
for i in range(feature_ext.shape[0]):
    print i
    if atomType[charmmAtomType_ext[i]][0:2] == "OG":
        feature_oxygen.append(feature_ext[i,:])
        charmmAtomType_oxygen.append(charmmAtomType_ext[i])
        charmmCharge_oxygen.append(charmmCharge_ext[i])
feature_oxygen = np.array(feature_oxygen)
charmmAtomType_oxygen = np.array(charmmAtomType_oxygen)
charmmCharge_oxygen = np.array(charmmCharge_oxygen)
n_train = int(feature_oxygen.shape[0] * 0.8)
idxs_train = list(random.choice(range(feature_oxygen.shape[0]), n_train, False))
idxs_test = list(set(range(feature_oxygen.shape[0])) - set(idxs_train))
feature_oxygen_train = feature_oxygen[idxs_train,:]
charmmAtomType_oxygen_train = np.array(charmmAtomType_oxygen[idxs_train])
charmmCharge_oxygen_train = np.array(charmmCharge_oxygen[idxs_train])
feature_oxygen_test = feature_oxygen[idxs_test,:]
charmmAtomType_oxygen_test = np.array(charmmAtomType_oxygen[idxs_test])
charmmCharge_oxygen_test = np.array(charmmCharge_oxygen[idxs_test])
np.savetxt("../data/feature_oxygen_train.csv", feature_oxygen_train,fmt = "%d", delimiter = ",")
np.savetxt("../data/charmmAtomType_oxygen_train.csv", charmmAtomType_oxygen_train,fmt = "%d", delimiter = ",")
np.savetxt("../data/charmmCharge_oxygen_train.csv", charmmCharge_oxygen_train,fmt = "%d", delimiter = ",")
np.savetxt("../data/feature_oxygen_test.csv", feature_oxygen_test,fmt = "%d", delimiter = ",")
np.savetxt("../data/charmmAtomType_oxygen_test.csv", charmmAtomType_oxygen_test,fmt = "%d", delimiter = ",")
np.savetxt("../data/charmmCharge_oxygen_test.csv", charmmCharge_oxygen_test,fmt = "%d", delimiter = ",")

## for hydrogen atoms
feature_hydrogen = []
charmmAtomType_hydrogen = []
charmmCharge_hydrogen = []
for i in range(feature_ext.shape[0]):
    print i
    if atomType[charmmAtomType_ext[i]][0:2] == "HG":
        feature_hydrogen.append(feature_ext[i,:])
        charmmAtomType_hydrogen.append(charmmAtomType_ext[i])
        charmmCharge_hydrogen.append(charmmCharge_ext[i])
feature_hydrogen = np.array(feature_hydrogen)
charmmAtomType_hydrogen = np.array(charmmAtomType_hydrogen)
charmmCharge_hydrogen = np.array(charmmCharge_hydrogen)
n_train = int(feature_hydrogen.shape[0] * 0.8)
idxs_train = list(random.choice(range(feature_hydrogen.shape[0]), n_train, False))
idxs_test = list(set(range(feature_hydrogen.shape[0])) - set(idxs_train))
feature_hydrogen_train = feature_hydrogen[idxs_train,:]
charmmAtomType_hydrogen_train = np.array(charmmAtomType_hydrogen[idxs_train])
charmmCharge_hydrogen_train = np.array(charmmCharge_hydrogen[idxs_train])
feature_hydrogen_test = feature_hydrogen[idxs_test,:]
charmmAtomType_hydrogen_test = np.array(charmmAtomType_hydrogen[idxs_test])
charmmCharge_hydrogen_test = np.array(charmmCharge_hydrogen[idxs_test])
np.savetxt("../data/feature_hydrogen_train.csv", feature_hydrogen_train,fmt = "%d", delimiter = ",")
np.savetxt("../data/charmmAtomType_hydrogen_train.csv", charmmAtomType_hydrogen_train,fmt = "%d", delimiter = ",")
np.savetxt("../data/charmmCharge_hydrogen_train.csv", charmmCharge_hydrogen_train,fmt = "%d", delimiter = ",")
np.savetxt("../data/feature_hydrogen_test.csv", feature_hydrogen_test,fmt = "%d", delimiter = ",")
np.savetxt("../data/charmmAtomType_hydrogen_test.csv", charmmAtomType_hydrogen_test,fmt = "%d", delimiter = ",")
np.savetxt("../data/charmmCharge_hydrogen_test.csv", charmmCharge_hydrogen_test,fmt = "%d", delimiter = ",")
