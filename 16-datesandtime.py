# Demo program for showing date and time

import datetime
import time
import calendar

print(datetime.date.today())

localtime=time.asctime(time.localtime(time.time()))
print(localtime)

cal=calendar.month(2017,8)
print(cal)

#content of sohamglobal.com