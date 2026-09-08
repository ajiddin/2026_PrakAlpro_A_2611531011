# deklarasi variabel dengan tipe data boolean
is_lulus=True
is_cumlaude=True

# menggunakan boolean
nilai_1011=85
batas_lulus_1011=75

#m menentukan nilai boolean dari kondisi
status_kelulusan_1011=nilai_1011>=batas_lulus_1011

print("=== check kelulusan ===")
print("nilai :" , nilai_1011)
print("apakah lulus? :", status_kelulusan_1011)
if is_lulus and is_cumlaude:
    print("selamat anda lulus dengan predikat cum laude")