# add items to dictionary in runtime

dic={}
cho="yes"

while cho!="no":
    key=input("enter key ")
    val=input("enter value ")
    dic[key]=val
    cho=input("do you want to continue(yes/no) ")

print(dic)
print(dir(dic))


# Content of Sohamglobal.com