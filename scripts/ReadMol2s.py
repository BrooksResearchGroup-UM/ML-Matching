__author__ = "Xinqiang Ding <xqding@umich.edu>"
__date__ = "2016/06/14 18:01:01"

import os
import openbabel as ob

def ReadMol2s(mol2Dir):
    ids = os.listdir(mol2Dir)
    mol2s = {}
    conv = ob.OBConversion();
    conv.SetInFormat("mol2")
    for i in ids:
    #    print i
        mol2FileName = mol2Dir + "/" + i + "/" + i + ".mol2"
        mol2s[i] = ob.OBMol()
        conv.ReadFile(mol2s[i], mol2FileName)
    return mol2s
