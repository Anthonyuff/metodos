import numpy as np

# Definir o sistema de equações
A = np.array([[10, 5, 2, 1],
              [5, 10, -3, 2],
              [2, -3, 12, -5],
              [1, 2, -5, 12]])

b = np.array([18, 14, -9, 10])

# Valores iniciais
x0 = np.array([2.0, 2.0, 2.0, 2.0])

# Função para o método de Jacobi
def jacobi(A, b, x0, iterations):
    n = len(b)
    x = x0.copy()
    for it in range(iterations):
        x_new = np.zeros_like(x)
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
        x = x_new
        print(f'Iteração {it + 1}: {x}')
    return x

# Função para o método de Gauss-Seidel
def gauss_seidel(A, b, x0, iterations):
    n = len(b)
    x = x0.copy()
    for it in range(iterations):
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - s) / A[i][i]
        print(f'Iteração {it + 1}: {x}')
    return x

# Número de iterações
iterations = 6

print("Método de Jacobi:")
jacobi_solution = jacobi(A, b, x0, iterations)
print(f'Solução final (Jacobi): {jacobi_solution}')

print("\nMétodo de Gauss-Seidel:")
gauss_seidel_solution = gauss_seidel(A, b, x0, iterations)
print(f'Solução final (Gauss-Seidel): {gauss_seidel_solution}')

# Comparação das soluções finais
difference = np.abs(jacobi_solution - gauss_seidel_solution)
print(f'\nDiferença entre as soluções finais (Jacobi vs Gauss-Seidel): {difference}')
