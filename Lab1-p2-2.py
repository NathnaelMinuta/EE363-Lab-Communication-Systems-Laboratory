'''
This is the first lab of EE363.

Purpose:
The purpose of this lab is to apply the unit step function to create and visualize a waveform based on a cosine function. The result demonstrates the effect of 
multiplying a trigonometric function with unit step transformations.

Procedure:
1. Define a unit step function, `unitfunc`, which returns 1 for t >= 0 and 0 otherwise.
2. Create a time array `t` ranging from -1 to 1 with small increments using `numpy`.
3. Define the function X4(t) using the formula:
   X4(t) = cos(4πt) * [u(t + 0.5) - u(t - 0.5)]
4. Use the `matplotlib` library to plot X4(t) over the time range.
5. Add titles, labels, and gridlines for better visualization.
6. Display the plot.

Author: Nathnael Minuta
Student ID: 15778991
Date: 01/21/2025
'''

import matplotlib.pyplot as plt
import numpy as np

# Define the unit step function
def unitfunc(time_array):
    # Returns 1 for t >= 0 and 0 otherwise
    result = (time_array >= 0.0) * 1.0
    return result

# Define the time array
t = np.arange(-1, 1, 0.00001)

# Define the function X4(t) based on the given formula
X4 = np.cos(4 * np.pi * t) * (unitfunc(t + 0.5) - unitfunc(t - 0.5))

# Plot the result
plt.plot(t, X4)
plt.title("Cosine with Unit Step Function Transformation")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.grid(True)  # Adds a grid to the plot for better readability
plt.show()
