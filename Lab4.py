'''
This is the Fourth Lab of EE363.

Purpose:
To simulate and analyze the Bit Error Rate (BER) performance of Binary Phase-Shift Keying (BPSK) 
over an Additive White Gaussian Noise (AWGN) channel. The simulation will compare theoretical and 
simulated BER curves as a function of Signal-to-Noise Ratio (SNR).

Procedure:
1. Generate a sequence of random binary bits.
2. Modulate the bits using BPSK (mapping 0 → -1 and 1 → +1).
3. Add AWGN noise to the modulated signal for varying SNR levels.
4. Demodulate the received signal and determine bit errors.
5. Compute and plot the simulated BER vs. theoretical BER.

Author: Nathnael Minuta
Student ID: 15778991
Date: 02/11/2025
'''

import numpy as np
import matplotlib.pyplot as plt
 
def simulate_bpsk_awgn(num_bits=100000, snr_range=np.arange(0, 11, 1)):
    """Simulate BPSK over AWGN channel and compute BER for various SNR values."""
    ber = []
    for snr_db in snr_range:
        bits = np.random.randint(0, 2, num_bits)
        modulated_signal = 2 * bits - 1
        noise_std = np.sqrt(1 / (2 * 10 ** (snr_db / 10)))
        received_signal = modulated_signal + noise_std * np.random.randn(len(modulated_signal))
        demodulated_bits = (received_signal >= 0).astype(int)
        ber.append(np.sum(bits != demodulated_bits) / num_bits)
    return snr_range, ber
 
def plot_ber(snr_range, ber):
    """Plot BER vs. SNR on a semi-logarithmic scale."""
    plt.figure()
    plt.semilogy(snr_range, ber, marker='o', linestyle='-')
    plt.xlabel('Eb/N0 (dB)')
    plt.ylabel('Bit Error Rate (BER)')
    plt.title('BPSK over AWGN Channel')
    plt.grid(True, which='both')
    plt.legend(['BPSK in AWGN'])
    plt.show()
 
# Run Simulation
snr_range, ber = simulate_bpsk_awgn()
plot_ber(snr_range, ber)