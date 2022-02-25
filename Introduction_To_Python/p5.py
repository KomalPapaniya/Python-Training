import datetime
dateTime = datetime.datetime.now()
print(dateTime)

year = lambda x: x.year
print(year(dateTime))

month = lambda x: x.month
print(month(dateTime))

date = lambda x: x.day
print(date(dateTime))

time = lambda x: x.time()
print(time(dateTime))