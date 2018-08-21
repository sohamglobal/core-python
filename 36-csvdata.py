# Working with CSV Files

import csv

file=open("sales.csv")
for data in file:
    print(data)


lines=[line for line in open("favfilms.csv")]
print(lines[0].strip().split(','))


f=[3,'PK',2014,'Rajkumar Hirani','Aamir Khan','Anushka Sharma','Hindi']

with open("favfilms.csv","a",newline='') as csvfile:
    wr=csv.writer(csvfile)
    wr.writerow(f)

#content of sohamglobal.com