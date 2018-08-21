# Update data in the database table

import mysql.connector

con=mysql.connector.connect(user='root',password='crosspolo',host='localhost',database='sharayudb')
curs=con.cursor()

no=int(input("enter account number "))
amt=float(input("enter amount "))

try:
    curs.execute("update accounts set balance=balance+%.2f where accno=%d;"%(amt,no))
    con.commit()
    if curs._affected_rows>0:
        print("Balance updated successfully")
    else:
        print("Nothing happened")
except:
    print("DB update failed")

con.close()

#content of sohamglobal.com
