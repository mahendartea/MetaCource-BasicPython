<h1>Package PIP</h1>

## 1. Apa itu PIP?
Pip adalah `package manager` yang digunakan untuk menginstal package/package baru pada `Python`. Terdapat banyak libarary/package yang dapat di install menggunakan pip.

Untuk mengecek apakah `pip` sudah di install di python kita dapat menulis peritah di `terminal` (mac/linux) atau di `cmd` atau di `powershell` seperti berikut :

```bash
pip --version
```

## 2. Install PIP
Bagaimana cara install PIP?
1. Pertema kunjungi dulu sebuah website mengunjungi tautan berikut : [link](https://pypi.org/project/pip/)

2. Atau install langsung menggunakan perintah berikut 
- install di OS mac/linux
    ```bash
    python get-pip.py
    ```
- install di OS windows
    ```bash
    py -m ensurepip --upgrade
    ```
ketika berhasil di install maka kita dapat mengeceknya dengan perintah `pip --version` seperti di atas.

## 3. Install Package menggunakan `pip`
Untuk menginstall `package` menggunakan pip pertama kita harus tau dulu package apa yang mau diinstall atau dapat di search pada web `https://pypi.org`. Ketika sudah diketahui `package` apa yang mau di install maka ketika perintah pada terminal. Contoh ketika kita mau install `package` bernama `camelcase` berikut cara installnya di terminal.
```bash
pip install camelcase
```

## 4. Menggunakan `package` di python
untuk menggunakan `package` yang telah di install maka kita dapat menggunakan `package` tersebut di syntax/code python kita dengan cara yang sama dengan menggunakan `module` pada python. Berikut contohnya.

```python
import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))
```
Output
> Hello World

## 5. Melihat package terinstall
Untuk melihat `package` terinstall dapat menggunakan perintah berikut pada terminal.
```bash
pip list
```
output (contoh)
```bash
Package         Version
-----------------------
camelcase       0.2
mysql-connector 2.1.6
pip             18.1
pymongo         3.6.1
setuptools      39.0.1
```

## 6. Uninstall `Package`
Untuk menghapus package yang terinstall pada `pip` dapat menggunakan perintah berikut pada terminal.

```bash
pip uninstall camelcase
```
