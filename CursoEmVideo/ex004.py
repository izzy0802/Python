n = input('Digite algo: ')
print(type(n))
print('É numerico? {}'.format(n.isnumeric()))
print('É alfabético? {}'.format(n.isalpha()))
print('É alfanumérico? {}'.format(n.isalnum()))
print('É maiúsculo? {}'.format(n.isupper()))
print('É minúscula? {}'.format(n.islower()))
print('É espaço? {}'.format(n.isspace()))
print('Está capitalizado? {}'.format(n.istitle()))