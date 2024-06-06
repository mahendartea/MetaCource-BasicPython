# jawab = "y"
# while jawab == "y":
#     angka = int(input("Masukkan angka: "))
#     if(angka > 1):
#         for i in range(2, angka):
#             if(angka % i == 0):
#                 print(angka, "bukan bilangan prima")
#                 print("Karena ", i, "adalah kelipatan dari ", angka)
#         else:
#             print(angka, "bukan bilangan prima")
#     else:
#         print(angka, "bukan bilangan prima")
#     print()
#     jawab = input("Apakah anda ingin melanjutkan (y/t)? ")
jawab = "y"
while jawab == "y":
    angka = int(input("Masukkan angka: "))
    if(angka % 4 == 0):
        if(angka % 100 == 0):
            if(angka % 400 == 0):
                print(angka, "adalah tahun kabisat")
            else:
                print(angka, "bukan tahun kabisat")
        else:
            print(angka, "adalah tahun kabisat")
    else:
        print(angka, "bukan tahun kabisat")
    print()
    jawab = input("Apakah anda ingin melanjutkan (y/t)? ")