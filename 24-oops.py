# Demo program on class and object

class numbers:
    a=0
    b=0
    def __init__(self):
        print("Welcome to python class")

    def calcsum(self):
        sum=self.a+self.b
        return sum

    def showmessage(self,name):
        print("your name is ",name)


obj=numbers()
obj.showmessage("Ethan Hunt")


obj.a=11
obj.b=22
c=obj.calcsum()
print(c)


#content of sohamglobal.com

