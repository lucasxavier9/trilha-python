import math
angulo = float(input('Digite o angulo que você deseja: '))
print('O angulo de {} tem o sen de {:.2f}'.format(angulo, math.sin(math.radians(angulo))))
print('O angulo de {} tem o cos de {:.2f}'.format(angulo, math.cos(math.radians(angulo))))
print('O angulo de {} tem o tangente de {:.2f}'.format(angulo, math.tan(math.radians(angulo))))