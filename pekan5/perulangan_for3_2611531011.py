ulang_1011 = int(input("masukkan jumlah perulangan: "))

jumlah_1011=0
for i_1011 in range(1, ulang_1011+1):
    print(i_1011, end=" ")
    jumlah_1011 = jumlah_1011 + i_1011

    if i_1011<ulang_1011:
        print("+", end=" ")
    else:
        print("=", jumlah_1011, end=" ")
print()
print("jumlah =", jumlah_1011)