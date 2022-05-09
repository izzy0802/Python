preco = float(input('Digite o preço normal do produto'))
condicao = int(input('Digite a condição de pagamento sendo 1 para a vista em dinheiro/cheque e 2 para parcelado'))

if condicao == 1:
    porcentual = preco*10/100
    print(f'Seu desconto é de {preco-porcentual}')
elif condicao == 2:
    parcela = int(input('Em quantas parcelas será feito?'))
    if parcela == 1:
        porcentual = preco*5/100
        print(f'Seu desconto é de {preco-porcentual}')
    elif parcela == 2:
        print(f'O preço é de {preco}')
    elif parcela >= 3:
        porcentual = preco*20/100
        print(f'O preço terá 20 porcento de juros sendo entao, {preco+porcentual}')



