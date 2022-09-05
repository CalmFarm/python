import datetime as dt

print('오늘 = ',dt.datetime.now())

hundred = dt.timedelta(days=100)
plus100day=dt.datetime.now()+hundred

print('100일 후 ', plus100day)