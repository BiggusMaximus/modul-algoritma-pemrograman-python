import numpy as np
import matplotlib.pyplot as plt
ax = plt.axes(projection='3d')
xn = np.linspace(-50, 50, 100)
yn = np.linspace(-50, 50, 100)
X, Y = np.meshgrid(xn, yn)
ax.set_xlabel("Sumbu-X")
ax.set_ylabel("Sumbu-Y")
ax.set_zlabel("Sumbu-Z")
ax.set_title("Z = f(x,y) = x^2 + y^2")
Z = X**2 + Y**2
ax.plot_surface(X, Y, Z, cmap="jet")
plt.show()
