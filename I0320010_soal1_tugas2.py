#Program Perhitungan
print("Program Perhitungan Luas")
print("........................")

#Menghitung Luas Persegi Panjang

#Menampilkan informasi program Perhitungan
print("Perhitungan Luas Persegi Panjang")

#Menginputkan nilai variabel panjang dan lebar
panjang = float(input("Masukkan nilai panjang: "))
lebar = float(input("Masukkan nilai lebar: "))

#Memproses luas persegi panjang
luas_persegi_panjang = panjang * lebar

#Menampilkan Hasil luas persegi panjang
print("Luas Persegi Panjang: ", luas_persegi_panjang)

print("..........................")
#Menghitung Luas Lingkaran

#Menampilkan informasi program perhitungan
print("Perhitungan Luas Lingkaran")

#Menginputkan nilai variabel phi dan r
phi = 22/7
r = float(input("Masukkan nilai jari-jari: "))

#Memproses Luas Lingkaran
luas_lingkaran = phi * r * r

#Menampilkan Hasil Luas Lingkaran
print("Luas Lingkaran: ", luas_lingkaran)

print("..........................")
#Menghitung Luas Kubus

#Menampilkan informas program perhitungan
print("Perhitungan Luas Kubus")

#Menginputkan nilai variabel s
s = float(input("Masukkan nilai sisi: "))

#Memproses Luas Kubus
luas_kubus = 6 * s * s

#Manampilkan Hasil Luas Kubus
print("Luas Kubus: ", luas_kubus)

print("...........................")
#Menghitung Konversi suhu Celcius  ke Fahrenheit

#Menampilkan informasi program perhitungan
print("Mengitung Konversi Suhu Celcius ke Fahrenheit")

#Menginputkan nilai variabel  suhu celcius
C = float(input("Masukkan nilai suhu(Celcius): "))

#Memproses Konversi suhu Celcius ke fahrenheit
F = (9 / 5 * C) + 32

#Menampilkan hasil konversi suhu Celcius ke Fahrenheit
print("Suhu Celcius: ", C)
print("Suhu Fahrenheit: ", F)

print("...........................")
#Menghitung Konversi suhu Reamur ke Kelvin

#Menampilkan informasi program perhitungan
print("Mengitung Konversi Suhu Reamur ke Kelvin")

#Menginputkan nilai variabel  suhu reamur
R = float(input("Masukkan nilai suhu(Reamur): "))

#Memproses Konversi suhu Reamur ke Kelvin
K = (5 / 4 * R) + 273

#Menampilkan hasil konversi suhu Reamur ke Kelvin
print("Suhu Celcius: ", C)
print("Suhu Kelvin: ", K)
print("...........................")