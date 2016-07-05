__author__ = "Xinqiang Ding <xqding@umich.edu>"
__date__ = "2016/06/22 20:46:26"

import openbabel as ob

def LocalSulfurTyper(atom):
    """
    LocalSulfurTyper.py
    - The function assigns local atom types for sulfur atoms based on its hybrization type, ring memebership, ring size, aromaticity.
    - atom: ob.OBAtom
    """
    ## check if the atom is a sulfur atom
    if (atom.GetAtomicNum() != 16):
        raise ValueError("The argument for function LocalSulfurTyper has to be an ob.OBAtom object")    

    ## assign types
    typeName = atom.GetType()
    return (typeName, atom.MemberOfRingSize())
    
    
