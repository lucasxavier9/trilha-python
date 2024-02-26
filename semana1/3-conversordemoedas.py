real = int(input('Quanto você quer investir: '))
dolar = real / 4.93
euro = real / 5.33
print('com {} R$, você consegue comprar {:.2f} dolar e {:.2f} euro'.format(real, dolar, euro))