__author__ = "Xinqiang Ding <xqding@umich.edu>"
__date__ = "2016/06/22 20:46:26"

import openbabel as ob

def LocalHalogenTyper(atom):
    """
    LocalHalogenTyper.py
    - The function assigns local atom types for halogen atoms based on its hybrization type, ring memebership, ring size, aromaticity.
    - atom: ob.OBAtom
    """
    ## check if the atom is a halogen atom
    if (atom.GetAtomicNum() not in [9,17,35,53]):
        raise ValueError("The argument for function LocalHalogenTyper has to be an ob.OBAtom object")    

    ## assign types
    typeName = atom.GetType()
    return (typeName, atom.MemberOfRingSize())
    
    
