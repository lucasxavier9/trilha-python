from random import randint
x = (randint(0, 20),randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20))
print(f'Os valores sorteados foram: {x}')
print(f'O maior valor sorteado foi {max(x)}')
print(f'O menor valor sorteado foi {min(x)}')