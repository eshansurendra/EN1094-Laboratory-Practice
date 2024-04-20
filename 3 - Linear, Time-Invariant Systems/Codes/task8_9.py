from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

data, samplerate = sf.read('audio_file.wav')

nyquist = samplerate // 2
fc = 2000 / nyquist
n = 121
b = signal.firwin(n, fc, pass_zero=True)
w, h = signal.freqz(b)

fig, ax1 = plt.subplots()
ax1.set_title('Digital filter frequency response')
ax1.plot(w, 20 * np.log10(abs(h)), 'b')
ax1.set_ylabel('Amplitude [dB]', color='b')
ax1.set_xlabel('Frequency [rad/sample]')
ax2 = ax1.twinx()
angles = np.unwrap(np.angle(h))
ax2.plot(w, angles, 'g')
ax2.set_ylabel('Angle (radians)', color='g')
ax2.grid()
ax2.axis('tight')
plt.show()

# Your code here for convolution
ch1 = []
ch2 = []
for i in range(len(data)):
     ch1.append(data[i][0])
     ch2.append(data[i][1])
# print(ch1)
# print(ch2)
y = signal.convolve(ch1, ch2)

fig, ax = plt.subplots(2, 1)
ax[0].plot(data)
ax[1].plot(y)

sf.write('audio_file_filtered.wav', np.vstack((ch1, ch2)).T + data, samplerate)

plt.show()