media = 0
maioridade = 0
nomevelho = ''
mulher20 = 0
for c in range(1, 5):
    print(f'--- {c}° Pessoa: ---')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    media += idade /4
    sexo = str(input('Sexo [M/F]: ')).strip()
    if c == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1

print(f'A média de idade do grupo é de {media} anos')
print(f'O homem mais velho tem {maioridade} anos e se chama {nomevelho}')
print(f'Ao todo são {mulher20} mulheres com menos de 20 anos')