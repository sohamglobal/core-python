# Demo program for writing and reading files


file=open("data.txt","w")
file.write("technology is power.\n")
file.write("technology is future.")
file.close()

file=open("data.txt","r")
str=file.read()
print(str)
file.close()



import os

os.rename("data.txt","message.txt")
os.remove("message.txt")

#content of sohamglobal.com