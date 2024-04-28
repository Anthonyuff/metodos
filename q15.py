def newton_raphson_cubica( x0, tol, max_iter):
    # Função e sua derivada para a raiz cúbica
    def f(x):
        return x**2 -91

    def df(x):
        return 2*x
    
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

 
x0 = 10.0  
tol = 1e-7
max_iter = 10

# Calculando a raiz cúbica
raiz_cubica = newton_raphson_cubica(x0, tol, max_iter)
if raiz_cubica:
    print("Raiz cúbica de {} é aproximadamente {:.12f}".format(raiz_cubica,raiz_cubica))