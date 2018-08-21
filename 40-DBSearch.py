
# Demo program on Searching/SELECT with MySQL 3.5

import mysql.connector

con=mysql.connector.connect(user='root',password='crosspolo',host='localhost',database='sharayudb')
curs=con.cursor()

typ=input("enter account type ")
curs.execute("select * from accounts where acctype ='"+typ+"';")
#print(curs.fetchall())
list=curs.fetchall()

for record in list:
    print("%s  %.2f"%(record[1],record[3]))


# Content of sohamglobal.com