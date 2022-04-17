import numpy as np
# Diketahui v(t) = 50∠30, L = 20.10^(-3), C = 50.10^(-6)
# Masukkan nilai C, L dan f
f = 60
C = 50*10**(-6)
L = 20*10**(-3)
W = 2 * np.pi * f
# Menghitung nilai masing-masing impendansi
ZL = 1j * W * L
ZC = -1j/(W*C)
ZR = 25


def ke_kompleks(amplitudo, sudut):
    # A∠θ = A(cos(θ) + j*sin(θ))
    real = amplitudo * np.cos(sudut * (np.pi/180))
    imajiner = amplitudo * np.sin(sudut * np.pi/180)
    bilangan_kompleks = real + imajiner*1j
    return bilangan_kompleks


def ke_polar(fungsi_kompleks):
    # Amplitudo (A) = akar(real^2 + imajiner^2)
    # Sudut(θ) = tan^(-1)(bilangan_imajiner/bilangan_real)
    amplitudo = np.sqrt(np.real(fungsi_kompleks)**2 +
                        np.imag(fungsi_kompleks)**2)
    sudut = np.angle(fungsi_kompleks, deg=True)
    bilangan_polar = str(round(amplitudo, 2)) + '∠' + str(round(sudut, 2))
    return bilangan_polar


Ztot = ZL + ZC + ZR
v = ke_kompleks(50, 30)

arus = v / Ztot
arus_dalam_polar = ke_polar(arus)
print(f"Nilai arus dalam polar adalah : {arus_dalam_polar}")
