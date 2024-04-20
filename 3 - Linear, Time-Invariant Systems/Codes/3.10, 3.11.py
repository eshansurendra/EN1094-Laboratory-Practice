import numpy as np
from scipy import signal

image = np.array([[0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0]])

filter = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

output = signal.convolve2d(image, filter)
print(output)