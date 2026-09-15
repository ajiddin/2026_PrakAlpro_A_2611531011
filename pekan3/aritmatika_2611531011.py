angka1_1011=int(input("Input angka-1: "))
angka2_1011=int(input("input angka-2: "))

#penjumlahan
hasil1_1011= angka1_1011 + angka2_1011
print("\nOperator penjumlahan")
print("hasil =", hasil1_1011)

#pengurangan
hasil2_1011 = angka1_1011 - angka2_1011
print("\nOperator pengurangan")
print("hasil =", hasil2_1011)

#perkalian
hasil3_1011 = angka1_1011 * angka2_1011
print("\nOperator perkalian")
print("hasil =", hasil3_1011)

#pembagian, pembagian bulat, dan sisa bagi
if angka2_1011 != 0:
    hasil4_1011 = angka1_1011 / angka2_1011
    print("\nOperator pembagian")
    print("hasil =", hasil4_1011)

    hasil5_1011 = angka1_1011 // angka2_1011
    print("\nOperator pembagian bulat")
    print("hasil =", hasil5_1011)

    hasil6_1011 = angka1_1011 % angka2_1011
    print("\nOperator sisa bagi")
    print("hasil =", hasil6_1011)
else:
    print("Angka kedua tidak boleh bernilai 0.")

#pangkat
hasil7_1011 = angka1_1011 ** angka2_1011
print("\nOperator pangkat")
print("hasil =", hasil7_1011)