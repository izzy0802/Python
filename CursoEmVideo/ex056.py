somaIdade = 0
maiorIdadeH = 0
nomeH = ''
menor20 = 0
for c in range(1,5):
    print(f'------{c} PESSOA -----')
    nome = str(input('Digite o seu nome: ')).strip()
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite o seu sexo, sendo F para feminino e M para masculino: ')).strip().upper()
    somaIdade += idade
    if c == 1 and sexo == 'M':
        maiorIdadeH = idade
        nomeH = nome
    if sexo == 'M' and idade> maiorIdadeH:
        maiorIdadeH = idade
        nomeH = nome
    if sexo == 'F' and idade < 20:
        menor20 += 1
print(f'A média das idade do grupo é de {somaIdade/4}')
print(f'O homem mais velho tem {maiorIdadeH} de idade e seu nome é {nomeH} ')
print(f'A quantidade de mulheres com menos de 20 anos é {menor20}')