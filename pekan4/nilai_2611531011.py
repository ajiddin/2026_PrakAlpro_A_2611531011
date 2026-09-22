#program ini menggunakan fungsi input ()
#program konversi nilai angka ke huruf

nilai_1011 = int(input("Masukkan nilai angka : "))

if nilai_1011 >= 81:
    print("A")
elif nilai_1011 >= 70:
    print("B")
elif nilai_1011 >= 60:
    print("C")
elif nilai_1011 >= 50:
    print("D")
else:
    print("E")