def testdic(dic):
	lst=[]
	for nm in dic.keys():
		lst.append(dic[nm].upper())
	lst.sort()
	return(lst)


def unite(s1,s2):
	s3=s1|s2
	return(s3)

def smembers(s1,ch):
	sres=set()
	for nm in s1:
		if nm.startswith(ch):
			sres.add(nm)
	return(sres)


dict={123:'praffull',234:'shailaja',345:'sharayu',456:'soham',567:'alonso'}
l=testdic(dict)
print(l)


s01={'praffull','soham'}
s02={'shailaja','sharayu','nupur'}


s03=unite(s01,s02)
print(s03)


s03=smembers(s02,'n')
print(s03)