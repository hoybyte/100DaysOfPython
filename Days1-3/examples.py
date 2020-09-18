from datetime import datetime
from datetime import date
from datetime import timedelta

today = date.today()
print(today)

November = date(2020, 11, 1)

print((November - today).days)

wake_up = timedelta(hours=12)
now = datetime.now()
print(wake_up + now)
print(str(wake_up + now))