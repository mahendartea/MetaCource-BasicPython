# kondisi if

a = 10
if a == 10:
    print("Benar")

# kondisi if else
a = 20
if a == 20:
    print("Benar")
else:
    print("Salah")

# kondisi if elif
a = 30
if a == 30:
    print("Benar")
elif a == 20:
    print("Salah")
else:
    print("Salah")

# kondisi dengan nilai boolean
a = True
b = False
c = True

if a:
    print("Benar")
elif b:
    print("Salah")
else:
    print("Salah")

# kondisi dengan operator logika
a = True
b = False
c = True

if a and b:
    print("Benar")
elif a or b:
    print("Salah")
else:
    print("Salah")

# kondisi dengan operator pembanding
a = 10
b = 20

if a < b:
    print("Benar")
elif a > b:
    print("Salah")
else:
    print("Salah")

#kondisi dengan operator identitas
a = 10
b = [1, 2, 3, 4, 5]

if a in b:
    print("Benar")
elif a not in b:
    print("Salah")

#kondisi dengan operator not
a = 10

if not a:
    print("Benar")
else:
    print("Salah")

# Switch Case
inputan = input("Masukkan angka: ")

match inputan:
    case "1":
        print("Satu")
    case "2":
        print("Dua")
    case "3":
        print("Tiga")
    case "4":
        print("Empat")
    case "5":
        print("Lima")
    case _:
        print("Salah")

# Ternary Operator
a = 10

print("Benar") if a == 10 else print("Salah")



