# nama = str(input("Masukan Nama: ")) #fungsi input
# uts = float(input("Masukan nilai UTS: ")) 
# uas = float(input("Masukan nilai UAS: "))

# print("Nama anda adalah : ",nama)
# print("Nilai UTS anda adalah : ", uts)
# print("Nilai UAS anda adalah : ", uas)

# # uts 30%
# # uas 50%
# hasil = (0.5*uts)+(0.5*uas) 
# print("hasil akhri nilai anda adalah : ", hasil)











# nim = int(input("Masukan Nomor Induk Mahasiswa : "))
# nama = str(input("Masukan Nama Mahasiswa: "))
# uts = float(input("Masukan nilai UTS: "))
# tugas = float(input("Masukan nilai Tugas: "))
# uas = float(input("Masukan nilai UAS: "))
# hasil = ((uts*0.3) + (tugas*0.2) + (uas*0.5))


# print("Nomor induk mahasiswa : ", nim)
# print("Nama lengkap mahasiswa : ", nama)
# print("nilai UTS : ", uts)
# print("Nilai tugas : ", tugas)
# print("Nilai Uas : ", uas)
# print("Hasil akhir nilai mahasiswa adalah : ",hasil)

# with open("readme.txt", 'r') as file:
#     content = file.read()
#     print(content)


# with open("readme.txt",'w') as file:
#     file.write("Selamat Datang")
#     print("Tulisan telah ditambahkan")

# with open('users.sql', 'r') as database:
#     content = (database.read())
#     print(content)


nama = str(input("Masukkan Nama Karyawan \t:"))
gaji = int(input("Masukkan Gaji Karyawan \t:"))
print("Nama Karyawan \t:", nama)
print("Gaji Karyawan \t: {:,.2f}".format(gaji))
tunjangan = gaji * 0.1
print("Tunjangan Karyawan \t: {:,.2f}".format(tunjangan))
pajak = gaji * 0.15
print("Pajak Karyawan \t: {:,.2f}".format(pajak))
gaji_bersih = gaji + tunjangan - pajak
print("Gaji Bersih Karyawan \t: {:,.2f}".format(gaji_bersih))