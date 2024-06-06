import numpy as np

# Definindo a função f(x)
def f(x):
    return x**3

# Valor exato da integral
a, b = 1, 3
valor_exato = (b**4 / 4) - (a**4 / 4)

# Função para calcular a Regra de Simpson
def simpson(f, a, b, n):
    if n % 2 == 1:  # Simpson's rule requires an even number of intervals
        n += 1
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    S = y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2])
    return (h / 3) * S

# Valores de n (número de subintervalos/parábolas)
n_values = [1, 2, 4, 8]

# Calculando as aproximações
aproximacoes = [simpson(f, a, b, n) for n in n_values]

# Resultados
resultados = []
for n, aprox in zip(n_values, aproximacoes):
    erro = abs(valor_exato - aprox)
    resultados.append((n, aprox, erro))

# Exibindo os resultados
print(f"Valor exato da integral: {valor_exato:.4f}\n")

for n, aprox, erro in resultados:
    print(f"Com {n} parábolas (n = {n}):")
    print(f"  Aproximação: {aprox:.4f}")
    print(f"  Erro: {erro:.4f}\n")
