nilai_1 = int(input("Masukkan nilai pertama :"))
nilai_2 = int(input("Masukkan nilai kedua : "))
nilai_3 = int(input("Masukkan nilai ketiga : "))

if nilai_1 > nilai_2:
    if nilai_1 > nilai_3:
        print("Nilai terbesar adalah nilai-1 ")
    elif nilai_1 < nilai_3:
        print("Nilai terbesar adalah nilai-3 ")
    else:
        print("Nilai-1 sama besarnya dengan nilai-3 ")
elif nilai_1 < nilai_2:
    if nilai_2 > nilai_3:
        print("Nilai terbesar adalah nilai-2 ")
    elif nilai_2 < nilai_3:
        print("Nilai terbesar adalah nilai-3 ")
    else:
        print("Nilai-2 sama besarnya dengan nilai-3")
else:
    print("Nilai-1 sama besarnya dengan nilai-2")
