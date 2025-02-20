'''
This is the third lab of EE363.

Purpose:
Compute the autocorrelation function of a continuous-time signal via numerical integration.

Procedure:
1. Generate a time array and signal x(t) = sin(2πft) + 0.5 sin(4πft) using define_signal().
2. Define a range of lag values (τ) for which the autocorrelation will be computed.
3. For each τ, numerically approximate R_x(τ) by interpolating x(t − τ) and summing the product x(t)·
   x(t − τ) over valid time intervals.
4. Plot both the original signal and its autocorrelation function.

Author: Nathnael Minuta
Student ID: 15778991
Date: 02/04/2025
'''

import numpy as np
import matplotlib.pyplot as plt
def define_signal(f=5.0, fs=1000, duration=2.0):
   """
   Generate the time array and signal x(t) = sin(2π f t) + 0.5 sin(4π f t)
   sampled at fs (samples/second) for 'duration' seconds.
   Returns:
       t: time array of shape (N,)
       x: signal array of shape (N,)
       dt: time step
   """
   dt = 1.0 / fs
   t = np.arange(0, duration, dt)
   x = np.sin(2 * np.pi * f * t) + 0.5 * np.sin(4 * np.pi * f * t)
   return t, x, dt

def autocorrelation_numerical(x, t, tau_vals):
   """
   Numerically approximate R_x(τ) = ∫ x(t) x(t - τ) dt
   over the domain where x(t) is defined (t in [0, max_time]).
   Assumes x(t) = 0 outside [0, max_time].
   Inputs:
       x: sampled signal array (length N)
       t: time array for x (same length N)
       tau_vals: array of τ values where we want R_x(τ)
   Returns:
       R: array of R_x(τ), same length as tau_vals
   """
   dt = t[1] - t[0]
   N = len(x)
   t_min, t_max = t[0], t[-1]   # 0 and 2, typically
   R = np.zeros_like(tau_vals)
   for i, tau in enumerate(tau_vals):
       valid_mask = (t - tau >= t_min) & (t - tau <= t_max)
       t_valid = t[valid_mask]
       x_valid = x[valid_mask]
       # We now need x(t - tau). We'll sample it from the x array
       # via interpolation.
       # Make a function for interpolation:
       x_interp = np.interp(t_valid - tau, t, x)
       # Accumulate sum * dt
       R[i] = np.sum(x_valid * x_interp) * dt
   return R

def main():
   # 1. Define the signal x(t)
   f = 5.0        # Hz
   fs = 1000      # sampling rate in Hz
   duration = 2.0 # seconds
   t, x, dt = define_signal(f, fs, duration)
   # 2. Define the lags τ in [-0.5, +0.5] with a step (for plotting)
   tau_vals = np.arange(-0.5, 0.5 + dt, dt)  # step by dt or smaller if you like
   # 3. Compute the autocorrelation R_x(τ)
   R = autocorrelation_numerical(x, t, tau_vals)
   # 4. Plot the results
   plt.figure(figsize=(10,4))
   # (a) Plot the original signal
   plt.subplot(1,2,1)
   plt.plot(t, x, label='x(t)')
   plt.title("Signal x(t)")
   plt.xlabel("Time [s]")
   plt.ylabel("Amplitude")
   plt.grid(True)
   plt.legend()
   # (b) Plot the autocorrelation vs. tau
   plt.subplot(1,2,2)
   plt.plot(tau_vals, R, label=r"$R_x(\tau)$")
   plt.title("Autocorrelation")
   plt.xlabel("Lag $\\tau$ [s]")
   plt.ylabel(r"$R_x(\tau)$")
   plt.grid(True)
   plt.legend()
   plt.tight_layout()
   plt.show()

if __name__ == "__main__":
   main()