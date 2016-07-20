__author__ = "Xinqiang Ding <xqding@umich.edu>"
__date__ = "2016/06/13 21:54:49"

import numpy as np
import pandas as pd
import openbabel as ob
import cPickle

from ReadPara import *
from ReadMol2s import *
from LocalAtomTyper import *
from AtomTyper import *
from AtomTyper2Binary import *

# ## read parameter files
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

## read all mol2 files
dataDir = "../structures/"
mol2s = ReadMol2s(dataDir)
ids = []
for (id, mol2) in mol2s.iteritems():
    for atom in ob.OBMolAtomIter(mol2):
        if atom.GetType() == "X":
            print (id, atom.GetType())
            ids.append(id)
            break
# remove the id which has unrecognized atom type X
for i in ids:
    mol2s.pop(i)

# read CHARMM charge and atom type for each mol2
charmmAtomType = {}
for (id, mol2) in mol2s.iteritems():
    print id
    # read CHARMM charge for each mol2
    fileName = "../structures/" + id + "/chargeOnly.txt"
    charge = pd.read_table(fileName, header = None)
    charge = list(charge[0])
    for i in range(mol2.NumAtoms()):
        mol2.GetAtomById(i).SetPartialCharge(charge[i])
    ## read CHARMM atom type
    fileName = "../structures/" + id + "/typeOnly.txt"
    tmpType = pd.read_table(fileName, header = None)
    tmpType = list(tmpType[0])
    tmpType = [int(k) for k in tmpType]
    charmmAtomType[id] = tmpType
## done with the cgenff database

## atom types
localAtomTypes = []
atomTypes = []
charmmAtomType = []
charmmCharge = []
for (id, mol2) in mol2s.iteritems():
    ## read CHARMM atom type
    fileName = "../structures/" + id + "/typeOnly.txt"
    tmpType = pd.read_table(fileName, header = None)
    tmpType = list(tmpType[0])
    tmpType = [int(k) for k in tmpType]

    # read CHARMM charge for each mol2
    fileName = "../structures/" + id + "/chargeOnly.txt"
    tmpCharge = pd.read_table(fileName, header = None)
    tmpCharge = list(tmpCharge[0])

    for i in range(mol2.NumAtoms()):
        atom = mol2.GetAtomById(i)
        if (atom.GetAtomicNum() in [1,6,7,8,15,16,9,17,35,53]):
            localAtomTypes.append(LocalAtomTyper(atom))
            atomTypes.append(AtomTyper(atom))
            charmmAtomType.append(tmpType[i])
            charmmCharge.append(tmpCharge[i])
            
## sybyl atom types
sybylAtomTypes = list(set([ i for (i,j) in localAtomTypes]))
features = []
for i in atomTypes:
    features.append(AtomTyper2Binary(i, sybylAtomTypes))
features = np.array(features)

## save features, atomtype and charge
f = open('../data/feature.pkl','w')
cPickle.dump(features, f)
f.close()

f = open('../data/charmmAtomType.pkl','w')
cPickle.dump(charmmAtomType, f)
f.close()

f = open('../data/charmmCharge.pkl','w')
cPickle.dump(charmmCharge, f)
f.close()

