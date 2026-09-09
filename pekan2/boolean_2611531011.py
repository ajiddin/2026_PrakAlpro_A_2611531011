# Buat file dengan nama Boolean_2611531021
# Nama variabel ditambah 4 digit nim terakhir contoh: nilai_1234
# Deklarasi variabel dengan tipe data Boolean
is_lulus_1011=True
is_cumlaude_1011=True

# menggunakan boolean
nilai_1011=85
batas_lulus_1011=75

#m menentukan nilai boolean dari kondisi
status_kelulusan_1011=nilai_1011>=batas_lulus_1011

print("=== check kelulusan ===")
print("nilai :" , nilai_1011)
print("apakah lulus? :", status_kelulusan_1011)
if is_lulus_1011 and is_cumlaude_1011:
    print("selamat anda lulus dengan predikat cum laude")