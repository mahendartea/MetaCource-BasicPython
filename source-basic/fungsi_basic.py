def kubus():
    s = 10
    v = s*s*s;
    return v


print(kubus())

print("nilai dari volume kubus adalah : ", kubus())

def segitiga(alas, tinggi):
    luas = alas * tinggi / 2
    return "Hasil luas segitia adalah ", luas


print(segitiga(10, 5))

def unknown(*args):
    print(args[0], args[1], args[2])

unknown("budi", "Dodi", "Ammar")

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function()
my_function("India")

def buah(fruits):
    for x in fruits:
        print(x)

fruits = ["budi", "dodi", "ammar"]

buah(fruits)

def suhu_udara (daerah, derajat = 30, satuan = 'celcius'):
  """
  Fungsi ini bertugas untuk menampilkan teks yang memberikan informasi 
  tentang suhu udara di suatu daerah.

  Args:
      daerah (str): daerah yang ingin diketahui suhu udara
      derajat (int, optional): derajat suhu udara. Defaults to 30.
      satuan (str, optional): satuan derajat suhu udara. Defaults to 'celcius'.

  Returns:
      String    
  """

  print(f"Suhu udara di {daerah} adalah {derajat} {satuan}")

suhu_udara("Jawa Timur", 25, 'celcius')
