import datetime

now = datetime.datetime.now()
now = now - datetime.timedelta(5)
print('5 day before: ' , now)