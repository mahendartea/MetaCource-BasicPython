<h1> Fungsi/Function </h1>

## 1. Definisi
Fungsi digunakan untuk mengimplementasikan konsep modular(modularity) pada Python. Fungsi ini digunakan untuk menyelesaikan masalah pada program. Fungsi bertugas untuk menjalankan serangkaian perintah secara spesifik. Selama ini kita sudah menggunakan beberapa fungsi bawaan dari python `buldin function`, seperti `print()`, `input()`, `len()`, `append()`, dan lain-lain.
Namun kita dapat membuat fungsi sendiri sesuai kebutuhan. Fungsi yang kita buat sendiri disebut `user defined function`. Fungsi ini dapat digunakan pada program kita sendiri.

## 2. Membuat Fungsi
cara membuat fungsi pada python:
```python
def nama_fungsi(daftar_parameter):
    statement
    return [ekspresi]
```
keterangan:
- `def` : keyword untuk membuat fungsi
- `nama_fungsi` : nama fungsi yang ingin dibuat
- `:` : penanda akhir dari sebuah fungsi
- `daftar_parameter` : parameter yang digunakan pada fungsi
- `statement` : pernyataan yang akan dieksekusi pada fungsi
- `return` : keyword untuk mengembalikan sebuah fungsi
- `[ekspresi]` : ekspresi yang akan dikembalikan

Contoh:
```python
#membuat fungsi
def hello():
    print("Hello World!")
    return "Hello World!"
#memanggil fungsi
hello()
```

## 3. Fungsi dengan Parameter

Dalam `function` pada pemrograman python dapat menggunakan `parameter` sehingga saat pemanggilan `function` user dapat memberikan argument di dalamnya.

misalnya ada sebuah `function` untuk rumus persegi. Maka perlu ada parameter sisi yang diinputkan user.

Berikut adalah skema sintax pada function yang memilki parameter.

```python
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
```

Contoh penggunaan function pada rumus menghitung rumus segitiga adalah sebagai berikut

contoh 2: Menghitung luas segitiga

```python
def luas_segitiga(alas, tinggi):
    luas = alas * tinggi / 2
    return luas
luas = luas_segitiga(10, 5)
print(luas)
```

## 4. Arbitrary Arguments

Dalam `function` pada pemrograman python ada cara penggunaan `arbitrary arguments`. Arbitrary arguments adalah argument yang tidak didefinisikan sebelumnya. Artinya ketika kita tidak mengetahui parameter yang dapat diinput user, kita bisa menggunakan `arbitrary arguments`.

sintak `arbitrary arguments` adalah `*`

contoh:

```python
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
```

## 5. ArbitraryArgument Keyword, **

jika kita menggunakan `arbitrary arguments` pada function, kita juga bisa menggunakan `arbitrary arguments` pada `keyword arguments`

```python
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
```

## 6. Parameter Default

parameter default adalah parameter yang diinputkan secara otomatis ketika sebuah `function` dipanggil.

```python
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function()
my_function("India")
```

## 7. Passing sebuah list sebagai argument

kita bisa memasukkan sebuah list sebagai argument pada sebuah `function`

```python
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
```


[<<Kembali](README.md)
