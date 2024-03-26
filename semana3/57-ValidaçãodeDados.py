while True:
    sexo = str(input('Informe seu sexo [M/F]: ')).strip()
    if sexo in 'MmFf':
        print(f'Sexo {sexo} registrado com sucesso')
        break
    else:
        print('Dados inválidos. Por favor, informe seu sexo: ')
        
        
        