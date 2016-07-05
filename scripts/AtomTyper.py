__author__ = "Xinqiang Ding <xqding@umich.edu>"
__date__ = "2016/07/05 14:04:21"

from LocalAtomTyper import *
import openbabel as ob

def AtomTyper(atom):
    """
    AtomTyper.py
    connect local atom types of current atom and its nearbouring atoms
    """
    types = [LocalAtomTyper(atom)]
    for nbrAtom in ob.OBAtomAtomIter(atom):
        types.append(LocalAtomTyper(nbrAtom))
    return types
