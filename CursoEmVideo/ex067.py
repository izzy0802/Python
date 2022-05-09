n = 1
while n > 0:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('\033[36m-=\033[m'*12)
    for i in range(0,11):
        multiplicacao  = i*n
        print(f'{n} x {i} = {multiplicacao}')
    print('\033[36m-=\033[m'*12) 
print('Programa tabuada encerrado, volte sempre!')