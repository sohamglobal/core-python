# program that performs bubble sort mechanism in python

a=[45,33,21,78,90,156,9,0,32]


for i in range(len(a)-1,-1,-1):
	for j in range(0,i):
		if a[j]>a[j+1]:
			tmp=a[j]
			a[j]=a[j+1]
			a[j+1]=tmp




i=0
while i<len(a):
	print(a[i])
	i+=1
	

# Content of Sohamglobal.com