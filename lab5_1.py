'''
EE363 - Lab 5: Fourier Transform of an Energy Signal

Purpose:
To analyze the Fourier Transform of a Gaussian-shaped energy signal numerically,
without using built-in FFT functions.

Procedure:
1. Define and plot the time-domain waveform.
2. Implement numerical integration to compute its Fourier Transform.
3. Plot the magnitude and phase spectra.
4. Compute and plot the Energy Spectrum Density.

Author: Nathnael Minuta
Student ID: 15778991
Date: 02/18/2025
'''

import numpy as np
import matplotlib.pyplot as plt

# Fourier Transform function using numerical integration
def fourier_transform(signal, t, f):
    dt = t[1] - t[0]  # Time step
    X_f = np.array([np.sum(signal * np.exp(-1j * 2.0 * np.pi * freq * t)) * dt for freq in f])
    return X_f

# Define constants
T = 0.1e-3  # Sampling period (0.1 ms)
t = np.linspace(0, 10*T, 1000)  # Time range from 0 to 10T

# Define the energy signal x(t) = exp(-((t - 5T) / T)^2)
def energy_signal(t, T):
    return np.exp(-((t - 5*T) / T) ** 2)

# Compute the time-domain signal
x_t = energy_signal(t, T)

# Plot time-domain waveform
plt.figure(figsize=(8, 4))
plt.plot(t * 1e3, x_t, label=r'$x(t) = e^{-((t-5T)/T)^2}$')
plt.xlabel("Time (ms)")
plt.ylabel("Amplitude")
plt.title("Time-Domain Signal")
plt.legend()
plt.grid()
plt.show()

# Define frequency range for Fourier Transform
f = np.linspace(-5000, 5000, 1000)  # Frequency range from -5000Hz to 5000Hz

# Compute Fourier Transform
X_f = fourier_transform(x_t, t, f)

# Plot Fourier Transform Magnitude Spectrum
plt.figure(figsize=(8, 4))
plt.plot(f, np.abs(X_f), label=r'$|X(f)|$')
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("Fourier Transform - Magnitude Spectrum")
plt.legend()
plt.grid()
plt.show()

# Plot Fourier Transform Phase Spectrum
plt.figure(figsize=(8, 4))
plt.plot(f, np.angle(X_f), label=r'$\angle X(f)$')
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (radians)")
plt.title("Fourier Transform - Phase Spectrum")
plt.legend()
plt.grid()
plt.show()

# Compute and plot Energy Spectrum Density (|X(f)|^2)
S_f = np.abs(X_f) ** 2
plt.figure(figsize=(8, 4))
plt.plot(f, S_f, label=r'$|X(f)|^2$')
plt.xlabel("Frequency (Hz)")
plt.ylabel("Energy Density")
plt.title("Energy Spectrum Density")
plt.legend()
plt.grid()
plt.show()
