__author__= "Murchtricia Charles <murchkia@umich.edu>"
__date__= "06/22/16"

import pybel
import openbabel as ob
from ReadMol2s import *
import os

dataDir = "../structures/"

if (__name__=="__main__"):
  mol2s=ReadMol2s(dataDir)
  print "SYBYL Atom Type.Ring membership.Ring Size followed by atoms bonded to Carbon atom and associated bond order"
  for (id,mol2) in mol2s.iteritems():    
    mol=pybel.Molecule(mol2)
    print "\n"
    print id
    print ("\n"+"-------------------------------------------------------")
    for atom in ob.OBMolAtomIter(mol2):
	if atom.IsCarbon():
           if atom.IsInRing():
        	if atom.IsInRingSize(3):
		   print (atom.GetType()+"."+"R"+"."+"3")
		if atom.IsInRingSize(4):
                   print (atom.GetType()+"."+"R"+"."+"4")
		if atom.IsInRingSize(5):
                   print (atom.GetType()+"."+"R"+"."+"5")
		if atom.IsInRingSize(6):
                   print (atom.GetType()+"."+"R"+"."+"6")
		if atom.IsInRingSize(7):
                   print (atom.GetType()+"."+"R"+"."+"7")
           else: print(atom.GetType()+"."+"0")

	   for neighbour_atom in ob.OBAtomAtomIter(atom):
                bond = atom.GetBond(neighbour_atom)
                order= str(bond.GetBondOrder())
                print (order+","+neighbour_atom.GetType())

