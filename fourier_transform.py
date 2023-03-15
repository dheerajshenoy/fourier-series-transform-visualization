import matplotlib.pyplot as plt
import matplotlib as mpl

plt.rcParams['axes.grid'] = True
plt.rcParams['text.usetex'] = True
mpl.rcParams.update({'font.size': 18})

import numpy as np
from numpy import pi
import scipy as sp
from scipy.fft import fft
from scipy.io.wavfile import write



fig, ax = plt.subplots(2, 1)
ax[0].set_title("\\textbf{\\huge{Signal}}")
ax[1].set_title("\\textbf{\\huge{Fourier Transform of the signal}}")


SR = 44100 # Sampling rate
T = 1/SR # Time period

t = np.arange(0, 1, T) # time space

x = 0

# for i in range(100):
#     amp = np.random.randint(100)
#     freq = np.random.randint(10)
#     x += amp * np.sin(2 * pi * freq * t)

# scaled = np.int16(x / np.max(np.abs(x)) * 32767)
# write('test.wav', SR, scaled)

# Waves
f1 = 18.
x += 10 * np.sin(2 * pi * f1 * t)

f2 = 40.
x += 10 * np.sin(2 * pi * f2 * t)

f3 = 6.
x += 0.5 * np.sin(2 * pi * f3 * t)

ax[0].plot(t, x, 'b')
ax[0].set_xlabel("t (sec)")
ax[0].set_ylabel("x(t)")

X = fft(x)
N = len(X)
n = np.arange(N)
T = N/SR
X = 2 * np.abs(X)/SR
freq = n/T
ax[1].set_xlabel('Freq (Hz)')
ax[1].set_ylabel('Amplitude')
ax[1].set_xlim(0, 20)
ax[1].stem(freq, X, 'r', markerfmt="")

plt.tight_layout()

plt.show()
