from scipy import integrate
import numpy as np

fs = 1000 # Sampling frequency for the plotting
delta = lambda t: np.array([fs/10 if 0 < t_ and t_ < 1/(fs/10) else 0.0 for t_ in t])

y = integrate.simps(delta(t), t)
print(y)