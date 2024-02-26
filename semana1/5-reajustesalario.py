salario = float(input('Qual seu salario? R$: '))
reajuste = salario + (salario *15/100)
print('Seu salario de {}R$,  com um aumento de 15%, passa a receber: {:.2f}R$'.format(salario, reajuste)) 