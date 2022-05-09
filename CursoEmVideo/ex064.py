n1 = cont = soma =0
n1 = int(input('Digite um numero [999 para parar]: '))
while n1!= 999:
    soma +=n1
    cont +=1
    n1 = int(input('Digite um numero [999 para parar]: '))
print(f'A quantidade de numeros digitados foi {cont} e a soma deles é {soma}')