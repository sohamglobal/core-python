# Demo program on Dictionaries

accounts={}

accounts["soham"]=9028293031
accounts["alvaro morata"]=9890937263
accounts["robert"]=3129400547
accounts["antoine"]=2177655643

print(accounts)


nm="alvaro morata"
print(accounts[nm])

players={
    "morata":"chelsea",
    "griezmann":"atletico",
    "lewandowski":"bayern munich",
    "jesus":"manchester city",
    "hazard":"chelsea"
}

for name,club in players.items():
    print("Name %s, Club %s"%(name,club))

del players["jesus"]
print(players)

if "morata" in players:
    print("Morata found in the list")
else:
    print("Not Found")

print(players.keys())
print(players.values())

#content of sohamglobal.com
