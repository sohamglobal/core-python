# program to use linear sort algorithm

a=[45,33,21,78,90,156,9,0,32]

for i in range(len(a)):
	for j in range(i+1, len(a)):
		if a[i]>a[j]:
			tmp=a[i]
			a[i]=a[j]
			a[j]=tmp



for i in range(len(a)):
	print(a[i])		
	


#content of sohamglobal.com