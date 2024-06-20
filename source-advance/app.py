# import mymodule defined-user
import mymodule as md
from mymodule import mahasiswa

# import from buildin
import math
import platform

a = md.increment()

b = md.mahasiswa["nama"]
print(b)

# math
print(math.pow(2, 2))
print(math.pi)
print(math.sin(90))
print(math.cos(20))

#platform
print(platform.system())
print(platform.release())
print(platform.version())

print(mahasiswa["nama"])

# Datetime
from datetime import date

today = date.today()

print(today)

format_date = date.today().strftime("%d-%m-%Y")
print(format_date)

ctime = date.ctime(today)
print(ctime)

import datetime
time = datetime.time(12, 0, 0)

bulan = datetime.datetime(2018, 6, 1)

print(bulan.strftime("%B"))






