from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt

fs = 1000  # Sampling frequency for the plotting
T = 5  # Time range
t = np.arange(-T, T, 1 / fs)  # Time samples
delta = lambda t: np.array([fs / 10 if 0 < t_ and t_ < 1 / (fs / 10) else 0.0 for t_ in t])

# Task 3
h = lambda t: delta(t + 2) + delta(t - 1)
x = lambda t: (t > 0) * np.exp(- 2 * t)  # a = -2
fs = 1000  # Sampling frequency for the plotting
T = 5  # Time range
t = np.arange(-T, T, 1 / fs)  # Time samples

# Computing the convolution using integration
y = np.zeros(len(t))
for n, t_ in enumerate(t):
    product = lambda tau: x(tau) * h(t_ - tau)
    y[n] = integrate.simps(product(t), t)  # Actual convolution at time t

# Task 4
plt.plot(t, y, label=r'$x(t)\ast h(t)$')  # Plotting the output y
plt.xlabel(r'$t$')
plt.legend()
plt.show()