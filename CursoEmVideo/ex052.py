n = int(input('Digite um numero: '))
for c in range(1, n+1):
    if(n%c == 0):
        print('\033[34m', end='')
    else:
        print('\033[33m', end='')
    print(f'{c}',end=' ')