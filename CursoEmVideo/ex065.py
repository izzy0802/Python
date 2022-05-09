continuar = 'S'
maior = menor = cont = soma = media = 0
while continuar in 'Ss':
    n = int(input('Digite um numero: '))
    soma+=n
    cont+=1
    if cont ==1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma/cont
print(f'Voce digitou {cont}, a média foi {media}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')