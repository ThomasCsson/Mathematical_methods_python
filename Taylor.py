import math
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, lambdify

x_values = np.linspace(-10,10,1000)
y_values = []

'''Function'''
f = lambda x: math.sin(x)

for x in x_values:
    y = f(x)
    y_values.append(y)

plt.plot(x_values,y_values)
plt.show()

x = symbols('x')

# Define the function
f = x**2 + 3*x + 5

# Compute the derivative
f_prime = diff(f, x)

# Convert the symbolic expressions to functions for numerical evaluation
f_func = lambdify(x, f, 'numpy')
f_prime_func = lambdify(x, f_prime, 'numpy')

# Generate x values
x_vals = np.linspace(-10, 10, 400)

# Calculate y values for the function and its derivative
y_vals = f_func(x_vals)
y_prime_vals = f_prime_func(x_vals)