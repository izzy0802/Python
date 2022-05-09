nome  = str(input('Digite o seu nome completo: ')).strip()
nome = nome.split()
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu ultimo nome é {len(nome)-1}')