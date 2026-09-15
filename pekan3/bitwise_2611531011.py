#program  ini menggunakan fungsi input ()

print("\n==================================")
print("3. Operator Bitwise")
print("==================================")

angka1_1011 = int(input("masukkan angka bitwise-1: "))
angka2_1011 = int(input("masukkan angka bitwise-2: "))

print("\nangka dalam bentuk desiman dan biner")
print("angka1 =", angka1_1011, "| biner =", bin(angka1_1011))
print("angka2 =", angka2_1011, "| biner =", bin(angka2_1011))

#bitwise AND
hasil1_1011 = angka1_1011 & angka2_1011
print("\nBitwise AND (&)")
print(angka1_1011, "&", angka2_1011, "=", hasil1_1011)
print("biner hasil =", bin(hasil1_1011))
print("biner hasil (8 bit) =", format(hasil1_1011, '08b'))

#bitwise OR
hasil2_1011 = angka1_1011 | angka2_1011
print("\nBitwise OR (|)")
print(angka1_1011, "|", angka2_1011, "=", hasil2_1011)
print("biner hasil =", bin(hasil2_1011))
print("biner hasil (8 bit) =", format(hasil2_1011, '08b'))

#bitwise XOR
hasil3_1011 = angka1_1011 ^ angka2_1011
print("\nBitwise XOR (^)")
print(angka1_1011, "^", angka2_1011, "=", hasil3_1011)
print("biner hasil =", bin(hasil3_1011))
print("biner hasil (8 bit) =", format(hasil3_1011, '08b'))

#bitwise NOT
hasil4_1011 = ~angka1_1011
print("\nBitwise NOT (~)")
print("~", angka1_1011, "=", hasil4_1011)
print("biner hasil =", bin(hasil4_1011))
print("biner hasil (8 bit) =", format(hasil4_1011, '08b'))

#bitwise geser kiri
jumlah_geser = int(input("\nmasukkan jumlah pergeseran bit: "))

hasil5_1011 = angka1_1011 << jumlah_geser
print("\nBitwise Geser Kiri (<<)")
print(angka1_1011, "<<", jumlah_geser, "=", hasil5_1011)
print("biner hasil =", bin(hasil5_1011))
print("biner hasil (8 bit) =", format(hasil5_1011, '08b'))

#bitwise geser kanan
hasil6_1011 = angka1_1011 >> jumlah_geser
print("\nBitwise Geser Kanan (>>)")
print(angka1_1011, ">>", jumlah_geser, "=", hasil6_1011)
print("biner hasil =", bin(hasil6_1011))
print("biner hasil (8 bit) =", format(hasil6_1011, '08b'))