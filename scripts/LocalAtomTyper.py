__author__ = "Xinqiang Ding <xqding@umich.edu>"
__date__ = "2016/07/05 13:35:22"

from LocalHydrogenTyper import *
from LocalCarbonTyper import *
from LocalNitrogenTyper import *
from LocalOxygenTyper import *
from LocalHalogenTyper import *
from LocalPhosphorusTyper import *
from LocalSulfurTyper import *

def LocalAtomTyper(atom):
    """
    LocalAtomTyper.py
    Local envionment type for atoms
    """
    if atom.GetAtomicNum() == 1:
        return LocalHydrogenTyper(atom)
    if atom.GetAtomicNum() == 6:
        return LocalCarbonTyper(atom)
    if atom.GetAtomicNum() == 7:
        return LocalNitrogenTyper(atom)
    if atom.GetAtomicNum() == 8:
        return LocalOxygenTyper(atom)
    if atom.GetAtomicNum() == 15:
        return LocalPhosphorusTyper(atom)
    if atom.GetAtomicNum() == 16:
        return LocalSulfurTyper(atom)
    if atom.GetAtomicNum() in [9,17,35,53]:
        return LocalHalogenTyper(atom)
