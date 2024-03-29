tot18 = totH = totm20 = 0
while True:
    print('-' * 23)
    print('CADASTRE UMA PESSOA')
    print('-' * 23)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1
    x = ' '
    while x not in 'SN':
        x = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if x == 'N':
        break
print(f'total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos o total de {totH} Homens cadastrados')
print(f'temos o total de {totm20} mulheres com menos de 20 anos')