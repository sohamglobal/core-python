# insert record in the database table

import mysql.connector

con=mysql.connector.connect(user='root',password='crosspolo',host='localhost',database='sharayudb')
curs=con.cursor()

no=int(input("enter account number "))
nm=input("enter name ")
typ=input("enter type ")
bal=float(input("enter balance "))

try:
    curs.execute("insert into accounts values(%d,'%s','%s',%f);"%(no,nm,typ,bal))
    con.commit()
    print("account opened successfully")
except:
    print("DB insert failed")

con.close()

#content of sohamglobal.com
