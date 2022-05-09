salario = float(input('Digite o salario do funcionario'))
if salario > 1250:
    porcentual = 1250*10/100
    print(f'O salario com o aumento é de {salario+porcentual}')
else:
    porcentual = salario*15/100
    print(f'O salario com o aumento é de {salario+porcentual}')