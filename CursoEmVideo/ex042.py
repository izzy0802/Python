r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1<r2+r2 and r2<r3+r1 and r3<r2+r1:
    print('É um triângulo')
    if r1 == r2 and r2 == r3:
        print('Equilátero')
    if r1 ==r2 and r2!=r3 or r2 == r3 and r2!=r1:
        print('Isósceles')
    if r1 != r2 and r2 != r3:
        print('Escaleno')
else:
    print('Não é um triângulo')