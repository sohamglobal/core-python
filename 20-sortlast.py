# generate sorted list of last names in title case


def getlastnames(nm):
	lnm=[]
	for n in nm:
	    lnm.append(n.split(" ")[1].title())

	lnm.sort()
	return(lnm)
	



nm=["ethan hunt","mohd salah","edan hazard","david luiz","amir khan"]
l=getlastnames(nm)
print(l)

# content of sohamglobal.com