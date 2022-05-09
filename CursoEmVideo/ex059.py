n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero numero: '))
finaliza = False
while not finaliza:
    print('''
        [1] soma
        [2] multiplica
        [3] maior
        [4] novos numeros
        [5] sair do programa ''')
    opcao = int(input('Qual a sua opção: '))
    if opcao == 1:
        soma = n1 + n2
        print(f'O resultado de {n1} + {n2} é {soma}')
    if opcao == 2:
        mult = n1 * n2
        print(f'O resultado de {n1} x {n2} é {mult}')
    if opcao == 3:
        if n1 > n2:
            print(f'O {n1} é o maior')
        else:
            print(f'O {n2} é o maior')
    if opcao == 4:
        print('Informe os numeros novamente:')
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero numero: '))
    if opcao == 5:
        finaliza = True