import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 2*np.pi, np.pi/100)
y1 = np.sin(x)
y2 = np.cos(x + 2*np.pi)
plt.plot(x, y1, '*', label='Sin(x)')
plt.plot(x, y2, '+', label='Sin(x + ℼ	)')
plt.xlabel('Sumbu-X')
plt.ylabel('Sumbu-y')
plt.title('Plot Data')
plt.grid()
plt.legend()
plt.show()
