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
contoh 2: Menghitung luas segitiga

```python
def luas_segitiga(alas, tinggi):
    luas = alas * tinggi / 2
    return luas
luas = luas_segitiga(10, 5)
print(luas)
```



[<<Kembali](README.md)
