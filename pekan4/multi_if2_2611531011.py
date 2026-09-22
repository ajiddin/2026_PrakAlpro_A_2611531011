# program ini menggunakan fungsi input()
# program menghitung diskon belanja

# input dari user
total_belanja_1011 = float(input("masukkan total belanja (Rp): "))

# input status member (mengecek apakah user mengetik y atau t)
input_member_1011 = input("apakah anda member (y/t): ").strip().lower()
is_member_1011 = input_member_1011 in ["y", "t"]

# input status kode promo (mengecek apakah user mengetik y atau t)
input_promo_1011 = input("apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_1011 = input_promo_1011 in ["y", "t"]

total_diskon_persen_1011 = 0

#multi if terpisah: setiaap kondisi diperiksa independen
#diskon bisa di tumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus 

if total_belanja_1011 > 1000000:
    total_diskon_persen_1011 += 10 #diskon belanja besar

if is_member_1011:
    total_diskon_persen_1011 += 5 #diskon member

if kode_promo_valid_1011:
    total_diskon_persen_1011 += 15 #diskon voucher

# menghitung nominal diskon dan total bayar
nominal_diskon_1011 = total_belanja_1011 * (total_diskon_persen_1011 / 100)
total_bayar_1011 = total_belanja_1011 - nominal_diskon_1011

# output hasil
print("\n--- rincian pembayaran ---")
print(f"total diskon : {total_diskon_persen_1011}% (Rp {nominal_diskon_1011:,.0f})")
print(f"total bayar : Rp {total_bayar_1011:,.0f}")

print(f"total diskon yang anda dapatkan adalah {total_diskon_persen_1011}%")
# output total diskon yang anda dapat: 30% jika belanja > 1 juta, member, dan kode promo valid