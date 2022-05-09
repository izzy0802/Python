valor = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salario do comprador '))
ano = int(input('Digite quanto anos pretende ser feita a parcela '))

porcentagem = salario*30/100
parcela = valor/(ano*12)

if parcela <= porcentagem:
    print('O valor a ser pago sera de {:.2f}'.format(parcela))
elif parcela > porcentagem:
    print('O valor mensal excedeu os 30 porcento do salario do comprador, empréstimo negado')
