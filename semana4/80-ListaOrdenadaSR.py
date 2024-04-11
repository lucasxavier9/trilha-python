lista = []
for c in range(0, 5):
    n1 = (int(input('Digite um valor: ')))
    if c == 0:
        lista.append(n1)
        print('Adcionado no começo da lista')
    elif n1 > lista[-1]:
        lista.append(n1)
        print('Adcionado no final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n1 <= lista[pos]:
                lista.insert(pos, n1)
                print(f'Adcionado na posição {pos}')
                break
            pos += 1

print(f'Os valores digites em ordem foi: {lista}')