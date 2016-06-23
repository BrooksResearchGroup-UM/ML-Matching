__author__= "Murchtricia Charles <murchkia@umich.edu>"
__date__= "06/22/16"

import pybel
import openbabel as ob
from ReadMol2s import *
import os

LookUp = pybel.ob.OBTypeTable()
LookUp.SetFromType("INT")
LookUp.SetToType("SYB")

dataDir = "../structures/"


if (__name__=="__main__"):
  D = 1 # default max depth
  mol2s=ReadMol2s(dataDir)

  fp = []
  for (id,mol2) in mol2s.iteritems():
    mol=pybel.Molecule(mol2)
    for i in range(len(mol.atoms)):
      ans = []
      for atom, depth in pybel.ob.OBMolAtomBFSIter(mol.OBMol, i + 1):
            if depth > D: break
            atomtype = LookUp.Translate(atom.GetType())
            ans.append("%d-%s" % (depth - 1, atomtype))
      fp.append(";".join(sorted(ans)))
  print "\t".join(fp)
