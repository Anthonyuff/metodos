numero=int(input('escolhe um numero:'))
resultado = numero

binario=[]
biin=''

while resultado!=0:
    resto = resultado % 2
    binario.append(resto)
    resultado = resultado // 2

binario.reverse()
for i in binario:
    biin+=str(i)
print(biin)

















