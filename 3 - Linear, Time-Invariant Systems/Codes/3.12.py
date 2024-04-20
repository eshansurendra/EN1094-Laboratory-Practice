import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from matplotlib import image
from scipy import signal

x = mpimg.imread('allenkeys.png')
fig, ax = plt.subplots(1,2)
ax[0].imshow(x, cmap='gray')

filter = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]])

filtered = signal.convolve2d(image, filter)
ax[1].imshow(filtered, cmap='gray')