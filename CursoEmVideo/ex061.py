print('\033[36m-=\033[m'*10)
print('10 TERMOS DE PA')
print('\033[36m-=\033[m'*10)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
deciom = termo + (10-1)*razao
cont = 1
while cont <= 10:
    print(f'{termo}',end=' ->')
    termo+=razao
    cont+=1