peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso/altura**2

if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc<= 25:
    print('Peso ideal')
else:
    print('Obesidade mórbida')