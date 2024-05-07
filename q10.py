import numpy as np

def f(x):
    return x**2 -2*x-1

def bisseccao(a, b, tol, max_iter):
    fa = f(a)
    fb = f(b)
    
    if fa * fb > 0:
        print("A função não muda de sinal no intervalo fornecido.")
        return None
    
    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        
        if np.abs(fc) < tol or np.abs(b - a) < tol:
            print("Bisseccao convergiu em {} iterações.".format(i+1))
            return c
        
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    
    print("Bisseccao não convergiu em {} iterações.".format(max_iter))
    return None

def falsa_posicao(a, b, tol, max_iter):
    fa = f(a)
    fb = f(b)
    
    if fa * fb > 0:
        print("A função não muda de sinal no intervalo fornecido.")
        return None
    
    for i in range(max_iter):
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)
        
        if np.abs(fc) < tol or np.abs(b - a) < tol:
            print("Falsa posição convergiu em {} iterações.".format(i+1))
            return c
        
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    
    print("Falsa posição não convergiu em {} iterações.".format(max_iter))
    return None

# Intervalo [a, b] e tolerância
a = 2
b = 3
tol = 1e-5
max_iter = 10

# Calculando a raiz usando o método da bissecção
raiz_bisseccao = bisseccao(a, b, tol, max_iter)
if raiz_bisseccao is not None:
    print("Raiz encontrada pela bissecção:", raiz_bisseccao)

# Calculando a raiz usando o método da falsa posição
raiz_falsa_posicao = falsa_posicao(a, b, tol, max_iter)
if raiz_falsa_posicao is not None:
    print("Raiz encontrada pela falsa posição:", raiz_falsa_posicao)
