{
    if($1 == "RESI") {
	rname = $2;
        # The residue names on the next line are not insteresting because 
        # of their size.
	if(rname == "CO2" || rname == "CO3" || rname == "AMM1" || 
	   rname == "ALF4" || rname == "PEGM" || rname == "FORA"){next}

	nres++;
	fname = "res_"nres".str";
	print "set resname = "rname >fname;
        # Look for IC line to extract IC SEED
	while($1 != "IC") {getline;}
        # Don't use lines with improper ICs
	while($1 == "IC" && $0 ~ /\*/) {getline;}
        # Process line with IC to make SEED
        if($1 == "IC" && $0 !~ /\*/){
	    split($0,a);
	    seed = "";
	    is = 0;
	    for(i=2;i<6;i++){
		if(a[i] != "BLNK") {
		    seed = seed " 1 "a[i];
		    is++;if(is==3){i=6}
		}
	    }
	    print "set seed = "seed >>fname;
	}
	close(fname);
    }
}
END{ print "set nres = "nres >"restot.str"}
