import numpy as np

# Definindo a função f(x)
def f(x):
    return x - 2 / x

# Pontos x0, x1, x2 e seus respectivos valores de f(x)
x_points = np.array([1, 2, 5])
y_points = f(x_points)

# Função para calcular o polinômio de Lagrange
def lagrange_polynomial(x, x_points, y_points):
    n = len(x_points)
    P = 0
    for i in range(n):
        L = 1
        for j in range(n):
            if i != j:
                L *= (x - x_points[j]) / (x_points[i] - x_points[j])
        P += y_points[i] * L
    return P

# Valores de x para avaliar o polinômio
x_values = [1.2, 2.2]

# Avaliando o polinômio nos pontos x_values
p_values = [lagrange_polynomial(x, x_points, y_points) for x in x_values]

# Valores exatos de f(x) para comparação
f_values = [f(x) for x in x_values]

# Exibindo os resultados
print("Resultados da Interpolação de Lagrange:")
print(f"Valor exato da função f(x) = x - 2/x nos pontos 1.2 e 2.2:")
for x, fx in zip(x_values, f_values):
    print(f"f({x}) = {fx}")

print("\nValores interpolados P(x) nos pontos 1.2 e 2.2:")
for x, px in zip(x_values, p_values):
    print(f"P({x}) = {px}")

print("\nErros de Interpolação:")
for x, fx, px in zip(x_values, f_values, p_values):
    print(f"Erro em x = {x}: |f(x) - P(x)| = {abs(fx - px)}")
