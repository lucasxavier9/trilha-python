lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adcionado!')
    else:
        print('Valor já adcionado')
    r = str(input('Quer continuar? [S/N]: '))
    if r in 'Nn':
        break
lista.sort()
print(f'Você digitou os valores: {lista}')
    