numero = int(input('Digite um numero: '))
print('''Digite a base a ser usada para a conversão 
[1] Converter para BINARIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL ''')
base = int(input('Sua opção: '))
if base == 1:
    print (f'{numero} convertido para BINARIO é {bin(numero)[2:]}')
elif base == 2:
    print (f'{numero} convertido para OCTAL é {oct(numero)[2:]}')
elif base == 3:
    print (f'{numero} convertido para HEXADECIMAL é {hex(numero)[2:]}')
else:
    print('Base invalida')
