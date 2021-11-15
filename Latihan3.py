print("PROGRAM DENGAN PERULANGAN BERTINGKAT (NESTED) FOR")

#variable

baris = 10
kolom = baris

#hasil inputan variable

for bar in range(baris):
    for col in range(kolom):
        tab = bar+col
        print("{0:>5}".format(tab), end='')
    print()