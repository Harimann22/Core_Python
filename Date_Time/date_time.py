import calendar
from datetime import datetime, timedelta
import time
import relativedelta

today = datetime.datetime.now()
print(today.date())

# print(-------------------------------------------------------------------------------------->)

date_string = "Feb 25 2020 4:20PM"
date_object = datetime.strptime(date_string, '%M %d %Y %I:%m%p')
print(date_object)

# print(-------------------------------------------------------------------------------------->)

given_date = datetime(2020, 2, 25)
substract_days = 7
res = given_date-timedelta(days=substract_days)
print(res)

# print(-------------------------------------------------------------------------------------->)

given_date = datetime(2020, 2, 25)
print(given_date.strftime('%A %d %B %Y'))

# print(-------------------------------------------------------------------------------------->)

given_date = datetime(1996, 7, 22)
print(given_date.today().weekday())
print(given_date.strftime('%A'))

# print(-------------------------------------------------------------------------------------->)

given_date = datetime(1996, 7, 22)
weekday = calendar.day_name[given_date.weekday()]
print(weekday)

# print(-------------------------------------------------------------------------------------->)

given_date = datetime(2022, 4, 6, 10, 0, 0)
add_days = 7
res = given_date+timedelta(days=add_days, hours=12)
print(res)

# print(-------------------------------------------------------------------------------------->)

milisecnd = int(round(time.time()*1000))
print(milisecnd)

# print(-------------------------------------------------------------------------------------->)

given_date = datetime(2020, 2, 25)
strform = given_date.strftime('%Y-%m-%d %H:%M:%S')
print(strform)

# print(-------------------------------------------------------------------------------------->)

given_date = datetime(2020, 2, 25).date()
month_add = 4
new_date = given_date+relativedelta(month=+ month_add)
print(new_date)

# print(-------------------------------------------------------------------------------------->)

date_1 = datetime(1996, 7, 22)
date_2 = datetime(2022, 4, 6)
delta = None
if date_1 > date_2:
    delta = date_1-date_2
else:
    delta = date_2-date_1
print(delta.days, "Days")

# print(-------------------------------------------------------------------------------------->)
