# class library (module) - classcollection.py

class Calculator:
    
    fnm=""
    
    def __init__(self,name):
        self.fnm=name

 
    def calcsum(self,a,b):
        self.result=a+b
        print("sum is ",self.result)
        print("name ",self.fnm)

    def calcsquare(self,n):
        print("square is ",n*n)



# Content of Sohamglobal.com