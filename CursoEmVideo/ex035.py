r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1<r2+r2 and r2<r3+r1 and r3<r2+r1:
    print('É um triângulo')
else:
    print('Não é um triângulo')