print("==========================================================")
print("|    Selamat Datang Di Rental Komputer Rafi Pratama      |")
print("|        Jl. Rawa Bebek No.48, Bekasi Barat              |")
print("==========================================================")

menu = {
    "Paket Reguler": 4000,
    "Paket VIP": 8000,
    "Paket VVIP": 15000,
}
print("==================== Daftar Paket ====================")
for i in menu:
    print("Daftar Paket : ", i, "\t Harga : ", menu[i])
print("Pengguna VVIP diatas 5 jam,- mendapatkan diskon 10%")
print("=====================================================")
Nama_Pengguna = input("Nama Pengguna : ")
Alamat = input("Alamat : ")
Paket = input("Pilih Paket : ")
Waktu = int(input("Jumlah Waktu : "))
bayar = menu[Paket] * Waktu

import time
Tanggal = time.strftime ("%d-%m-%y %H-:%M:%S")

if bayar > 75000:
    Paket = "Paket VVIP"
    diskon = bayar*10/100
    total = bayar - diskon
else:
    total = bayar
    
print("================= Detail Paket =================")
print("Nama Pengguna            : ", Nama_Pengguna)
print("Alamat                   : ",Alamat)
print("Tanggal                  : ",Tanggal)
print("Paket yang dipesan       : ",Paket)
print("Jumlah Yang Dipesan      : ",Waktu)
print("Total Biaya              : ",bayar)
print("Total Yang Harus Dibayar : ", total)
print("=================== Terima Kasih ================")

