<h1> Operator Kondisi </h1>

# Kondisi pada Pemrograman Python

## 1.1 Kondisi 

### 1.1.1 Kondisi if

Kondisi if merupakan sebuah percabangan yang akan dieksekusi jika sebuah syarat bernilai benar. Contoh: `if a == 10`

Contoh penggunaan if

```python
a = 10
if a == 10:
    print("Benar")
```

### 1.1.2 Kondisi if-else

Kondisi if-else merupakan sebuah percabangan yang akan dieksekusi jika sebuah syarat bernilai benar dan jika syarat bernilai salah. Contoh: `if a == 10: print("Benar") else: print("Salah")`

contoh penggunaan if-else

```python
a = 10
if a == 10:
    print("Benar")
else:
    print("Salah")
```

### 1.1.3 Kondisi if-elif-else

Kondisi if-elif-else merupakan sebuah percabangan yang akan dieksekusi jika sebuah syarat bernilai benar, jika syarat bernilai salah, dan jika syarat bernilai salah, jika syarat bernilai salah.

Contoh penggunaan if-elif-else

```python
a = 10
if a == 10:
    print("Benar")
elif a == 20:
    print("Salah")
else:
    print("Salah")
```

### 1.1.4 Kondisi dengan Nilai Boolean

Kondisi dengan Nilai Boolean adalah sebuah kondisi yang didefinisikan menggunakan tipe data boolean. Contoh: `a = True`, `b = False`, `c = True`

contoh penggunaan kondisi dengan nilai boolean

```python
a = True
b = False
c = True

if a:
    print("Benar")
elif b:
    print("Salah")
else:
    print("Salah")
```

### 1.1.5 Kondisi dengan Operator Logika

Kondisi dengan Operator Logika adalah sebuah kondisi yang didefinisikan menggunakan operator logika. Contoh: `a and b`, `a or b`, `not a`

contoh penggunaan kondisi dengan operator logika

```python
a = True
b = False
c = True

if a and b:
    print("Benar")
elif a or b:
    print("Salah")
else:
    print("Salah")
```

### 1.1.6 Kondisi dengan Operator Perbandingan

Kondisi dengan Operator Perbandingan adalah sebuah kondisi yang didefinisikan menggunakan operator perbandingan. Contoh: `a == b`, `a != b`, `a > b`, `a < b`, `a >= b`, `a <= b`

contoh penggunaan kondisi dengan operator perbandingan

```python
a = 10
b = 5

if a == b:
    print("Benar")
elif a != b:
    print("Salah")
else:
    print("Salah")
```


### 1.1.7 Kondisi dengan Operator Identity

Kondisi dengan Operator Identity adalah sebuah kondisi yang didefinisikan menggunakan operator identity. Contoh: `a is b`, `a is not b`

contoh penggunaan kondisi dengan operator identity

```python
a = 10
b = 5

if a is b:
    print("Benar")
elif a is not b:
    print("Salah")
```

### 1.1.8 Kondisi dengan Operator Membership

Kondisi dengan Operator Membership adalah sebuah kondisi yang didefinisikan menggunakan operator membership. Contoh: `a in b`, `a not in b`

contoh penggunaan kondisi dengan operator membership

```python
a = 10
b = [1, 2, 3, 4, 5]

if a in b:
    print("Benar")
elif a not in b:
    print("Salah")
```

## 2.1 Switch Case

### 2.1.1 Switch Case

Switch Case merupakan sebuah percabangan yang akan dieksekusi jika sebuah syarat bernilai benar. Contoh: `switch (a) {case 10: print("Benar")}`

contoh penggunaan switch case

```python
a = 10
switch (a) {
    case 10:
        print("Benar")
    case 20:
        print("Salah")
}
```


## 3.1 Ternary Operator

### 3.1.1 Ternary Operator

Ternary Operator merupakan sebuah percabangan yang akan dieksekusi jika sebuah syarat bernilai benar. Contoh: `a == 10 ? print("Benar") : print("Salah")`

Contoh penggunaan ternary operator

```python
a = 10
a == 10 ? print("Benar") : print("Salah")
```
[<<Kembali](README.md)


