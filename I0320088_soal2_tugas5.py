x = input("Masukkan Nama: ")
y = int(input("Masukkan Nilai: "))
nilai = y
if nilai >= 85 and nilai <= 100:
    print("Halo", x +'!', "Nilai anda setelah dikonversi adalah A")
elif nilai >= 80 and nilai < 85 :
    print("Halo", x +'!', "Nilai anda setelah dikonversi adalah A-")
elif nilai >= 75 and nilai < 80:
    print("Halo", x +'!', "Nilai anda setelah dikonversi adalah B+")
elif nilai >= 70 and nilai < 75:
    print("Halo", x +'!', "Nilai anda setelah dikonversi adalah B")
elif nilai >= 65 and nilai < 70:
    print("Halo", x +'!', "Nilai anda setelah dikonversi adalah C+")
elif nilai >= 60 and nilai < 65:
    print("Halo", x +'!', "Nilai anda setelah dikonversi adalah C")
elif nilai < 60:
    print("Halo", x +'!', "Nilai anda setelah dikonversi adalah E")
else:
    print("Halo", x +'!', "Nilai yang anda masukkan tidak valid, silahkan masukkan ulang!")
print()


