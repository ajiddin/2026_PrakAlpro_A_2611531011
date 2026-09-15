#program operator keanggotaan dan identitas
print("==================================")
print("1. Operator Keanggotaan")
print("==================================")

#input beberapa data yang dipisahkan dengan koma
input_data_1011 = input("Input beberapa angka, pisahkan dengan koma: ")

#mengubah input menjadi list integer
data_1011 = [int(angka.strip()) for angka in input_data_1011.split(",")]

nilai_dicari_1011 = int(input("Input nilai yang dicari: "))

#operator in
hasil1_1011 = nilai_dicari_1011 in data_1011
print("\nOperator in")
print(nilai_dicari_1011, "in", data_1011, "=", hasil1_1011)

#operator not in
hasil2_1011 = nilai_dicari_1011 not in data_1011
print("\nOperator not in")
print(nilai_dicari_1011, "not in", data_1011, "=", hasil2_1011)

print("\n==================================")
print("2. Operator Identitas")
print("==================================")

#objek1 menggunakan list dari input pengguna
objek1_1011 = data_1011

#objek2 merujuk pada objek yang sama dengan objek1
objek2_1011 = objek1_1011

#objek3 memiliki isi sama, tetapi merupakan objek yang baru
objek3_1011 = data_1011.copy()

print("objek1 =", objek1_1011)
print("objek2 =", objek2_1011)
print("objek3 =", objek3_1011)

#operator is
hasil3_1011 = objek1_1011 is objek2_1011
print("\nOperator is")
print("objek1 is objek2 =", hasil3_1011)

#operator is not
hasil4_1011 = objek1_1011 is not objek3_1011
print("\nOperator is not")
print("objek1 is not objek3 =", hasil4_1011)

#membandingkan identitas dan nilai
print("\nperbandingkan identitas dan nilai")
print("objek1 is objek3 =", objek1_1011 is objek3_1011)
print("objek1 == objek3 =", objek1_1011 == objek3_1011)
