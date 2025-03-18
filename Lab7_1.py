'''
EE363 - Lab 7: USB & LSB SSB Modulation

Purpose:
To perform USB-SSB and LSB-SSB modulation on a given baseband signal and analyze its spectral properties.

Procedure:
1. Define the baseband signal m(t) using the given mathematical expression.
2. Compute and plot the baseband signal.
3. Compute and plot the baseband spectrum using the Fourier Transform.
4. Compute the Hilbert transform using IDFT.
5. Generate the USB-SSB and LSB-SSB modulated signals.
6. Compute and plot the spectra of the USB-SSB and LSB-SSB signals.

Author: Nathnael Minuta
Student ID: 15778991
Date: 03/04/2025
'''

import numpy as np
import matplotlib.pyplot as plt

# Define parameters
T = 0.01  # Given in problem statement
fc = 500  # Carrier frequency in Hz
fs = 1 / (T/100)  # Sampling frequency
t = np.arange(0, 10*T, T/100)  # Time vector

# Define the baseband signal m(t)
m_t = (t - 5*T) * np.exp(-((t - 5*T)/T)**2)
m_t *= (t >= 0) & (t < 10*T)  # Apply unit step function constraints

# Compute Fourier Transform of m(t)
M_f = np.fft.fft(m_t)
freqs = np.fft.fftfreq(len(t), d=T/100)

# Apply Hilbert transform in the frequency domain
H = np.zeros_like(M_f, dtype=complex)
H[freqs > 0] = -1j  # -90 degree shift for positive frequencies
H[freqs < 0] = 1j   # +90 degree shift for negative frequencies

hilbert_spectrum = M_f * H
hilbert_signal = np.fft.ifft(hilbert_spectrum).real  # Inverse FFT to get time-domain Hilbert signal

# Compute USB-SSB and LSB-SSB signals
s_usb = m_t * np.cos(2 * np.pi * fc * t) - hilbert_signal * np.sin(2 * np.pi * fc * t)
s_lsb = m_t * np.cos(2 * np.pi * fc * t) + hilbert_signal * np.sin(2 * np.pi * fc * t)

# Compute spectrum of USB-SSB and LSB-SSB
S_usb_f = np.fft.fft(s_usb)
S_lsb_f = np.fft.fft(s_lsb)

# Plot everything on a single figure with 4 subplots
plt.figure(figsize=(12, 10))

plt.subplot(2, 2, 1)
plt.plot(t, m_t, label="Baseband Signal m(t)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Baseband Signal")
plt.legend()
plt.grid()

plt.subplot(2, 2, 2)
plt.plot(t, hilbert_signal, label="Hilbert Signal m̂(t)", linestyle="dashed")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Hilbert Transform")
plt.legend()
plt.grid()

plt.subplot(2, 2, 3)
plt.plot(t, s_usb, label="USB-SSB Signal", linestyle="dotted")
plt.plot(t, s_lsb, label="LSB-SSB Signal", linestyle="dashdot")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("USB-SSB and LSB-SSB Signals")
plt.legend()
plt.grid()

plt.subplot(2, 2, 4)
plt.plot(np.fft.fftshift(freqs), np.abs(np.fft.fftshift(M_f)), label="Baseband Spectrum")
plt.plot(np.fft.fftshift(freqs), np.abs(np.fft.fftshift(S_usb_f)), label="USB-SSB Spectrum", linestyle="dashed")
plt.plot(np.fft.fftshift(freqs), np.abs(np.fft.fftshift(S_lsb_f)), label="LSB-SSB Spectrum", linestyle="dotted")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("Frequency-Domain Spectra")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
