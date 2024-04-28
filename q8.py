# from sympy import sin, cos, exp
import numpy as np

der = [np.cos(0), -np.sin(0), -np.cos(0), np.sin(0), np.cos(0), -np.sin(0), -np.cos(0)]

def fatorial(a):
    fat = 1
    for i in range(a):
        fat = (i+1) * fat

    return fat

def mcLaurin(x):
    y = 0
    for i in range(7): # começa no zero

        y += der[i] * (x**(i+1))/(fatorial(i+1))

    return y

print(mcLaurin(1))