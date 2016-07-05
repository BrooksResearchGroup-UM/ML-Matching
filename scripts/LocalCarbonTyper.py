__author__ = "Xinqiang Ding <xqding@umich.edu>"
__date__ = "2016/06/22 20:46:26"

import openbabel as ob

def LocalCarbonTyper(atom):
    """
    LocalCarbonTyper.py
    - The function assigns local atom types for carbon atoms based on its hybrization type, ring memebership, ring size, aromaticity.
    - atom: ob.OBAtom
    """
    ## check if the atom is a carbon atom
    if (atom.GetAtomicNum() != 6):
        raise ValueError("The argument for function LocalCarbonTyper has to be an ob.OBAtom object")    

    ## assign types
    typeName = atom.GetType()
    return (typeName, atom.MemberOfRingSize())
    
    
