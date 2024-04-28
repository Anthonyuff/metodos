# Erro absoluto = |valor verdadeiro - valor calculado|
# Erro relativo = |valor verdadeiro - valor calculado|/|valor verdadeiro|
# Erro percentual = Erro absoluto * Erro relativo * 100

a = [1.000, 0.999]
b = [0.34678, 0.3468]
c = [0.000005, 0.00000495]
d = [15000.85, 14999.0]

def calc_menor_erro(v_v, v_c): # valor ver e calc
    erro_ver = v_v - v_c
    if erro_ver < 0: erro_ver *= -1 # modulo

    erro_rel = erro_ver/v_v
    if erro_rel < 0: erro_rel *= -1 # modulo
    
    erro_per = erro_rel * 100

    return erro_per


def compara_erro_per(*args):

    erros_per = []
    for i in args:
        erros_per.append(calc_menor_erro(i[0], i[1]))


    menor = 0
    for j in range(len(erros_per)):
        if j > 0:
            if erros_per[j] < erros_per[j-1]:
                menor = erros_per[j]
        else:
            menor = j
    
    frase = f'valor exato: {args[j][0]} | valor exato: {args[j][1]} | erro percentual: {menor} \n {erros_per}'

    return frase

print(compara_erro_per(a, b, c, d))