print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")
nama_1011 = input("Masukkan Nama Mahasiswa : ")
kelamin_1011 = input("Masukkan Jenis Kelamin (L/P): ")
umur_1011 = int(input("Masukkan Umur : "))
skor_1011 = float(input("Masukkan Skor Tes Awal : "))

alamat_1011 = """
Komplek Palm Griya Indah II,
Kecamatan Kuranji,
Kota Padang,
Sumatera Barat,
Indonesia
"""
from typing import Final
kkm_1011: Final = 75.0
token_1011 = 100+3j
lulus_1011 = skor_1011 > kkm_1011

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print("Nama Mahasiswa : ",nama_1011," | ",type(nama_1011))
print("Jenis Kelamin : ",kelamin_1011," | ",type(kelamin_1011))
print("Alamat Domisili : ",alamat_1011," | ",type(alamat_1011))
print("Umur : ",umur_1011," tahun | ",type(umur_1011))
print("Skor Tes Awal : ",skor_1011," | ",type(skor_1011))
print("ID Token Sinyal: ",token_1011," | ",type(token_1011))

print("=== STATUS KELULUSAN PRAKTIKUM ===")
print("Batas Minimum Nilai: ",kkm_1011," | ",type(kkm_1011))
print("Apakah Dinyatakan Lulus?: ",lulus_1011," | ",type(lulus_1011))