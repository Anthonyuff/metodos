def newton_raphson_cubica(N, x0, tol, max_iter):
    # Função e sua derivada para a raiz cúbica
    def f(x):
        return x**3 - N

    def df(x):
        return 3 * x**2
    
    # Iterações de Newton-Raphson
    for i in range(max_iter):
        fx0 = f(x0)
        if abs(fx0) < tol:
            print("Convergiu para raiz cúbica após {} iterações.".format(i+1))
            return x0
        x1 = x0 - fx0 / df(x0)
        x0 = x1
    print("Não convergiu para raiz cúbica após {} iterações.".format(max_iter))
    return None

def newton_raphson_quarta(N, x0, tol, max_iter):
    # Função e sua derivada para a raiz quarta
    def g(x):
        return x**4 - N

    def dg(x):
        return 4 * x**3
    
    # Iterações de Newton-Raphson
    for i in range(max_iter):
        gx0 = g(x0)
        if abs(gx0) < tol:
            print("Convergiu para raiz quarta após {} iterações.".format(i+1))
            return x0
        x1 = x0 - gx0 / dg(x0)
        x0 = x1
    print("Não convergiu para raiz quarta após {} iterações.".format(max_iter))
    return None

# Definindo o número N e o ponto inicial x0
N = 64  # número para encontrar a raiz cúbica e quarta
x0 = 1.0  # ponto inicial arbitrário
tol = 1e-12  # tolerância
max_iter = 100  # número máximo de iterações

# Calculando a raiz cúbica
raiz_cubica = newton_raphson_cubica(N, x0, tol, max_iter)
if raiz_cubica:
    print("Raiz cúbica de {} é aproximadamente {:.12f}".format(N, raiz_cubica))

# Calculando a raiz quarta
raiz_quarta = newton_raphson_quarta(N, x0, tol, max_iter)
if raiz_quarta:
    print("Raiz quarta de {} é aproximadamente {:.12f}".format(N, raiz_quarta))
