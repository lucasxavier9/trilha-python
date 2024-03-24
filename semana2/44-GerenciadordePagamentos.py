print('-' * 25)
print('****** Loja de teste ******')
print('-' * 25)
preco = float(input('Preço de compra: '))
print ('Forma de pagamento ? \n[1]à vista dinheiro/cheque \n[2]à vista cartão \n[3]2x no cartão \n[4]3x ou mais no cartão')
compra = int(input('Qual é a opção? '))
if compra == 1:
    preco1 = preco - ((preco*10)/100)
    print('Sua compra de {} vai te custar {} no final'.format(preco, preco1))
elif compra == 2:
    preco2 = preco - ((preco*5)/100)
    print('Sua compra de {} vai te custar {} no final'.format(preco, preco2))
elif compra == 3:
    print('Sua compra de {} vai te custar {} no final'.format(preco, preco))
elif compra == 4:
     preco4 = preco + ((preco*20)/100)
     print('Sua compra de {} vai te custar {} no final'.format(preco, preco4))
else:
    print('Opção invalida, tente novamente')