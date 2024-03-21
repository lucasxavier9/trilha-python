print('-' * 25 )
print ('Analisador de triângulos')
print('-' * 25 )
reta1 = float(input('Informe a primeira reta: '))
reta2 = float(input('Informe a segunda reta: '))
reta3 = float(input('Informe a terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os segmentos acima podem formar triângulo!')
else:
    print('Os segmentos acima não podem formar triângulo!')
