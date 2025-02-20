'''
This is the first lab of EE363.

Purpose:
The purpose of this lab is to explore the application of unit step functions in waveform transformations and to visualize the behavior of the resulting function using Python.

Procedure:
1. Define a unit step function, `unitfunc`, which returns 1 for t >= 0 and 0 otherwise.
2. Create a time array `t` ranging from -1 to 1 with small increments using `numpy`.
3. Define the function X2(t) based on the given mathematical expression:
   X2(t) = (t + 0.5) * [u(t + 0.5) - u(t)] + (0.5 - t) * [u(t) - u(t - 0.5)]
4. Use the `matplotlib` library to plot the function X2(t) over the time range.
5. Label the axes, add a title, and enable gridlines for better readability.
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

# Define the function X2(t) based on the given expression
X2 = (t + 0.5) * (unitfunc(t + 0.5) - unitfunc(t)) + \
     (0.5 - t) * (unitfunc(t) - unitfunc(t - 0.5))

# Plot the result
plt.plot(t, X2)
plt.title("Unit Step Function Transformation")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.grid(True)  # Adds a grid to the plot for better readability
plt.show()
