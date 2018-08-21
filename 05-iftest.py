# Code for testing if statement in python

nm=input("Enter name ")
basic=int(input("enter basic salary "))

if basic>5000:
	allowance=basic*45/100
	bonus=basic*30/100
elif basic>3000:
	allowance=basic*25/100
	bonus=basic*10/100
else:
	allowance=basic*15/100
	bonus=0
total=basic+allowance+bonus

print("Total salary is %d" %total)


# content of sohamglobal.com