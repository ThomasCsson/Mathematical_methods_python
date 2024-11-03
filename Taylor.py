import numpy as np
import matplotlib.pyplot as plt
from sympy import sin, symbols, diff, lambdify
import math

N = 10
a = 1

x_vals = np.linspace(-4, 6, 400)
x = symbols('x')


'''Function'''
f = sin(x)+x


f_func = lambdify(x, f, 'numpy')
y_vals = f_func(x_vals)
final_y = [0]*len(x_vals)


for n in range(N):
    f_Nth_der = diff(f, x, n)
    f_prime_func = lambdify(x, f_Nth_der, 'numpy')
    f_Nth = f_prime_func(a)/(math.factorial(n))*(x-a)**n

    Nth_function = lambdify(x, f_Nth, 'numpy')
    y_prime_vals = Nth_function(x_vals)
    if isinstance(y_prime_vals, np.ndarray):
        plt.plot(x_vals, y_vals)
        plt.plot(x_vals, y_prime_vals)
    for i in range(len(final_y)):
        final_y[i] += Nth_function(x_vals[i])
plt.show()
plt.plot(x_vals,final_y)
plt.show()
plt.plot(x_vals,y_vals)
plt.show()


