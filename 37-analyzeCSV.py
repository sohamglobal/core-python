# Analyzing CSV Data using Lists

offline=[]
online=[]
totoff=0.0
toton=0.0
lines=[line for line in open("sales.csv")]

for i in range(1,len(lines)):
    line=lines[i].strip().split(',')
    if(line[3].lower()=="Offline".lower()):
        offline.append(line)
        totoff+=float(line[-1])
    else:
        online.append(line)
        toton+=float(line[-1])

print("Total offline sale : ",len(offline))
print("Total offline sales profit ",round(totoff))
print("Total online sale : ",len(online))
print("Total online sales profit ",round(toton))

#content of sohamglobal.com