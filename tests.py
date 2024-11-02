import numpy as np
import matplotlib.pyplot as plt
from sympy import sin, symbols, diff, lambdify
import math

N = 5
a = 1

x_vals = np.linspace(-10, 10, 400)
x = symbols('x')
f = sin(x)
f_func = lambdify(x, f, 'numpy')
y_vals = f_func(x_vals)


for n in range(N):
    f_Nth_der = diff(f, x, n)
    f_prime_func = lambdify(x, f_Nth_der, 'numpy')
    f_Nth = f_prime_func(a)/(math.factorial(n))*(x-a)**n
    Nth_function = lambdify(x, f_Nth, 'numpy')

    y_prime_vals = Nth_function(x_vals)

    # Plot the function and its derivative


    plt.plot(x_vals, y_vals)
    plt.plot(x_vals, y_prime_vals)
plt.show()

print(f_func(0))
