#!/bin/bash

# Created by Xinqiang Ding (xqding@umich.edu)
# at 2016/06/10 19:12:22
ls ../structures/ > list.txt

for i in `cat list.txt`; do
    echo $i
    cd ../structures/$i/
    ## get charge and atom type information
    charmm -i ../../scripts/getChargeAndType.inp resname=$i
    
    ## process the charge and type file
    grep "(" charge.txt | cut -d ")" -f 2 > chargeOnly.txt
    grep "(" type.txt | cut -d ")" -f 2 > typeOnly.txt
    
    ## generate mol2 file
    obabel $i.pdb -O $i.mol2
    cd ../../scripts/
done
