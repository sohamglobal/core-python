# Program demonstrates while loop in python


count=1
while count<=10:
    print(count)
    count+=1
else:
    print("loop terminated")

print("--------------")

num=0
while True:
    print(num)
    num+=1
    if num>5:
        break
print("--------------")

for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

print("--------------")
num=1

while num>0:
	num=int(input("Enter a number "))
	sq=num*num
	print("square of ",num," is ",sq)
else:
	print("Loop terminated")



#content of sohamglobal.com