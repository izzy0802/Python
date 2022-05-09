from datetime import date
ano = int(input('Digite o ano ou coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano%4 == 0:
    print('É um ano bissexto')
else:
    print('Não é uma ano bissesto')