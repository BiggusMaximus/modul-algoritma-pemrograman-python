import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-2*np.pi, 2*np.pi, 200)
plt.axvline(x=0, color='k')
plt.axhline(y=0, color='k')
plt.xlabel('Time (s)')
plt.ylabel('f(t)')

sum = 0
amplitudo = int(input("Masukkan nilai amplitudo: "))
periode = int(input("Masukkan nilai T : "))
n = int(input("Masukkan banyaknya  aproksimasi : "))

for angka in range(1, n):
    sum = sum + ((amplitudo/np.pi) * np.sin(angka*(2*np.pi/periode)*t))/angka
    plt.plot(t, sum)
