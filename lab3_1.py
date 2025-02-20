'''
This is the third lab of EE363.

Purpose:
Compute the Pearson-type correlation coefficient between two signals (x and y) using dt as the sample interval.

Procedure:
1. Import NumPy.
2. Define correlation_coefficient(x, y, dt).
3. Compute the means and variances (scaled by dt) of x and y.
4. Handle zero variance cases.
5. Calculate and return the correlation coefficient.
6. Test with sample signals.

Author: Nathnael Minuta
Student ID: 15778991
Date: 02/04/2025
'''


import numpy as np
def correlation_coefficient(x, y, dt):
   
   x_mean = np.mean(x)
   y_mean = np.mean(y)
   # Compute approximate 'variance' using sums * dt
   var_x = np.sum((x - x_mean)**2) * dt
   var_y = np.sum((y - y_mean)**2) * dt
   # -- Handle zero-variance cases --
   if np.isclose(var_x, 0.0) and np.isclose(var_y, 0.0):
       # Both x and y are constant signals
       if np.isclose(x_mean, y_mean):
           # Same constant => define correlation to be +1
           return 1.0
       else:
           # Different constants => define correlation to be 0
           return 0.0
   elif np.isclose(var_x, 0.0) or np.isclose(var_y, 0.0):
       # Only one signal is constant => correlation is undefined
       return float('nan')
   # -- Standard correlation formula --
   numerator = np.sum((x - x_mean) * (y - y_mean)) * dt
   denominator = np.sqrt(var_x) * np.sqrt(var_y)
   return numerator / denominator

if __name__ == "__main__":
   # Define time array
   t = np.arange(0, 5, 0.01)
   dt = t[1] - t[0]
   # x(t): constant 1
   x = np.ones_like(t)
   # g1(t): also constant 1
   g1 = np.ones_like(t)
   # g2(t): constant 0.5
   g2 = 0.5 * np.ones_like(t)
   # g3(t): constant -1
   g3 = -1.0 * np.ones_like(t)
   # g4(t): e^{-t/5}
   g4 = np.exp(-t/5.0)
   # g5(t): e^{-t}
   g5 = np.exp(-t)
   # g6(t): sin(2πt)
   g6 = np.sin(2 * np.pi * t)
   # Compute correlation coefficients
   r_x_g1 = correlation_coefficient(x, g1, dt)
   r_x_g2 = correlation_coefficient(x, g2, dt)
   r_x_g3 = correlation_coefficient(x, g3, dt)
   r_x_g4 = correlation_coefficient(x, g4, dt)
   r_x_g5 = correlation_coefficient(x, g5, dt)
   r_x_g6 = correlation_coefficient(x, g6, dt)
   # Print results
   print(f"Correlation r(x, g1) = {r_x_g1:.3f}")
   print(f"Correlation r(x, g2) = {r_x_g2:.3f}")
   print(f"Correlation r(x, g3) = {r_x_g3:.3f}")
   print(f"Correlation r(x, g4) = {r_x_g4:.3f}")
   print(f"Correlation r(x, g5) = {r_x_g5:.3f}")
   print(f"Correlation r(x, g6) = {r_x_g6:.3f}")