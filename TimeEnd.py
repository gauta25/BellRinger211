from datetime import datetime
now = datetime.utcnow()
s1 = '{}:{}:{}'.format(now.hour-7, now.minute, now.second)
# print(s1)
# s1 = '13:40:00'
s2 = '14:19:00' # for example
format = '%H:%M:%S'
time1 = datetime.strptime(s1, format)
time2 = datetime.strptime(s2, format)
time = time1 - time2
m = time
# print(now)
