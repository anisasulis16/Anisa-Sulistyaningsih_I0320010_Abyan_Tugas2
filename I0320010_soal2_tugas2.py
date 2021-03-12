#Menampilkan informasi program
print("Program Identitas")

#Menginputkan variabel nama
nama = input("Masukkan Nama Anda: ")

#Menginputkan variabel umur
tanggal_lahir = int(input("Masukkan Tanggal Lahir: "))
tanggal_sekarang = int(input("Masukkan Tanggal Saat ini: "))
bulan_lahir = int(input("Masukkan Bulan Lahir: "))
bulan_sekarang = int(input("Masukkan Bulan Sekarang: "))
tahun_lahir = int(input("Masukkan Tahun Lahir: "))
tahun_sekarang = int(input("Masukkan Tahun Saat ini: "))

#Menginputkan tinggi badan
tinggi_badan = float(input("Masukkan Tinggi Badan Anda: "))

#Menginputkan ukuran sepatu
ukuran_sepatu = float(input("Masukkan Ukuran Sepatu: "))

#Menginputkan alamat rumah
alamat_rumah = input("Masukkan Alamat Rumah Anda: ")

#Menginputkan pekerjaan
pekerjaan = input("Pekerjaan: ")

#Menghitung umur
kelahiran = tanggal_lahir + (bulan_lahir * 30) + (tahun_lahir * 365)
saat_ini = tanggal_sekarang + (bulan_sekarang * 30) + (tahun_sekarang * 365)

tahun = (saat_ini - kelahiran) / 365
bulan = (tahun - int(tahun)) * 12
hari = (bulan - int(bulan)) * 30

print(".............................")
#Menampilkan hasil proses
print("identitas Pribadi")
print("Nama: ", nama)
print("Anda berumur: ", int(tahun), "tahun", int(bulan), "bulan", int(hari), "hari")
print("Tinggi badan: ", tinggi_badan)
print("Ukuran Sepatu: ", ukuran_sepatu)
print("Alamat rumah: ", alamat_rumah)
print("Pekerjaan: ", pekerjaan)
print(".............................")