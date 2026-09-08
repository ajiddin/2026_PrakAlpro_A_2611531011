# program ini menggunakan konstata untuk menghitung luas lingkaran
from typing import Final
pi: Final = 3.14
print("pi: %f" % (pi))
jari_1011=float(input("masukkan nilai jari-jari: "))
luas_1011=pi * jari_1011 * jari_1011
print("luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_1011, luas_1011))