__author__ = "Xinqiang Ding <xqding@umich.edu>"
__date__ = "2016/06/22 20:46:26"

import openbabel as ob

def LocalPhosphorusTyper(atom):
    """
    LocalPhosphorusTyper.py
    - The function assigns local atom types for phosphorus atoms based on its hybrization type, ring memebership, ring size, aromaticity.
    - atom: ob.OBAtom
    """
    ## check if the atom is a phosphorus atom
    if (atom.GetAtomicNum() != 15):
        raise ValueError("The argument for function LocalPhosphorusTyper has to be an ob.OBAtom object")    

    ## assign types
    typeName = atom.GetType()
    return (typeName, atom.MemberOfRingSize())
    
    
