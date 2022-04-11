# Buat lah suatu fungsi yang dapat membuat fungsi himpunan
# dan Fungsi dari Y(x) = x^2 + 2x + 1
# Isilah garis bawah untuk membuat program bekerja
def buat_himpunan_interval(angka_awal, angka_akhir):
    himpunan = []
    for i in range(angka_awal, angka_akhir + 1):
        himpunan.append(i)
    return himpunan


def hasil_fungsi(himpunan):
    hasil = []
    for i in himpunan:
        hasil.append(i*i + 2*i + 1)
    return hasil


print(
    f"Nilai kuadrat fungsi adalah {hasil_fungsi(buat_himpunan_interval(1,7))}")
