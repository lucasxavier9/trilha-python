import math
cOP = float(input('Comprimento do cateto oposto: '))
cadj = float(input('Comprimento do cateto Adjacente: '))
print('A hipotenusa vai medir:{:.2f} '.format(math.hypot(cOP, cadj)))