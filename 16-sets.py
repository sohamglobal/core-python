# A set is an unordered collection with no duplicate elements (mutable).

lang={"java","c#","python","microsoft","oracle"}
db={"oracle","sql server","mysql","microsoft"}
db.add("oracle")



#Difference elements in lang but not in db

print(lang-db)
print(20*"-")

#Union elements from both lang and db
print(lang | db)
print(20*"-")

#Intersection elements common to lang and db
print(lang & db)
print(20*"-")

#Symmetric difference elements in either lang or db but not both
print(lang ^ db)

print(20*"-")
tech=lang.copy()
print(tech)


s1=set('missionimpossible')
print(s1)

# frozenset is an immutable set 

s2=frozenset(("soham","sharayu"))
#s2.add("ethan")



#content of sohamglobal.com

