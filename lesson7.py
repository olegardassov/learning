# #___________________ Import calendar
#
# import calendar
#
# print(calendar.month(2020, 11 , w=10, l=0))
#
# print(calendar.month(2000, 3, w=7, l=0))  # w = width and l = length and prints calender of 2000 year and march
#
# print(calendar.calendar(2000, w=2, l=1, c=8, m=3)) # c = is space between months, m = число столбтков , напечатаеть весь календарь за год
#
# print(calendar.isleap(2020)) # проверка года, високостный год или нет
#
# print(calendar.weekday(2021, 2 , 14))
# print(calendar.weekday(2021, 2 , 11))
# print(calendar.weekday(2021, 2 , 15))  #prints number of day of the week, counting from 0 , monady is = 0 and so on (year, month, day)
#
# print(calendar.leapdays(2000, 2020)) # will return number of leap years between 2000 and 2020 = 5
#
# print(calendar.prmonth(2020, 11, w=0, l=3))


# #____________ Import time


# import time
# start = time.time()
# time.sleep(7)  # makes pause in program 7seconds
#
# print(time.time())
#
# print(time.asctime()) # will return time now
# print(time.gmtime())
# print(type(time.gmtime()))
#
# now = time.gmtime()
# print(now[0])  # will return only year
# print(now[0], now[1], now[2])  # we can use index for that command
#
# print(2300 - now[0])  # print how many years have left to 2300, we can use now[] as a number
# end = time.time()
#
#
#
# print(end - start)  # returns how many seconds program took
#
# #_________________________
#
# import time
# start = time.time()
# time.sleep(7)  # makes pause in program 7seconds
#
# print(time.time())
#
# print(time.asctime()) # will return time now
# print(time.gmtime())
# print(type(time.gmtime()))
#
# now = time.gmtime()
# print(now[0])  # will return only year
# print(now[0], now[1], now[2])  # we can use index for that command
#
# print(2300 - now[0])  # print how many years have left to 2300, we can use now[] as a number
#
# counter = 0  # counts how many seconds program takes to finish
# while counter < 1000000:
#     print('Hello')
#     counter += 1
# end = time.time()
#
# print(end - start)  # returns how many seconds program took

#_______________________________________ Import datetime
import datetime

# d = datetime.date(2020, 7 ,22)
# print(d)
# print(type(d))
#
# today = datetime.date.today()  # we make variable out of today
# print(today)  #returns today date
#
# print(today - d)  # returns difference between today and d
#
# print(today.year)  # returns only year
# print(today.day)  # returns only day
# print(today.month) # returns only month
#
# print(today.weekday())  # Monday 0, Sunday 6
# print(today.isoweekday())   # Monday 1, Sunday 7


#__________________
today = datetime.date.today()
some_date = datetime.date(2020, 6, 12)
tdelta = datetime.timedelta(days=7) # will return time delta equal to 7 days

print(today + tdelta)  # will print date 7 days from today

# date2 = date1 + timedelta
# timedelta = date1 - date2


bday = datetime.date(2021, 5, 11) #  my birthday
till_bday = bday - today
print(till_bday)  # will return in days
print(till_bday.days)  # will return in days
print(till_bday.total_seconds())  # will return in seconds



dt_str = 'November 30, 2020'
print(dt_str)
str_to_date = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(str_to_date)

