from datetime import date
ano = int(input('Iforme o ano de nascimento: '))
idade = date.today().year - ano
if idade < 18:
    tempo = 18 - idade
    print(f'Voce ainda vai se alistar ao serviço militar, falta {tempo} anos')
elif idade == 18:
    print('É hora de se alistar')
else:
    tempo = idade - 18
    print(f'Já passou o tempo de alistamento, passou-se {tempo} do prazo')