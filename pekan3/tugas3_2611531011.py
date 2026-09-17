# ==============================================================================
# PROGRAM SIMULASI TRANSAKSI DAN VALIDASI AKSES TOKO
# ==============================================================================

# 1. INPUT DATA UTAMA
print("=== SISTEM TRANSAKSI TOKO ===")
nama_1011 = input("Masukkan Nama Pelanggan : ")
status_1011 = input("Masukkan Status Pelanggan (member/nonmember) : ")
total_belanja_1011 = int(input("Masukkan Total Belanja : "))
jumlah_barang_1011 = int(input("Masukkan Jumlah Barang : "))
kode_promo_1011 = input("Masukkan Kode Promo : ")

# List Promo yang Diterima
daftar_promo_1011 = ["SABTUMAJU", "MINGGUSERU", "LAPANDELAPAN", "HEMATBERSAMA"]

# 2. EVALUASI KONDISI (OPERATOR PERBANDINGAN & KEANGGOTAAN)
is_member_1011 = (status_1011.lower() == "member")
is_cukup_belanja_1011 = total_belanja_1011 >= 200000
is_cukup_barang_1011 = jumlah_barang_1011 >= 3
is_promo_tersedia_1011 = kode_promo_1011 in daftar_promo_1011

# Evaluasi Logika Kombinasi
dapat_diskon_1011 = is_cukup_belanja_1011 or is_cukup_barang_1011
dapat_promo_1011 = is_promo_tersedia_1011

# 3. KALKULASI ARITMATIKA & AUGMENTED ASSIGNMENT
persen_diskon_1011 = 0.05
potongan_harga_1011 = total_belanja_1011 * persen_diskon_1011

# Menggunakan operator penugasan (-=) untuk total bayar
total_pembayaran_1011 = float(total_belanja_1011)
total_pembayaran_1011 -= potongan_harga_1011

rata_rata_harga_1011 = total_pembayaran_1011 / jumlah_barang_1011

# 4. OPERASI BITWISE
# Pembuatan Mask Bitwise
BIT_MEMBER_1011 = 1 if is_member_1011 else 0
BIT_BELANJA_1011 = 2 if is_cukup_belanja_1011 else 0
BIT_BARANG_1011 = 4 if is_cukup_barang_1011 else 0
BIT_PROMO_1011 = 8 if is_promo_tersedia_1011 else 0

# Menggabungkan Flag Status dengan Bitwise OR (|)
kode_transaksi_1011 = BIT_MEMBER_1011 | BIT_BELANJA_1011 | BIT_BARANG_1011 | BIT_PROMO_1011
kode_referensi_1011 = BIT_MEMBER_1011 | BIT_BELANJA_1011 | BIT_PROMO_1011

# Operasi Bitwise Spesifik
cek_member_1011 = kode_transaksi_1011 & 0b0001
cek_promo_1011 = kode_transaksi_1011 & 0b1000
hasil_xor_1011 = kode_transaksi_1011 ^ kode_referensi_1011
hasil_shift_1011 = kode_transaksi_1011 << 1

# ==============================================================================
# CETAK OUTPUT TRANSAKSI
# ==============================================================================

print("\n=== DATA TRANSAKSI ===")
print(f"Nama Pelanggan       : {nama_1011}")
print(f"Status Pelanggan     : {status_1011}")
print(f"Total Belanja        : Rp{total_belanja_1011}")
print(f"Jumlah Barang        : {jumlah_barang_1011}")
print(f"Kode Promo           : {kode_promo_1011}")

print("\n=== HASIL VALIDASI ===")
print(f"Belanja >= Rp200000        : {is_cukup_belanja_1011}")
print(f"Jumlah Barang >= 3         : {is_cukup_barang_1011}")
print(f"Status Member              : {is_member_1011}")
print(f"Kode Promo Tersedia        : {is_promo_tersedia_1011}")
print(f"Mendapatkan Diskon         : {dapat_diskon_1011}")
print(f"Mendapatkan Promo          : {dapat_promo_1011}")

print("\n=== HASIL PERHITUNGAN ===")
print(f"Diskon                      : Rp{potongan_harga_1011:.1f}")
print(f"Total Pembayaran            : Rp{total_pembayaran_1011:.1f}")
print(f"Rata-rata Harga Barang      : Rp{rata_rata_harga_1011:.1f}")

print("\n=== HAK AKSES PELANGGAN ===")
print(f"Kode Hak Akses              : {bin(kode_transaksi_1011)[2:].zfill(4)}")
print(f"Member Access               : {is_member_1011}")
print(f"Promo Access                : {is_promo_tersedia_1011}")
print(f"Free Shipping Access        : {kode_promo_1011 == 'SABTUMAJU'}")

print("\n=== OPERASI BITWISE ===")
print("=== Kode Status Transaksi ===")
print(f"{BIT_MEMBER_1011:04b} | {BIT_BELANJA_1011:04b} | {BIT_BARANG_1011:04b} | {BIT_PROMO_1011:04b}")
print(f"Kode Biner   : {kode_transaksi_1011:04b}")
print(f"Kode Desimal : {kode_transaksi_1011}")

print("\n=== Pemeriksaan Status ===")
print("Cek Member")
print(f"{kode_transaksi_1011:04b} & 0001")
print(f"Hasil Biner   : {cek_member_1011:04b}")
print(f"Hasil Desimal : {cek_member_1011}")

print("\nCek Promo")
print(f"{kode_transaksi_1011:04b} & 1000")
print(f"Hasil Biner   : {cek_promo_1011:04b}")
print(f"Hasil Desimal : {cek_promo_1011}")

print("\n=== Perbandingan Status ===")
print(f"Kode Transaksi : {kode_transaksi_1011:04b}")
print(f"Kode Referensi : {kode_referensi_1011:04b}")
print(f"{kode_transaksi_1011:04b} ^ {kode_referensi_1011:04b}")
print(f"Hasil Biner   : {hasil_xor_1011:04b}")
print(f"Hasil Desimal : {hasil_xor_1011}")

print("\n=== Shift ===")
print(f"{kode_transaksi_1011:04b} << 1")
print(f"Hasil Biner   : {hasil_shift_1011:05b}")
print(f"Hasil Desimal : {hasil_shift_1011}")

print("=== SELESAI ===")