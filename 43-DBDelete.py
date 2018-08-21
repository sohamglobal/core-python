# Update data in the database table

import mysql.connector

con=mysql.connector.connect(user='root',password='crosspolo',host='localhost',database='sharayudb')
curs=con.cursor()

no=int(input("enter account number "))

try:
    curs.execute("delete from accounts where accno=%d;"%no)
    con.commit()
    if curs._affected_rows>0:
        print("account deleted successfully")
    else:
        print("Nothing happened")
except:
    print("DB delete failed")

con.close()

#content of sohamglobal.com
