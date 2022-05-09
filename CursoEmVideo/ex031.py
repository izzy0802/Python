distancia = float(input('Qual a distancia percorrida? '))
if distancia > 200:
    preco = distancia* 0.45
    print(preco)
else:
    preco =distancia*0.50
    print(preco)