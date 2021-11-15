print("PROGRAM INPUT SEJUMLAH DATA")
print("TAMPILKAN HASIL SECARA BERURUTAN MULAI DARI YANG TERKECIL")

def angka_terbesar (a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c

def angka_terkecil (a, b, c,):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    elif c < a and c < b:
        return c

def nilai_tengah (a,b, c):
    if (b > a > c) or (c > a > b):
        return a
    elif (a > b > c) or (c > b > a):
        return b
    elif (a > c > b) or (b > c > a):
        return c

a, b, c = (
    int(input("BILANGAN A:")),
    int(input("BILANGAN B:")),
    int(input("BILANGAN C:")),
)

i1 = angka_terkecil(a, b, c)
i2 = nilai_tengah(a, b, c)
i3 = angka_terbesar(a, b, c)

print(f"URUTAN BILANGAN: {i1}, {i2}, {i3}")