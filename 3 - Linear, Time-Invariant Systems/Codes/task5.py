import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 1, 2, 0])
h = np.array([0, 0, 0, 3, 1, 0, 0])
hr = np.flip(h)
xo = 2
ho = 4
y = np.zeros(len(x) + len(h) - 1)
for n in range(len(y)):
    xkmin = max(0, n - len(h) + 1)
    xkmax = min(len(x), n + 1)
    hkmin = max(0, len(h) - n - 1)
    hkmax = min(len(h), len(x) + len(h) - n - 1)
    y[n] = np.sum(x[xkmin:xkmax] * hr[hkmin:hkmax])
    print("y[{0}] = x[{1}:{2}]*h[{3}:{4}] = {5}".format(n, xkmin, xkmax, hkmin, hkmax, y[n]))
n = np.arange(-5, 6, 1)
fig, ax = plt.subplots(figsize=(8, 3))
ax.stem(n, y)
plt.xlim(-5, 5)
plt.show()