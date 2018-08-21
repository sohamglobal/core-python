# Call Stored procedure to transfer amount from one account to another

'''
delimiter //
create procedure transferamt(sourceacc int,destacc int,amount float)
begin
declare cnt int;
select count(accnm) into cnt from accounts
where accno=sourceacc;
if cnt>0 then
    update accounts set balance=balance-amount
    where accno=sourceacc;
    update accounts set balance=balance+amount
    where accno=destacc;
end if;
end//
delimiter ;
'''


import mysql.connector

con=mysql.connector.connect(user='root',password='crosspolo',host='localhost',database='sharayudb')
curs=con.cursor()

sno=int(input("Transfer from account : "))
dno=int(input("Transfer to account : "))
amt=float(input("Amount : "))

try:
    curs.execute("call transferamt(%d,%d,%f);"%(sno,dno,amt))
    con.commit()
    print("procedure executed and amount transferred successfully")
except:
    print("procedure call failed")

con.close()

#content of sohamglobal.com
