# # kondisi if
# a = 10
# if a == 11: #benar jalankan dibawahnya
#     print("Benar")

# # kondisi if else
# a = 20
# if a == 21:
#     print("Benar")
# else:
#     print("Salah")

# # kondisi if elif
# a = 20
# if a == 30:
#     print("Benar 30")
# elif a == 20:
#     print("yang benar 20")
# else:
#     print("Salah")
#
# # kondisi dengan nilai boolean
# a = False
# b = True
# c = True

# if a:
#     print("A Benar")
# elif b:
#     print("Salah A, tetapi B Benar")
# elif c:
#     print("C Benar, yang salah")
# else:
#     print("salah semua")
#
# # kondisi dengan operator logika
# a = True
# b = False
# c = True

# if a and b:
#     print("Benar")
# elif a or b:
#     print("Salah 1")
# else:
#     print("Salah 2")

# kondisi dengan operator pembanding
# a = 10
# b = 20
# #
# if a < b:
#     print("Benar, A lebih kecil daripada B")
# elif a > b:
#     print("Benar A lebih besar daripada B")
# else:
#     print("Pernyataan Salah")
#
# #kondisi dengan operator identitas
# a = 10
# b = [1, 2, 3, 4, 5, 10]

# if a in b:
#     print("Ada A di dalam B")
# elif a not in b:
#     print("Tidak ada A di dalam B")
#
# #kondisi dengan operator not
# a = False

# if not a:
#     print("Benar")
# else:
#     print("Salah")
#
# # Switch Case
# print('''
# 1. Pemrograman Framework
# 2. Datamining
# 3. Network Security
# 4. Computer Vision
# 5. SIG
# lainnya. Gak kuliah lagi

# ''')
# inputan = input("Masukkan angka: ")

# match inputan:
#     case "1":
#         print("Pemrograman Framework \t : 3 SKS")
#     case "2":
#         print("Datamining \t : 3 SKS")
#     case "3":
#         print("Network Security \t : 3 SKS")
#     case "4":
#         print("Computer Vision \t : 3 SKS")
#     case "5":
#         print("SIG \t : 3 SKS")
#     case _:
#         print("Gak kuliah lagi \t : DO")
#
# # Ternary Operator
# a = 10

# print("Benar") if a == 10 else print("Salah")
#
#
#
# nim = int(input("Masukan Nomor Induk Mahasiswa : "))
# nama = str(input("Masukan Nama Mahasiswa: "))
# nilai = int(input("Masukan nilai final: "))
# if nilai >= 80:
#     status = "Lulus"
# else:
#     status = "Tidak Lulus"

# print("=============================")
# print("Nomor induk mahasiswa : ", nim)
# print("Nama lengkap mahasiswa : ", nama)
# print("Nilai \t: ", nilai)
# print("Status \t: ", status)

# nim = int(input("Masukan Nomor Induk Mahasiswa : "))
# nama = str(input("Masukan Nama Mahasiswa: "))
# tugas = int(input("Masukan nilai Tugas: "))
# uts = int(input("Masukan nilai UTS: "))
# uas = int(input("Masukan nilai UAS: "))
# hasil = (0.2*tugas)+(0.3*uts)+(0.5*uas)

# if hasil >= 80:
#     status = "Lulus"
# else:
#     status = "Tidak Lulus"

# print("=============================")
# print("Nomor induk mahasiswa : ", nim)
# print("Nama lengkap mahasiswa : ", nama)
# print("Nilai Tugas \t: ", tugas)
# print("Nilai UTS \t: ", uts)
# print("nilai UAS \t: ", uas)
# print("Nilai Akhir adalah : ", hasil)
# print("Keterangan : ", status)

