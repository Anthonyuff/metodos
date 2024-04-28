def polinomio1(x):
    return 1 + 3*(x - 1) + 3*(x - 1)**2 + (x - 1)**3

def polinomio2(x):
    return 1 + 3*(x + 1) - 3*(x + 1)**2 + (x + 1)**3

def expandir_polinomio(polinomio):
    # Expandindo o polinômio
    expandido = ""
    termos = polinomio.split(" + ")
    for termo in termos:
        if "* x**" in termo:
            coeficiente, potencia = termo.split("* x**")
        else:
            coeficiente = termo
            potencia = "0"
        expandido += f"{coeficiente} * x**{potencia} + "
    return expandido[:-3]  # Removendo o último " + "




x = 1


polinomio1_expandido = expandir_polinomio(str(polinomio1(x)))
polinomio2_expandido = expandir_polinomio(str(polinomio2(x)))

# Verificando se os dois polinômios são equivalentes
if polinomio1_expandido == polinomio2_expandido:
    print("Os polinômios são equivalentes.")
else:
    print("Os polinômios são diferentes.")
