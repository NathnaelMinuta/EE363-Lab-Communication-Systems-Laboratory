import numpy as np
import matplotlib.pyplot as plt

# Define parameters
T = 0.01  # Given in the problem
Fs = 10000  # Sampling frequency (10 kHz for better resolution)
t = np.arange(0, 10.0 * T, T / 100.0)  # Time array
fc = 500  # Carrier frequency in Hz (1000π rad/s)

# Fourier Transform function
def fourier_transform(signal, t, f):
    dt = t[1] - t[0]  # Time step
    X_f = np.array([np.sum(signal * np.exp(-1j * 2.0 * np.pi * freq * t)) * dt for freq in f])
    return X_f

# Define unit step function u(t)
def u(t):
    return np.heaviside(t, 1)

# Define the baseband signal
baseband_signal = (t - 5 * T) * np.exp(-((t - 5 * T) ** 2) / T) * (u(t) - u(t - 10 * T))

# Define the carrier signal
carrier_signal = np.cos(1000 * np.pi * t)  # cos(1000πt)

# Step 2: Modulate the baseband signal to get x(t) (DSB-SC signal)
x_t_modulated = baseband_signal * carrier_signal

# Step 3: Multiply x(t) with 2cos(1000πt) to obtain y(t) (Mixed signal)
y_t = 2 * x_t_modulated * carrier_signal

# Define the baseband signal function (energy signal)
def baseband_signal_1(t, T):
    return (t - 5 * T) * np.exp(-((t - 5 * T) ** 2) / T) * (u(t) - u(t - 10 * T))

# Compute the time-domain signal
x_t_baseband = baseband_signal_1(t, T)

# Define frequency range for Fourier Transform
f = np.linspace(-750, 750, 1500)  # Generate 1500 frequency points

# Compute Fourier Transform of baseband signal
X_f = fourier_transform(x_t_baseband, t, f)

# Plot time-domain waveform
plt.figure(figsize=(8, 4))
plt.plot(t * 1e3, x_t_baseband, label=r'Baseband Signal x(t)')
plt.xlabel("Time (ms)")
plt.ylabel("Amplitude")
plt.title("Time-Domain Baseband Signal")
plt.legend()
plt.grid()
plt.show()

# Compute Fourier Transform of Modulated Signal
X_f_modulated = fourier_transform(x_t_modulated, t, f)

# Plot Fourier Transform Magnitude Spectrum
plt.figure(figsize=(8, 4))
plt.plot(f, np.abs(X_f_modulated), label=r'$|X(f)|$')
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("Fourier Transform - Magnitude Spectrum of Modulated Signal")
plt.legend()
plt.grid()
plt.show()
