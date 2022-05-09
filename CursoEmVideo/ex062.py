print('\033[36m-=\033[m'*10)
print('10 TERMOS DE PA')
print('\033[36m-=\033[m'*10)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
deciom = termo + (10-1)*razao
cont = 1
total = 0
n = 10
while n != 0:
    total+=n
    while cont <= total:
        print(f'{termo}',end=' ->')
        termo+=razao
        cont+=1
        print('PAUSA')
        n = int(input('Quantos termos voce quer mostrar a mais?'))
print('FIM')

