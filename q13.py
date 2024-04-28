import numpy as np

# Definição da função
def f(x):
    return np.cos(x) + 1 - x


def encontrar_x0(a, b, num_partitions):
    
    x_values = np.linspace(a, b, num_partitions)
    
    x0 = min(x_values, key=lambda x: abs(f(x)))
    return x0

# Intervalo [a, b] e número de partições
a = 0.8
b = 1.6
num_partitions = 100


x0 = encontrar_x0(a, b, num_partitions)
print("Valor inicial x0:", x0)

import numpy as np


def f(x):
    return np.cos(x) + 1 - x

def df(x):
    return -np.sin(x) - 1

# Método de Newton-Raphson
def newton_raphson(x0, tol, max_iter):
    for i in range(max_iter):
        fx0 = f(x0)
        if abs(fx0) < tol:
            print("Convergiu para a raiz após {} iterações.".format(i+1))
            return x0
        x1 = x0 - fx0 / df(x0)
        if abs(x1 - x0) < tol:
            print("Diferença entre duas iterações é menor que 10^-9.")
            return x1
        x0 = x1
    print("Não convergiu após {} iterações.".format(max_iter))
    return None

# Valor inicial x0, tolerância e número máximo de iterações
x0 = 1.0  # valor inicial calculado anteriormente
tol = 1e-9  # tolerância
max_iter = 10  

# Executando o método de Newton-Raphson
raiz = newton_raphson(x0, tol, max_iter)
print("Raiz encontrada pelo método de Newton-Raphson:", raiz)
