# display sum of digits of a number

n=int(input("enter a number "))
sum=0

while (n!=0):
	r=n%10
	sum+=r
	n=int(n/10)

print(sum)


for i in range(1,6):
	for j in range(1,i):
		print("*",end="   ")

	print("\n")


# content of sohamglobal.com