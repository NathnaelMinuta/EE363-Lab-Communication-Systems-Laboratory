'''
EE363 - Lab 6: Synchronous Detection of DSB-SC Signals

Purpose:
To implement and analyze the process of demodulating a Double Sideband Suppressed Carrier (DSB-SC) 
signal using synchronous detection. The experiment demonstrates signal modulation, mixing, spectral analysis, 
low-pass filtering, and baseband signal recovery.

Procedure:
1. Generate the baseband signal using the given function.
2. Modulate the baseband signal using a cosine carrier to create the DSB-SC signal.
3. Multiply the received signal with the same carrier signal to perform synchronous detection.
4. Compute the frequency spectrum of the mixed signal using Fourier Transform.
5. Apply a low-pass filter to extract the baseband signal.
6. Perform the inverse Fourier Transform to recover the time-domain baseband signal.
7. Plot and analyze all signals and spectra.

Author: Nathnael Minuta
Student ID: 15778991
Date: 02/25/2025
'''

import numpy as np
import matplotlib.pyplot as plt

# Define parameters
T = 0.01  # Given in the problem
Fs = 10000  # Sampling frequency (10 kHz for better resolution)
t = np.arange(0, 10.0 * T, T / 100.0)  # Time array
fc = 500  # Carrier frequency in Hz (1000π rad/s)


# Define unit step function u(t)
def u(t):
    return np.heaviside(t, 1)

# Define the baseband signal
baseband_signal = (t - 5 * T) * np.exp(-((t - 5 * T) ** 2) / T) * (u(t) - u(t - 10 * T))

# Define the carrier signal
carrier_signal = np.cos(1000 * np.pi * t)  # cos(1000πt)

# Step 2: Modulate the baseband signal to get x(t) (DSB-SC signal)
x_t = baseband_signal * carrier_signal

# Step 3: Multiply x(t) with 2cos(1000πt) to obtain y(t) (Mixed signal)
y_t = 2 * x_t * carrier_signal

# Compute Fourier Transform
def compute_spectrum(signal, Fs):
    N = len(signal)
    freq = np.fft.fftfreq(N, d=1/Fs)
    spectrum = np.fft.fft(signal)
    return freq, np.abs(spectrum)

# Get spectrum of y(t)
freq, spectrum_y = compute_spectrum(y_t, Fs)

# Step 5: Apply Low-Pass Filter (Ideal LPF)
LPF_array = np.where(np.abs(freq) > fc, 0, 1)
filtered_spectrum = spectrum_y * LPF_array

# Step 6: Inverse Fourier Transform to recover baseband signal
recovered_signal = np.fft.ifft(filtered_spectrum).real

# Plot results
plt.figure(figsize=(12, 8))

plt.subplot(3, 2, 1)
plt.plot(t, baseband_signal)
plt.title("Baseband Signal")

plt.subplot(3, 2, 2)
plt.plot(t, x_t)
plt.title("DSB-SC Modulated Signal x(t)")

plt.subplot(3, 2, 3)
plt.plot(t, y_t)
plt.title("Mixed Signal y(t)")

plt.subplot(3, 2, 4)
plt.plot(freq, spectrum_y)
plt.title("Spectrum of y(t)")

plt.subplot(3, 2, 5)
plt.plot(t, recovered_signal)
plt.title("Recovered Baseband Signal")

plt.tight_layout()
plt.show()