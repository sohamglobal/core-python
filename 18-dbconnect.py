# Demo program on DB connectivity with MySQL

import mysql.connector

con=mysql.connector.connect(user='root',password='crosspolo',host='localhost',database='praffulldb')
curs=con.cursor()
curs.execute("select * from accounts")
print(curs.fetchall())

no=1009
nm="marcos alonso"
typ="current"
bal=35500
try:
    #curs.execute("insert into accounts values ("+str(no)+",'"+nm+"','"+typ+"',"+str(bal)+");")
    curs.execute("insert into accounts values(%d,'%s','%s',%f);"%(no,nm,typ,bal))
    #curs.execute("insert into accounts values(1003,'edan hazard','current',43200);")
    con.commit()
except:
    print("data insert failed..check parameters")

typ=input("enter account type ")
curs.execute("select * from accounts where acctype ='"+typ+"';")
print(curs.fetchall())

print("\n\n")
no=int(input("Enter account number "))
amt=float(input("Enter amount "))
curs.execute("update accounts set balance=balance+"+str(amt)+" where accno="+str(no)+";")
con.commit()


curs.execute("select * from accounts where accno ="+str(no)+";")
print(curs.fetchall())

con.close()


#content of sohamglobal.com