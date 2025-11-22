import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. BASIC PLOTTING


x = np.linspace(-10, 10, 400)
y = x**2 - 4*x + 4

plt.figure()
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Plot of f(x) = x^2 - 4x + 4")
plt.grid(True)
plt.show()



# 2. SINE AND COSINE PLOT


x = np.linspace(0, 2*np.pi, 400)

plt.figure()
plt.plot(x, np.sin(x), linestyle='--', marker='o', label='sin(x)')
plt.plot(x, np.cos(x), linestyle='-', marker='s', label='cos(x)')
plt.xlabel("x")
plt.ylabel("Value")
plt.title("Sine and Cosine")
plt.legend()
plt.grid(True)
plt.show()



# 3. SUBPLOTS 2×2

x = np.linspace(0, 10, 400)
x_log = np.linspace(0, 10, 400)

fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(x, x**3)
axs[0, 0].set_title("f(x) = x^3")

axs[0, 1].plot(x, np.sin(x))
axs[0, 1].set_title("f(x) = sin(x)")

axs[1, 0].plot(x, np.exp(x))
axs[1, 0].set_title("f(x) = e^x")

axs[1, 1].plot(x_log, np.log(x_log + 1))
axs[1, 1].set_title("f(x) = log(x + 1)")

plt.tight_layout()
plt.show()



# 4. SCATTER PLOT (100 random points)


x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)

plt.figure()
plt.scatter(x, y, marker='o')
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Random Scatter Plot")
plt.grid(True)
plt.show()


# 5. HISTOGRAM (1000 normal samples)


data = np.random.normal(0, 1, 1000)

plt.figure()
plt.hist(data, bins=30, alpha=0.7)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of Normal Distribution")
plt.grid(True)
plt.show()



# 6 3D SURFACE PLOT


x = np.linspace(-5, 5, 200)
y = np.linspace(-5, 5, 200)
X, Y = np.meshgrid(x, y)
Z = np.cos(X**2 + Y**2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis')
plt.title("3D Surface Plot of f(x,y) = cos(x² + y²)")
fig.colorbar(surf)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()



