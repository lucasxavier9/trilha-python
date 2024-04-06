tupla = ('Lapís', 1.7, 'Borracha', 2, 'Caderno', 5, 'Estojo', 3, 'Marca texto', 1.50, 'Mochila', 55)
print('-' * 38)
print(f'{"LISTAGEM DE PREÇO":^38}')
print('-' * 38)

for pos in range (0, len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<30}', end ='')
    else:
        print(f'R${tupla[pos]:>5.2f}')
print('-' * 38)
