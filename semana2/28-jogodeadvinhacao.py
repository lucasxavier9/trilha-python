import random
from time import sleep
print('---------------------------------------------------')
print('Vou pensar em um número de 0 a 5, tente advinhar...')
print('---------------------------------------------------')
v1 = int(input('\nEm que numero eu pensei? '))
print('PROCESSANDO...')
x = random.randint(1, 5)
sleep(2)
if x == v1:
    print('Parabéns! você conseguiu me vencer!')
else:
    print('GANHEI!, eu pensei no número {} e não no {}'.format(x, v1))