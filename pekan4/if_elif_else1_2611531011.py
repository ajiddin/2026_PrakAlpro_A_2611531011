umur_1011 = int(input("input umur anda : "))
sim_1011 = input("apakah anda sudah punya sim c: ")[0]

if umur_1011 >= 17 and sim_1011 == "y":
    print("anda sudah dewasa dan boleh bawa motor")
elif umur_1011 >= 17 and sim_1011 != "y":
    print("anda sudah dewasa tapi tidak boleh bawa motor")
elif umur_1011 < 17 and sim_1011 == "y":
    print("anda belum cukup umur punya sim")
else:
    print("anda belum cukup umur dan tidak boleh bawa motor")
print("program selesai")