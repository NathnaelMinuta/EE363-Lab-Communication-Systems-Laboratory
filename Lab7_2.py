import numpy as np

import matplotlib.pyplot as plt
 
# Define parameters

T = 0.01  # Given time period

fs = 50000  # Sampling frequency

t = np.arange(0, 10*T, 1/fs)  # Time vector

f_c = 500  # Carrier frequency in Hz

w_c = 2 * np.pi * f_c
 
# Define the baseband signal m(t)

def unit_step(t):

    return np.where(t >= 0, 1, 0)
 
baseband = (t - 5*T) * np.exp(-((t - 5*T) / T) ** 2) * (unit_step(t) - unit_step(t - 10*T))
 
# Compute the Hilbert transform using FFT method

spectrum_baseband = np.fft.fft(baseband)

freqs = np.fft.fftfreq(len(baseband), 1/fs)
 
# Create the Hilbert transform filter

H = np.zeros_like(spectrum_baseband, dtype=complex)

H[freqs > 0] = 2  # Apply Hilbert filter

H[freqs < 0] = 0
 
hilbert_spectrum = spectrum_baseband * H

hilbert_signal = np.fft.ifft(hilbert_spectrum).real  # Inverse FFT to get time-domain Hilbert signal
 
# Plot the Hilbert transform signal

plt.figure()

plt.plot(t, hilbert_signal, label="Hilbert Signal m̂(t)")

plt.xlabel("Time (s)")

plt.ylabel("Amplitude")

plt.title("Hilbert Transform of Baseband Signal")

plt.legend()

plt.grid()

plt.show()
 
# Generate the SSB-USB signal

ssb_usb = baseband * np.cos(w_c * t) - hilbert_signal * np.sin(w_c * t)
 
# Plot the SSB-USB signal

plt.figure()

plt.plot(t, ssb_usb, label="SSB-USB Signal")

plt.xlabel("Time (s)")

plt.ylabel("Amplitude")

plt.title("Single Sideband Upper Sideband (SSB-USB) Signal")

plt.legend()

plt.grid()

plt.show()
 
# Compute the spectrum of SSB-USB

spectrum_ssb_usb = np.fft.fft(ssb_usb)
 
# Plot the spectrum of SSB-USB

plt.figure()

plt.plot(freqs, np.abs(spectrum_ssb_usb), label="Spectrum of SSB-USB")

plt.xlabel("Frequency (Hz)")

plt.ylabel("Magnitude")

plt.title("Spectrum of SSB-USB Signal")

plt.legend()

plt.grid()

plt.xlim(-2000, 2000)

plt.show()
 
# Generate the SSB-LSB signal

ssb_lsb = baseband * np.cos(w_c * t) + hilbert_signal * np.sin(w_c * t)
 
# Plot the SSB-LSB signal

plt.figure()

plt.plot(t, ssb_lsb, label="SSB-LSB Signal")

plt.xlabel("Time (s)")

plt.ylabel("Amplitude")

plt.title("Single Sideband Lower Sideband (SSB-LSB) Signal")

plt.legend()

plt.grid()

plt.show()
 
# Compute the spectrum of SSB-LSB

spectrum_ssb_lsb = np.fft.fft(ssb_lsb)
 
# Plot the spectrum of SSB-LSB

plt.figure()

plt.plot(freqs, np.abs(spectrum_ssb_lsb), label="Spectrum of SSB-LSB")

plt.xlabel("Frequency (Hz)")

plt.ylabel("Magnitude")

plt.title("Spectrum of SSB-LSB Signal")

plt.legend()

plt.grid()

plt.xlim(-2000, 2000)

plt.show()