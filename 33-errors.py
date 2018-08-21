# Program for simple exception handling

try:
    a=int(input("enter number "))
except ValueError as err:
    a=0
    print("error in input",err)
else:
    print("no error")
finally:
    sq=a*a
    print("square is",sq)


#content of sohamglobal.com