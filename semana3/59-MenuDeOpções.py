n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
while True:
    programa = int(input('[1] Somar\n[2] Multiplicar \n[3] Maior \n[4] Novos números \n[5] Sair do programa\n'))
    if programa == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} vale {soma}\n')
    elif programa == 2:
        multi = n1 * n2
        print(f'A Multiplicação entre {n1} e {n2} vale {multi}\n')
    elif programa == 3:
        if n1 > n2:
            print (f'Entre {n1} e {n2} o maior entre eles é {n1}\n')
        elif n2 > n1:
            print (f'Entre {n1} e {n2} o maior entre eles é {n2}\n')
    elif programa == 4:
        print('Informe os números novamente: ')
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
    elif programa == 5:
        print('ENCARRANDO PROGRAMA...')
        break
    else:
        print('Opção invalida, tente novamente')
        