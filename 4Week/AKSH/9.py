from datetime import datetime

now = datetime.now()

print(now)
print(now.day)
print(now.year)
print(now.month)

print(now.strftime('%d.%m.%Y'))

print(now.strftime('%A'))

d = datetime(2019, 3, 23, 13, 25)

print(d.strftime('%d/%m/%Y %H:%M'))