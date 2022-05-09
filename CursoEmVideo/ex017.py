from math import hypot
Cop = float(input('Cumprimeiro do cateto oposto: '))
Cad = float(input('Cumprimento do cateto adjacente: '))
print('A hipotenusa vai medir {:.2f}'.format(hypot(Cop,Cad)))
'''
Cop = float(input('Cumprimento do cateto oposto: '))
Cad = float(input('Cumprimento do cateto adjacente: '))
hip = (Cop**2+Cad**2)**(1/2)
print('A hipotenusa vai medir {:.2f}'.format(hip))
'''
