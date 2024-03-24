from time import sleep
from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
x = randint(0, 2)
print('Suas opções:\n[ 0 ] PEDRA \n[ 1 ] PAPEL \n[ 2 ] TESOURA')
jogada = int(input('Qual é sua jogada? '))
sleep(1)
print('JO')
sleep(1)
print('GEN')
sleep(1)
print('PO!!!\n')
if x == 0:
    if jogada == 0:
        print('EMPATAMOS!\n')
    elif jogada == 1:
        print('Você venceu\n')    
    elif jogada == 2:
        print('Você perdeu\n')
    else:
        print('JOGADA INVALIDA\n')
if x == 1:
    if jogada == 0:
        print('Você perdeu!\n')
    elif jogada == 1:
        print('EMPATE\n')    
    elif jogada == 2:
        print('Você ganhou!\n')
    else:
        print('JOGADA INVALIDA\n')
if x == 2:
    if jogada == 0:
        print('Você ganhou!\n')
    elif jogada == 1:
        print('Você perdeu\n')    
    elif jogada == 2:
        print('EMPATE\n')
    else:
        print('JOGADA INVALIDA\n')
print('-' * 20)
print('Eu escolhi: {}'.format(itens[x]))
print('Você escolheu: {}'.format(itens[jogada]))
print('-' * 20)