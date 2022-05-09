maior = 0
menor = 0
for c in range(1,6):
    peso = float(input('Digite o seu peso '))
    if c == 1:
        maior = c
        menor = c
    else:
        if peso>maior:
            maior = peso
        if peso<menor:
            menor = peso
print(f'O maior peso lido é de {maior}')
