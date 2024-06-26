<h1>Python JSON </h1>

## 1. Apa itu JSON
Json adalah sintaks untuk menyimpan dan menukar data.
JSON adalah file format untuk menyimpan data yang biasanya digunakan oleh bahasa pemrograman untuk berinteraksi dengan data. Format penulisan datanya adalah menggunakan format data pada javascript atau kepanjangan JSON adalah javascript object notation.

## 2. Module JSON
`Module` JSON terdapat pada `python`. Module ini digunakan untuk menangani JSON. Untuk memakai module JSON, kita harus mengimportnya terlebih dahulu. Module JSON pada python yaitu `json`. Berikut adalah contoh penggunaan module `json`:

```python
import json
```

## 3. Parse JSON - Convert JSON to Python
Jika kita ingin melakukan parse JSON maka kita dapat menggunakan method `json.loads()`. Method ini akan mengembalikan sebuah dictionary yang berisi data JSON yang kita parse.

```python
import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
```
output:
> 30

## 4. Convert Python to JSON
Bagaimana mengkonversi Python ke JSON? Berikut adalah contohnya.

```python
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
```
output:
> '{"name": "John", "age": 30, "city": "New York"}'

kita dapat melakukan konversi python objects berikut menjadi JSON String:

- dict
- list
- tuple
- string
- int
- float
- True
- False
- None

contoh penggunaan yaitu menggunakan method `json.dumps()`

```python
import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
```
Konversikan objek Python yang berisi semua tipe data legal :

```python
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
```

## 5. Memformat Hasil JSON

Contoh di atas mencetak string JSON, tetapi tidak mudah dibaca, tanpa lekukan dan jeda baris. Metode `json.dumps()` memiliki parameter untuk memudahkan membaca hasilnya:

```python
json.dumps(x, indent=4)
```

Kita juga dapat menentukan pemisah, nilai defaultnya adalah (", ", ":"), yang berarti menggunakan koma dan spasi untuk memisahkan setiap objek, serta titik dua dan spasi untuk memisahkan kunci dari nilai:

```python
json.dumps(x, indent=4, separators=(". ", " = "))
```

## 6. Pengurutan JSON

Pengurutan JSON dapat dilakukan dengan menggunakan method `json.dumps()` dengan parameter `sort_keys=True`. Ini akan mengurutkan semua kunci dari JSON secara otomatis.

```python
json.dumps(x, indent=4, sort_keys=True)
````
