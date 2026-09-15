#memasukkan nilai boolean
#input tidak peka terhadap huruf besar dan kecil
a1_1011 = input("Input nilai boolean-1 (True/False): ").strip().lower() == "true"
a2_1011 = input("Input nilai boolean-2 (True/False): ").strip().lower() == "true"

print("\nA1 =", a1_1011)
print("A2 =", a2_1011)

#konjungsi: bernilai true jika keduanya true
hasil1_1011 = a1_1011 and a2_1011
print("\nKonjungsi (AND)")
print("A1 AND A2 =", hasil1_1011)

#disjungsi: bernilai true jika salah satu true
hasil2_1011 = a1_1011 or a2_1011
print("\nDisjungsi (OR)")
print("A1 OR A2 =", hasil2_1011)

#negasi: A1: membalik nilai A1
hasil3_1011 = not a2_1011
print("\nNegasi (NOT)")
print("NOT A2 =", hasil3_1011)

#xor: bernilai true jika kedua nilai berbeda
hasil4_1011 = a1_1011 != a2_1011
print("\ndiskonjungsi eksklusif (XOR)")
print("A1 XOR A2 =", hasil4_1011) 
