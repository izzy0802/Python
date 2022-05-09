frase = str(input('Diga uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in (len(junto)-1,-1,-1):
    inverso+=junto[letra]
if inverso == junto:
    print('É palindromo')
else:
    print('Não é palindromo')
