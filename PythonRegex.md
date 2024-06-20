<h1>Python Regex</h1>

## 12. Python Regex
Python Regex merupakan package/module pada Python. Module ini digunakan untuk menangani Regular Expression.

### 12.1. Apa itu Regular Expression
Regular Expression adalah kumpulan karakter yang menunjukkan pola dari sebuah string. Regular Expression biasanya digunakan untuk menemukan string yang sesuai dengan pola yang kita inginkan.

### 12.2. Module Regex
Python memiliki module regex yang dapat digunakan untuk Regular Expression. Untuk menggunakan module Regex, kita harus mengimportnya terlebih dahulu. Module regex pada python yaitu `re`. Berikut adalah contoh penggunaan module `re`:

```python
import re
```

### 12.3. Regular Expression Python
Cara menggunakan modul `re` ini adalah sebagai berikut : 

```python
import re

text = "The rain in Spain"
x = re.search("^The.*Spain$", text)

if x:
    print("Yes")
else:
    print("No")
```

Output
> Yes

Code di atas menggunakan Regular Expression Python untuk mencari kata `Spain` pada variabel `text`. Jika ditemukan, variabel `x` bernilai `True`, jika tidak ditemukan, variabel `x` bernilai `False`.

### 12.4. Fungsi Regex pada module `re`

Fungsi Regex pada module `re` yaitu `findall()`, `search()`, `split()`, dan `sub()`.

| Fungsi Regex | Deskripsi |
| :--- | :--- |
| `findall()` | Mencari semua string yang cocok dengan pola yang ditentukan. |
| `search()` | Mencari string yang cocok dengan pola yang ditentukan. |
| `split()` | Memisahkan string berdasarkan pola yang ditentukan. |
| `sub()` | Mengganti string yang cocok dengan pola yang ditentukan. |

#### 12.4.1. Fungsi Regex `findall()`

```python
import re

text = "The rain in Spain"
x = re.findall("ai", text)

print(x)
```

Output
> ['ai', 'ai']

Code di atas menggunakan Regular Expression Python untuk mencari kata `ai` pada variabel `text`.

#### 12.4.2. Fungsi Regex `search()`

```python
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())
```

Output
> The first white-space character is located in position: 3

Code di atas menggunakan Regular Expression Python untuk mencari karakter spasi pada variabel `txt`.

#### 12.4.3. Fungsi Regex `split()`

```python
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
```

Output
> ['The', 'rain', 'in', 'Spain']

Code di atas menggunakan Regular Expression Python untuk memisahkan string berdasarkan karakter spasi pada variabel `txt`.

#### 12.4.4. Fungsi Regex `sub()`

```python
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
```

Output
> The9rain9in9Spain

Code di atas menggunakan Regular Expression Python untuk mengganti karakter spasi menjadi angka `9` pada variabel `txt`.

### 12.5. Meta Characters
`Metacharacters` adalah karakter dengan spesial fungsi/maksud.

| Metacharacters   | Deskripsi                                                                             | example |
|:-----------------|:--------------------------------------------------------------------------------------|:--------|
| []               | Sebuah set pada karakter                                                              | `[a-z]` |
| \                | Memberi sinyal urutan khusus (juga dapat digunakan untuk keluar dari karakter khusus) | `\d`    |
| .                | Karakter apa pun (kecuali karakter baris baru)                                        | `\.`    |
| ^                | Memulai string                                                                        | `^The`  |
| $                | Berakhir dengan                                                                       | `Spain$` |
| *                | Nol atau lebih kejadian                                                               | `he.*o` |
| +                | Satu atau lebih kejadian                                                              | `he.+o` |
| ?                | Nol atau satu kejadianl                                                               | `he.?o` |
| {}               | Persis dengan jumlah kejadian yang ditentukan                                         | `{1,3}` |
| ()               | Tangkap dan Group                                                                     |         |

### 12.5 Special Characters
Sebuah karakter spesial atau `special characters` diikuti oleh karakter spesial yang ditentukan di bawah ini dan memiliki makna spesial.

| Special Characters | Deskripsi | example |
|:-------------------|:----------| :--- |
| \A                 |Mengembalikan kecocokan jika karakter yang ditentukan berada di awal string| `\AThe` |
| \b                 |Mengembalikan kecocokan dimana karakter tertentu berada di awal atau di akhir kata ("r" di awal adalah memastikan bahwa string diperlakukan sebagai "string mentah")| `r"\bain"` |
| \B                 |Mengembalikan kecocokan dimana karakter tertentu berada di awal atau di akhir kata ("r" di awal adalah memastikan bahwa string diperlakukan sebagai "string mentah")| `r"\Bain"` |
| \d                 |Mengembalikan kecocokan yang stringnya berisi digit (angka dari 0-9)| `\d` |
| \D                 |Mengembalikan kecocokan yang stringnya TIDAK berisi angka| `\D` |
| \s                 |Mengembalikan kecocokan jika karakter yang ditentukan adalah spasi| `\s` |
| \S                 |Mengembalikan kecocokan jika karakter yang ditentukan bukan spasi| `\S` |
| \w                 |Mengembalikan kecocokan yang stringnya berisi karakter kata apa pun (karakter dari a hingga Z, digit dari 0-9, dan karakter garis bawah _)| `\w` |
| \W                 |Mengembalikan kecocokan yang stringnya berisi karakter kata apa pun (karakter dari a hingga Z, digit dari 0-9, dan karakter garis bawah _)| `\W` |
| \Z                 |Mengembalikan kecocokan jika karakter yang ditentukan berada di akhir string| `\Z` |


