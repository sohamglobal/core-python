# Reading & Writing JSON File

import json

j=open("family.json","r",encoding="utf-8")
fam=json.load(j)
j.close()

print(fam)
print(fam["firstName"])
print(fam["address"]["streetAddress"])
print(type(fam))

ply={"name":"edan hazard","club":"chelsea","role":"striker"}
file=open("players.json","w")
json.dump(ply,file)

#content of sohamglobal.com