import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


def Fourier(f,N,period):
    x_values = np.linspace(-10,10,1000)
    y_values = []
    A_n,B_n = [],[]
    for x in x_values:
        y_values.append(f(x))
    plt.plot(x_values,y_values)
    plt.title('Given function')
    plt.show()
    a_0 = (1/period)*(quad(f,-period/2,period/2)[0])
    final_y = [a_0/2]*len(x_values)
    plt.plot(x_values,final_y)
    for n in range(1,N):
        y_values_cos, y_values_sin = [],[]
        func_cos = lambda x: math.cos(n*x)
        final_cos = lambda x: f(x)*func_cos(x)
        a_n = (2/period)*(quad(final_cos,-period/2,period/2)[0])
        A_n.append(a_n)
        func_sin = lambda x: math.sin(n*x)
        final_sin = lambda x: f(x)*func_sin(x)
        b_n = (2/period)*(quad(final_sin,-period/2,period/2)[0])
        B_n.append(b_n)
        for x in x_values:
            y_values_cos.append(a_n*math.cos(n*x))
            y_values_sin.append(b_n*math.sin(n*x))
        plt.plot(x_values, y_values_sin)
        plt.plot(x_values,y_values_cos)
        for i in range(len(x_values)):
            final_y[i]= final_y[i] + y_values_cos[i] + y_values_sin[i]
    plt.title('Individual functions that will compose the Fourier series')
    plt.show()
    plt.plot(x_values,final_y)
    plt.title('Final function')
    plt.show()
    return

'''Enter function here: '''
'''Carefull to use notation that python will understand (math is imported)'''
f = lambda x: abs((x%math.pi)-2)

'''Number of iterations'''
N = 10

'''Have to manually enter period of function'''
period = 2*math.pi

Fourier(f,N,period)

