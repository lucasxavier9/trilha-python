from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    pc = randint(0, 10)
    total = jogador + pc
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Ímpar, [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {pc}, total de {total} ', end='')
    print('deu par' if total % 2 == 0 else 'deu ímpar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes')