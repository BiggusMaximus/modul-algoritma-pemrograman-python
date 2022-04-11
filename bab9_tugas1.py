# Program Membuat nilai himpunan Y dengan
# Memetakan nilai x pada interval [1,10] ke dalam fungsi Y(X) = (x^3) + 1

# Membuat list kosong berisi himpunan 1-10
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Membuat list kosong dari Y
y = []

# Melakukan iterasi terhadap list pada nilai X
for nilai_x in x:
  # Memasukkan persamaan fungsi
  # Memasukkan nilai ke dalam list Y
  y.append(nilai_x*nilai_x*nilai_x + 1)

print(f"Himpunan nilai Y(X) = (x^3) + 1 adalah : {y} ")
