__author__ = "Xinqiang Ding <xqding@umich.edu>"
__date__ = "2016/07/05 14:45:17"

"""
LocalAtomTyper2Binary.py
"""

def LocalAtomTyper2Binary(localAtomType, sybylAtomTypes):
    if localAtomType == None:
        return [0 for i in sybylAtomTypes] + [0]
    else:
        tmp = [localAtomType[0] == i for i in sybylAtomTypes]
        tmp = [int(i) for i in tmp]
        tmp.append(localAtomType[1])
        return tmp
