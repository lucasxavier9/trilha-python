import random
print('Sou seu computador..')
print('Acabei de pensar em um número de 0 a 10')
print('Será que você consegue advinhar qual foi?')
x = random.randint(0, 10)
contador = 0
while True:
    palpite = int(input('Qual o seu papilte? '))
    contador += 1
    if palpite < x:
        print('Mais... tente mais uma vez')
    elif palpite > x:
        print('Menos... tente mais uma vez')
    elif palpite == x:
        print(f'Acertou com {contador} tentativas. Parabéns!')
        break
