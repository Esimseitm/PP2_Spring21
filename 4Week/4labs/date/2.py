import datetime

now = datetime.datetime.now()
yesterday = now - datetime.timedelta(1)
today = now
tomorrow = now + datetime.timedelta(1)
print('yesterday: ' , yesterday)
print('today: ' , now)
print('tomorrow: ' , tomorrow)
