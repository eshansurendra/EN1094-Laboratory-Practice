from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 0, 0, 1, 1, 2, 0, 0, 0])
h = np.array([0, 0, 0, 0, 1, 2, 0, 0, 0])

fig, ax = plt.subplots(3, 1, figsize=(12, 12))

y = signal.convolve(x, h, 'full')
ax[0].stem(y)

y = signal.convolve(x, h, 'valid')
ax[1].stem(y)

y = signal.convolve(x, h, 'same')
ax[2].stem(y)

plt.show()