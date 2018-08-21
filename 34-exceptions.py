# program of exception handling

a=int(input("Enter number "))
b=int(input("Enter number "))

res=a*b
print("multiplication is",res)
try:
    res=a/b
except:
    res=None
else:        
    print("division is %.2f"%res)
finally:
    try:
        print("all is well %.2f"%res)
    except TypeError as err:
        print(err)



res=a+b
print("sum is",res)
res=a-b
print("subtraction is",res)



#  1+2+"soham"
'''
try:
except:
else:
finally:
'''