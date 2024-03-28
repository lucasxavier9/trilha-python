cont = soma = n1 = 0
n1 = int(input('[999]-> Para o programa \nDigite um número: '))
while n1 != 999:
    soma += n1
    cont += 1
    n1 = int(input('[999]-> Para o programa \nDigite um número: '))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}')
