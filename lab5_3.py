'''
EE363 - Lab 5: Fourier Transform of an Energy Signal

Purpose:
To analyze the Fourier Transform of a Gaussian-shaped energy signal and its scaled version 
numerically, without using built-in FFT functions.

Procedure:
1. Define and plot the time-domain waveform for x(t) and x(2t).
2. Implement numerical integration to compute their Fourier Transforms.
3. Plot the magnitude and phase spectra for both signals.
4. Compute and plot the Energy Spectrum Density.
5. Compare the original and scaled signals in the frequency domain.

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

# Compute the original and scaled signals
x_t = energy_signal(t, T)        # Original signal
x_scaled = energy_signal(2*t, T)  # Scaled signal x(2t)

# Plot original time-domain waveform
plt.figure(figsize=(8, 4))
plt.plot(t * 1e3, x_t, label=r'$x(t) = e^{-((t-5T)/T)^2}$')
plt.xlabel("Time (ms)")
plt.ylabel("Amplitude")
plt.title("Time-Domain Signal X(t)")
plt.legend()
plt.grid()
plt.show()

# Plot scaled time-domain waveform
plt.figure(figsize=(8, 4))
plt.plot(t * 1e3, x_scaled, label=r'$x(2t)$', linestyle="dashed")
plt.xlabel("Time (ms)")
plt.ylabel("Amplitude")
plt.title("Time-Domain Signal X(2t)")
plt.legend()
plt.grid()
plt.show()

# Define frequency range for Fourier Transform
f = np.linspace(-5000, 5000, 1000)  # Frequency range from -5000Hz to 5000Hz

# Compute Fourier Transforms
X_f = fourier_transform(x_t, t, f)        # Original
X_f_scaled = fourier_transform(x_scaled, t, f)  # Scaled

# Plot Fourier Transform Magnitude Spectrum (Original vs Scaled)
plt.figure(figsize=(8, 4))
plt.plot(f, np.abs(X_f), label="Original Spectrum")
plt.plot(f, np.abs(X_f_scaled), label="Scaled Spectrum (2t)", linestyle="dashed")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("Fourier Transform - Magnitude Spectrum Comparison")
plt.legend()
plt.grid()
plt.show()

# Plot Fourier Transform Phase Spectrum (Original vs Scaled)
plt.figure(figsize=(8, 4))
plt.plot(f, np.angle(X_f), label="Original Phase")
plt.plot(f, np.angle(X_f_scaled), label="Scaled Phase (2t)", linestyle="dashed")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (radians)")
plt.title("Fourier Transform - Phase Spectrum Comparison")
plt.legend()
plt.grid()
plt.show()

# Compute and plot Energy Spectrum Density (|X(f)|^2) for Original and Scaled
S_f = np.abs(X_f) ** 2
S_f_scaled = np.abs(X_f_scaled) ** 2

plt.figure(figsize=(8, 4))
plt.plot(f, S_f, label="Original Energy Spectrum")
plt.plot(f, S_f_scaled, label="Scaled Energy Spectrum (2t)", linestyle="dashed")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Energy Density")
plt.title("Energy Spectrum Density Comparison")
plt.legend()
plt.grid()
plt.show()
