# Demo program on DB connectivity & SELECT with MySQL 3.5

import mysql.connector

con=mysql.connector.connect(user='root',password='crosspolo',host='localhost',database='sharayudb')
curs=con.cursor()
curs.execute("select * from accounts;")
print(curs.fetchall())

con.close()


#content of sohamglobal.com