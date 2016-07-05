__author__ = "Xinqiang Ding <xqding@umich.edu>"
__date__ = "2016/07/05 14:56:54"

from LocalAtomTyper2Binary import *

"""
AtomTyper2Binary.py
"""

def AtomTyper2Binary(atomType, sybylAtomTypes):
    binaryVector = []
    for localAtomType in atomType:
        binaryVector = binaryVector + LocalAtomTyper2Binary(localAtomType, sybylAtomTypes)
    if (len(atomType) < 5):
        binaryVector += [0 for i in range((len(sybylAtomTypes)+1)*(5-len(atomType)))]
    return binaryVector
