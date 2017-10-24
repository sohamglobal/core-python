# Demo program on user defined functions

def showmess(nm):
    print("I love %s"%nm)


def calcsum(a,b):
    print("this is a user defined function")
    print("sum is %d"%(a+b))

def getsquare(n):
    return n*n


showmess("chelsea")
calcsum(12,23)

sq=getsquare(45)
print("square %d"%sq)

#content of sohamglobal.com