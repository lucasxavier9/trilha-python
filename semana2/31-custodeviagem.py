km = float(input('Qual a distância da sua viagem em KM: '))
semdesconto = km * 0.50
comdesconto = km * 0.45

if km < 200:
    print('O preço da sua viagem será de R${}'.format(semdesconto))
else:
    print('O preço da sua viagem será de R${}'.format(comdesconto))