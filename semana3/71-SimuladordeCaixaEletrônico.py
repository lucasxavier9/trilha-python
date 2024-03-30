print('=' * 25)
print('        BANCO DEV  ')
print('=' * 25)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
nota = 100
totNota = 0
while True:
    if total >= nota:
        total -= nota
        totNota += 1
    else:
        if totNota > 0:
            print(f'Total de {totNota} cédulas de R$ {nota}')
        if nota == 100:
            nota = 50
        elif nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        totNota = 0
        if total == 0:
            break

print('-' * 25)
print('Volte sempre ao banco DEV! ')
print('-' * 25)