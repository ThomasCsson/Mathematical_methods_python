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

