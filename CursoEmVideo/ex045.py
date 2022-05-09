from random import randint
from time import sleep
itens = ('pedra','papel','tesoura')
computador = randint(0,2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual a sua jogada?  '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('\033[36m-=\033[m'*11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('\033[36m-=\033[m'*11)
if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador venceu')
    elif jogador == 2:
        print('Computador venceu')
    else:
        print('Jogada invalida')
elif computador == 1:
    if jogador == 0:
        print('Computador venceu')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador venceu')
    else:
        print('Jogada invalida')
elif computador == 2:
    if jogador == 0:
        print('Jogador venceu')
    elif jogador == 1:
        print('Computador venceu')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada invalida')