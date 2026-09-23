
print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

# Input data pengunjung
nama_1011 = input("Masukkan Nama Pengunjung        : ")
umur_1011 = int(input("Input umur anda                 : "))
sim_1011 = input("Apakah Anda Sudah Punya SIM C (y/t): ").strip().lower()[0]
jumlah_tiket_1011 = int(input("Masukkan jumlah tiket           : "))

# Validasi jumlah tiket
if jumlah_tiket_1011 <= 0:
    print("Peringatan: Kuota tiket tidak valid.")

# Pilihan paket wahana
print("\nPilihan Paket Wahana (1-5):")
print("1. Safari Rimba         (Rp 50,000)")
print("2. Arung Jeram          (Rp 75,000)")
print("3. Motor ATV Ekstrim    (Rp 120,000)")
print("4. Roller Coaster Kilat (Rp 100,000)")
print("5. All-Access VIP       (Rp 220,000)")

paket_1011 = int(input("Masukkan nomor paket (1-5) : "))

# Pemilihan wahana
match paket_1011:
    case 1:
        nama_wahana_1011 = "Wahana Safari Rimba"
        harga_satuan_1011 = 50000
    case 2:
        nama_wahana_1011 = "Wahana Arung Jeram"
        harga_satuan_1011 = 75000
    case 3:
        nama_wahana_1011 = "Wahana Motor ATV Ekstrim"
        harga_satuan_1011 = 120000
    case 4:
        nama_wahana_1011 = "Wahana Roller Coaster Kilat"
        harga_satuan_1011 = 100000
    case 5:
        nama_wahana_1011 = "Wahana All-Access VIP"
        harga_satuan_1011 = 220000
    case _:
        print("Paket wahana tidak valid!")
        print("Program Selesai")
        exit()

# Validasi izin wahana 
print("\n--- KELAYAKAN PENGENDARA WAHANA ---")

if paket_1011 == 3 and umur_1011 >= 17 and sim_1011 == "y":
    print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")

elif paket_1011 == 3 and umur_1011 >= 17 and sim_1011 != "y":
    print("Status Akses: Anda sudah dewasa tetapi tidak boleh bawa motor ATV, wajib didampingi.")

elif paket_1011 == 3 and umur_1011 < 17 and sim_1011 == "y":
    print("Status Akses: Identitas tidak valid: Belum cukup umur memiliki SIM.")

elif paket_1011 == 3 and umur_1011 < 17 and sim_1011 != "y":
    print("Status Akses: Anda belum cukup umur dan tidak boleh bawa motor ATV.")

elif paket_1011 != 3 and umur_1011 >= 10:
    print("Status Akses: Anda memenuhi batas umur untuk wahana.")

else:
    print("Status Akses: Anda belum cukup umur untuk wahana ini.")

# Input member dan kode promo
is_member_1011 = input("Apakah Anda member? (y/t): ").strip().lower()
kode_promo_valid_1011 = input("Apakah kode promo valid? (y/t): ").strip().lower()

# Menghitung subtotal
subtotal_1011 = harga_satuan_1011 * jumlah_tiket_1011

# Menghitung diskon 
total_diskon_persen_1011 = 0

if subtotal_1011 >= 200000:
    total_diskon_persen_1011 += 10

if is_member_1011 in ["y", "ya"]:
    total_diskon_persen_1011 += 5

if kode_promo_valid_1011 in ["y", "ya"]:
    total_diskon_persen_1011 += 15

if jumlah_tiket_1011 >= 5:
    total_diskon_persen_1011 += 5

# Menghitung pembayaran
nominal_diskon_1011 = subtotal_1011 * (total_diskon_persen_1011 / 100)
total_bayar_1011 = subtotal_1011 - nominal_diskon_1011

# Rincian pembayaran
print("\n--- RINCIAN PEMBAYARAN ---")
print("Nama Pengunjung  :", nama_1011)
print("Wahana           :", nama_wahana_1011)
print("Jumlah Tiket     :", jumlah_tiket_1011)
print(f"Subtotal Belanja : Rp {subtotal_1011:,.0f}")
print(f"Total Diskon     : {total_diskon_persen_1011}% (Rp {nominal_diskon_1011:,.0f})")
print(f"Total Bayar      : Rp {total_bayar_1011:,.0f}")
print("Catatan Layanan  : Terima kasih telah berkunjung.")
print("\nProgram Selesai")