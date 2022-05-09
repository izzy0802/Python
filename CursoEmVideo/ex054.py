from datetime import date
cont = 0
for c in range(0,6):
    data = int(input('Digite a sua data de nascimento: '))
    ano = date.today().year - data
    if ano >= 18:
        c+=1
    else:
        cont += 1
print(f'{cont} pessoas ainda nao sao maiores de idade')