tinggi_1011 = int(input("masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_1011 %2 != 0:
    print("tinggi harus bilangan genap")
else:
    a_1011 = tinggi_1011
    c_1011 = a_1011
    lebar_1011 = (2*tinggi_1011) - 2

    for i_1011 in range(1, tinggi_1011 +1):
        b_1011 = c_1011 + 1

        for j_1011 in range(1, lebar_1011 + 1):

            #baris atas dan bawah
            if i_1011 == 1 or i_1011 == tinggi_1011:
                if j_1011 ==1 or j_1011 == lebar_1011:
                    print("#", end="")
                else:
                    print("=", end="")
            #baris isi
            else:
                if j_1011 == 1 or j_1011 == lebar_1011:
                    print("|", end="")
                else:
                    if j_1011 == c_1011:
                        print("<", end="")
                    elif j_1011 == b_1011:
                        print(">", end="")
                    elif j_1011 == (lebar_1011 - c_1011):
                        print("<", end="")
                    elif j_1011 == (lebar_1011 - c_1011 + 1):
                        print(">", end="")
                    elif j_1011>b_1011 and j_1011<(lebar_1011 - c_1011):
                        print(".", end="")
                    else:
                        print(" ", end="")
        print()

        #logika asli java
        a_1011 -= 2

        if a_1011 <= 0:
            c_1011 = (-a_1011) + 2
        else:
            c_1011 = a_1011