# Reading and Writing a text file

fw=open("ethan.txt","a")
line=input("Enter a line of text ")
fw.write(line+"\n")
fw.close()

fr=open("ethan.txt","r")
content=fr.read()
print(content)

#content of sohamglobal.com