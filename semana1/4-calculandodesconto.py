produto = float(input('Qual o preço do produto? R$ '))
desconto = produto - (produto * 5/100)
print('O produto de R${} com o descontão de 5% vai custar R${}'.format(produto, desconto))