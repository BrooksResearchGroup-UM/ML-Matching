__author__ = "Xinqiang Ding <xqding@umich.edu>"
__date__ = "2016/06/13 19:35:55"

import re

"""
ReadPara.py
"""

def ReadPara(paraFileName, atomType,
             mass, epsilon, sigma, epsilon14, sigma14,
             bond, angle, diheral, improper):    
    inFile = open(paraFileName, 'r')
    if type(atomType) != dict:
        raise TypeError("The input parameter atomType has to be dict\n")
    if type(mass) != dict:
        raise TypeError("The input parameter mass has to be dict\n")
    if type(epsilon) != dict:
        raise TypeError("The input parameter epsilon has to be dict\n")
    if type(sigma) != dict:
        raise TypeError("The input parameter sigma has to be dict\n")
    if type(epsilon14) != dict:
        raise TypeError("The input parameter epsilon14 has to be dict\n")
    if type(sigma14) != dict:
        raise TypeError("The input parameter sigma14 has to be dict\n")
    if type(bond) != dict:
        raise TypeError("The input parameter bond has to be dict\n")
    if type(angle) != dict:
        raise TypeError("The input parameter angle has to be dict\n")
    if type(diheral) != dict:
        raise TypeError("The input parameter diheral has to be dict\n")
    if type(improper) != dict:
        raise TypeError("The input parameter improper has to be dict\n")

    ## loop over file
    atomFlag = False
    bondFlag = False
    angleFlag = False
    diheralFlag = False
    improperFlag = False
    nonbondedFlag = False
    
    for l in inFile:
        if len(l) == 0:
            continue
        if l[0] == "!" or l[0] == "*" or l[0] == " " or l[0] == "\n":
            continue
        l = l.strip()
        if l[0:4] == "HBON":
            continue
        if l[0:3] == "END":
            break
        if l[0:4] == "ATOM":
            atomFlag = True
            bondFlag = False
            angleFlag = False
            diheralFlag = False
            improperFlag = False
            nonbondedFlag = False
            continue
        if l[0:4] == "BOND":
            atomFlag = False
            bondFlag = True
            angleFlag = False
            diheralFlag = False
            improperFlag = False
            nonbondedFlag = False
            continue
        if l[0:4] == "ANGL":
            atomFlag = False
            bondFlag = False
            angleFlag = True
            diheralFlag = False
            improperFlag = False
            nonbondedFlag = False
            continue
        if l[0:4] == "DIHE":
            atomFlag = False
            bondFlag = False
            angleFlag = False
            diheralFlag = True
            improperFlag = False
            nonbondedFlag = False
            continue
        if l[0:4] == "NONB":
            atomFlag = False
            bondFlag = False
            angleFlag = False
            diheralFlag = False
            improperFlag = False
            nonbondedFlag = True
            continue
        if l[0:4] == "IMPR":
            atomFlag = False
            bondFlag = False
            angleFlag = False
            diheralFlag = False
            improperFlag = True
            nonbondedFlag = False
            continue

        if l[-1] == "-" and l.count("!") == 0:
            tmp = next(inFile)
        if atomFlag:
            if l[0:4] == "MASS":
                lf = re.split(" +", l)
                atomType[int(lf[1])] = lf[2]
                mass[lf[2]] = float(lf[3])
        if bondFlag:
            lf = re.split(" +", l)
            bond[(lf[0],lf[1])] = (float(lf[2]), float(lf[3]))
        if angleFlag:
            lf = re.split(" +", l)
            angle[(lf[0], lf[1], lf[2])] = (float(lf[3]), float(lf[4]))
        if diheralFlag:
            lf = re.split(" +", l)
            diheral[(lf[0], lf[1], lf[2], lf[3])] = (float(lf[4]), int(lf[5]), float(lf[6]))
        if improperFlag:
            lf = re.split(" +", l)
            improper[(lf[0], lf[1], lf[2], lf[3])] = float(lf[4])
        if nonbondedFlag:
            lf = re.split(" *! *", l)[0]
            lf = re.split(" +", lf)
            if len(lf) == 4:
                epsilon[lf[0]] = float(lf[2])
                sigma[lf[0]] = float(lf[3])
            if len(lf) == 7:
                epsilon[lf[0]] = float(lf[2])
                sigma[lf[0]] = float(lf[3])
                epsilon14[lf[0]] = float(lf[5])
                sigma14[lf[0]] = float(lf[6])
        
            
