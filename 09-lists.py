# Demo program on Lists

names=[]
names.append("edan hazard")
names.append("alvaro morata")
names.append("soham")

for nm in names:
    print(nm)

nums=[23,45,89]
for x in nums:
    print(x)


list=['soham','praffull','tom','gilchrist']
print(list[0])
print(list[1:3])

list[2]='cruise'
print(list[2])

print(len(list))
del list[2]
print(list)
print(len(list))


list=[23,45,89]
print(min(list))
print(max(list))

#content of sohamglobal.com