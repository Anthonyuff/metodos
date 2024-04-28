bin_input = '1001001110011010'
res_b16 = ''

# Adapta o número binário para ter um comprimento múltiplo de 4
while len(bin_input) % 4 != 0:
    bin_input = '0' + bin_input

print("Número binário adaptado:", bin_input)

for i in range(0, len(bin_input), 4):
    grupo_bin = bin_input[i:i+4]
    print("Parte binária separada:", grupo_bin)

   
    grupo_hexa = 0
    for j, bit in enumerate(reversed(grupo_bin)):
        grupo_hexa += int(bit) * (2 ** j)
    
    if grupo_hexa > 9:
        word = 'ABCDEF'
        for k in range(6):
            if grupo_hexa == (k + 10):
                grupo_hexa = word[k]
        
    res_b16 += str(grupo_hexa)

print("Número hexadecimal:", res_b16)

hex_input = '93CA'
bin_output = ''

# Mapeando cada dígito hexadecimal para seu equivalente binário de 4 bits
hex_to_bin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
              '4': '0100', '5': '0101', '6': '0110', '7': '0111',
              '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
              'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

# Iterando sobre cada dígito hexadecimal e convertendo para binário
for digit in hex_input:
    bin_output += hex_to_bin[digit]

print("Número hexadecimal:", hex_input)
print("Número binário:", bin_output)