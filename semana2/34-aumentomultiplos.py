salario = float(input('Qual o seu salário? '))
if salario > 1250:
    salario = salario + ((salario * 10 )/100)
    print("Seu novo salario com aumento de 10% é de R${}".format(salario))
else:
    salario = salario + ((salario * 15)/100)
    print("Seu novo salario com aumento de 15% é de R${}".format(salario))
