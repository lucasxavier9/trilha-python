reta1 = float(input('Informe a primeira reta: '))
reta2 = float(input('Informe a segunda reta: '))
reta3 = float(input('Informe a terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os segmentos acima podem formar um triângulo ', end='')
    if reta1 == reta2 and reta2 == reta3:
        print('Equilátero')
    elif reta1 != reta2 != reta3 != reta1:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Os segmentos acima não podem formar um triângulo!')
