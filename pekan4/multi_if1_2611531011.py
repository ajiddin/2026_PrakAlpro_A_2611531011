# program ini menggunakan fungsi input ()

umur_1011 = int(input("Masukkan umur Anda: "))
sim_1011 = input("Apakah Anda sudah punya SIM C ? (y/t): ")[0]

if umur_1011 >= 17 and sim_1011 == "y" :
    print("Anda sudah dewasa dan boleh membawa motor")

if umur_1011 >= 17 and sim_1011 != "y" :
    print("Anda sudah dewasa tetapi belum boleh membawa motor")

if umur_1011 < 17 and sim_1011 != "y" :
    print("anda belum cukup umur bawa motor")

if umur_1011 < 17 and sim_1011 == "y" :
    print("anda belum cukup umur punya sim")
    