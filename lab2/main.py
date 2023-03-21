import numpy as np
import matplotlib.pyplot as plt


def func(x, n):
    arr = []
    for i in range(n):
        arr.append(pow((x[i]-1), 2))
    return arr


x = np.linspace(0, 1, 10)
y = func(x, 10)

x1 = np.linspace(0, 1, 10)
y1 = np.interp(x1, x, y)
plt.plot(x, y, "o", x1, y1, "-")
plt.grid()
plt.show()
