from random import choice
numero = [0,1,2,3,4,5]
numero = choice(numero)
print(numero)
numeroD = int(input(f'O computador pensou em um numero de 0 a 5, tente adivinhar, qual é o numero? '))
if numeroD == numero:
    print('Voce venceu!')
else:
    print('Voce perdeu')

