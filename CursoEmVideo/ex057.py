sexo = str(input('Digite o seu sexo F/M: ')).upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos, por favor digite novamente: ')).strip().upper()[0]
print(f'sexo registrado com sucesso {sexo}')