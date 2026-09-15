angka1_1011 = int(input("Input angka-1: "))
angka2_1011 = int(input("Input angka-2: "))

print("\nnilai awal angka1_1011 =", angka1_1011)
print("nilai awal angka2_1011 =", angka2_1011)

#assignment biasa
hasil1_1011 = angka1_1011
print("\nAssignment biasa (=)")
print("hasil =", hasil1_1011)

#assignment penambahan
hasil2_1011 = angka1_1011
hasil2_1011 += angka2_1011
print("\nAssignment penambahan (+=)")
print("hasil =", hasil2_1011)

#assignment pengurangan
hasil3_1011 = angka1_1011
hasil3_1011 -= angka2_1011
print("\nAssignment pengurangan (-=)")
print("hasil =", hasil3_1011)

#assignment perkalian
hasil4_1011 = angka1_1011
hasil4_1011 *= angka2_1011
print("\nAssignment perkalian (*=)")
print("hasil =", hasil4_1011)

#assignment pembagian
if angka2_1011 != 0:
    hasil5_1011 = angka1_1011
    hasil5_1011 /= angka2_1011
    print("\nAssignment pembagian (/=)")
    print("hasil =", hasil5_1011)

    #assignment pembagian bulat
    hasil6_1011 = angka1_1011
    hasil6_1011 //= angka2_1011
    print("\nAssignment pembagian bulat (//=)")
    print("hasil =", hasil6_1011)

    #assignment sisa bagi
    hasil7_1011 = angka1_1011
    hasil7_1011 %= angka2_1011
    print("\nAssignment sisa bagi (%=)")
    print("hasil =", hasil7_1011)
else:
    print("\npembagian tidak dapat dilakukan")
    print("angka kedua tidak boleh bernilai 0.")

#operator tambahan: assignment pangkat
hasil8_1011 = angka1_1011
hasil8_1011 **= angka2_1011
print("\nAssignment pangkat (**=)")
print("hasil =", hasil8_1011)