import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-100, 100, 100)
y1 = 69*(x**2) + 69*x + 69
sum = 0
for n in range(0, 3 + 1):
    sum = sum + np.sin((69 + n)*x) + np.cos((69 + n)*x)


fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(x, y1)
ax2.plot(x, sum)
plt.show()
