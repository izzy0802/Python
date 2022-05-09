n = int(input('Digite um numero: '))
print('\033[36m-=\033[m'*12)
for i in range(0,11):
    multiplicacao  = i*n
    print(f'{n} x {i} = {multiplicacao}')
print('\033[36m-=\033[m'*12)    