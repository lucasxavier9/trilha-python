lista = []
maior = menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]

print('-' * 35)
print(f'\nVocê digitou os valores {lista}')
for i, v in enumerate(lista):
    if v == maior:
        print(f'\no maior valor digitado foi {maior} na posição {i}..')
for i, v in enumerate(lista):
    if v == menor:
        print(f'\no menor valor digitado foi {menor} na posição {i}..')
