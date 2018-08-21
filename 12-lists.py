# Demo program on Lists

names=[]
names.append("edan hazard")
names.append("alvaro morata")
names.append("david luiz")
names.append("hugo lloris")
names.append("soham")

for nm in names:
    print(nm)

print("----------------")

names.insert(1,"mohd salah")
names.remove("soham")

for nm in names:
    print(nm)

print("----------------")

names.reverse()

for nm in names:
    print(nm)

print("----------------")

names.sort()

for nm in names:
    print(nm)

print("Index %d"%names.index("david luiz"))

names.clear()


#----------------------------------

nums=[23,45,89,95]
for x in nums:
    print(x)

print("pop -------------")

print(nums.pop())
print(nums.pop())


#----------------------------------
list=['soham','praffull','tom','gilchrist']
print(list[0])
print(list[1:3])

list[2]='cruise'
print(list)

print(len(list))
del list[2]
print(list)
print(len(list))


list=[23,45,89]
print(min(list))
print(max(list))


#content of sohamglobal.com