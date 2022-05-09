print('\033[36m-=\033[m'*10)
print('10 TERMOS DE PA')
print('\033[36m-=\033[m'*10)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
deciom = termo + (10-1)*razao
for c in range(termo,deciom,razao):
    print(f'{c}',end=' ->')
print('ACABOU')
