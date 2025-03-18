'''
EE363 - Lab 8: Frequency Modulation Analysis

Purpose:
To analyze the energy spectrum of a given message signal, generate an FM signal for different modulation indices, and examine its frequency spectrum.

Procedure:
1. Define the baseband message signal (m(t)) as given.
2. Compute and plot the energy spectrum density (ESD) using the Fourier Transform.
3. Calculate the frequency deviation and frequency sensitivity (k_f) for modulation indices of 0.5 and 1.
4. Set the carrier frequency as 5 times the frequency deviation and generate the FM signal.
5. Plot the time-domain representation of the FM signal.
6. Compute and plot the spectrum of the FM signal using the Fourier Transform.
7. Repeat steps 4-6 using a modulation index of 1.

Author: Nathnael Minuta
Student ID: 15778991
Date: 03/18/2025
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq

# Define parameters
T = 10e-3  # 10 ms
fs = 10 * (1/T)  # Sampling frequency
N = 2048  # Number of samples
t = np.linspace(0, 2*T, N)  # Time vector
m_t = (t - 5*T) * np.exp(-((t - 5*T) / T) ** 2)  # Message signal

# Compute and plot Energy Spectrum Density (Fourier Transform)
M_f = fft(m_t)
freqs = fftfreq(N, d=1/fs)
ESD = np.abs(M_f) ** 2

plt.figure()
plt.plot(freqs[:N // 2], ESD[:N // 2])
plt.xlabel("Frequency (Hz)")
plt.ylabel("Energy Spectrum Density")
plt.title("Energy Spectrum Density of m(t)")
plt.grid()
plt.show()

# Frequency deviation and k_f calculations
modulation_indices = [0.5, 1]
delta_f_list = []
kf_list = []
for beta in modulation_indices:
    delta_f = beta / T  # Frequency deviation
    kf = delta_f / np.max(np.abs(m_t))  # k_f calculation
    delta_f_list.append(delta_f)
    kf_list.append(kf)

# FM signal generation and plotting for each modulation index
fc = 5 * delta_f_list[0]  # Carrier frequency
Ac = 1  # Carrier amplitude
dt = t[1] - t[0]  # Time step

for i, beta in enumerate(modulation_indices):
    kf = kf_list[i]
    phase = 2 * np.pi * fc * t + 2 * np.pi * kf * np.cumsum(m_t) * dt
    s_t = Ac * np.cos(phase)
    
    plt.figure()
    plt.plot(t, s_t)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title(f"FM Signal (Modulation Index: {beta})")
    plt.grid()
    plt.show()

    # Compute and plot FM spectrum
    S_f = fft(s_t)
    FM_spectrum = np.abs(S_f) ** 2
    
    plt.figure()
    plt.plot(freqs[:N // 2], FM_spectrum[:N // 2])
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Power Spectrum Density")
    plt.title(f"FM Spectrum (Modulation Index: {beta})")
    plt.grid()
    plt.show()