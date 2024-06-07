<h1> Python Advance </h1>

## 10. Datetime

`datetime` merupakan package/module pada python. Module ini digunakan untuk menangani waktu. 
terdapat beberapa objek yang terdapat pada module `datetime` seperti `date` dan `time`.

### 10.1. Date

`Date` adalah objek yang terdapat pada module `datetime`.
Berikut adalah penggunaan module `date`:

```python

from datetime import date


today = date.today()

print(today)

format_date = date.today().strftime("%d-%m-%Y")
print(format_date)

ctime = date.ctime(today)
print(ctime)

```

Output
> 2024-06-7

> 7-06-2024

> Thu Jun  7 00:00:00 2024

### 10.2. Time

`Time` adalah objek yang terdapat pada module `datetime`.
Berikut adalah penggunaan module `time`:

```python

from datetime import time

now = time.now()
print(now)

print(time.ctime())
```

Output
> 00:00:00

> Thu Jun  7 00:00:00 2024

### 10.3. Strftime() method

Datetime memiliki method `strftime()` yang dapat digunakan untuk menampilkan waktu dengan memformat date object.


```python
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))
```
output
> June

Referensi semua kode format date di atas adalah sebagai berikut:

| Kode Format | Deskripsi | example |
|-------------|-----------|---------|
| %a | Weekday, short version | Wed |
| %A | Weekday, full version | Wednesday |
| %w | Weekday, number (0 = Sunday) | 2 |
| %d | Day of month, 2 digits with leading zeros | 01 |
| %b | Month name, short version | Sep |
| %B | Month name, full version | September |
| %m | Month number, 2 digits with leading zeros | 09 |
| %y | Year, 2 digits | 18 |

[Referensi](https://www.w3schools.com/python/python_datetime.asp)

