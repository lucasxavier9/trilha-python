'''from math import factorial
f = int(input('Digite um número inteiro para calcular seu fatorial: '))
fat = factorial(f)
print(f'O fatoral de {f} é {fat}')
'''

f = int(input('Digite um número inteiro para calcular seu fatorial: '))
c = f
n = 1
print(f'Calculando {f}!: ')
while c > 0:
    print(f'{c}', end=' ')
    print(' x ' if c > 1 else ' = ', end='')
    n *= c
    c -=1
print (f'O fatorial de {f} é {n}')