tinggi_1011 = int(input("masukkan tinggi segitiga: "))

for i in range(1, tinggi_1011 + 1):
    print(" " * (tinggi_1011 - i), end="")
    for j in range(1, i + 1):
        print("*", end=" ")
    print()