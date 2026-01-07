import os

os.system('cls')

numero1 = input('Digite o primeiro numero: ')
numero2 = input('Digite o segundo numero: ')
operador = input('Digite o operador [* | + | - | /]: ')
numero: float = 0

while True:
    
    try:
        if operador == '+':
            numero = float(numero1) + float(numero2)
            print(f'{numero1} + {numero2} = {numero}')
            break
        elif operador == '-':
            numero = float(numero1) - float(numero2)
            print(f'{numero1} - {numero2} = {numero}')
            break
        elif operador == '*':
            numero = float(numero1) * float(numero2)
            print(f'{numero1} * {numero2} = {numero}')
            break
        elif operador == '/':
            try:
                numero = float(numero1) / float(numero2)
                print(f'{numero1} / {numero2} = {numero}')
                break
            except ZeroDivisionError as e:
                print(f'Erro: {e}.')
                break
        else:
            print('Operadores aceitos [* | + | - | /]')
            break
    except ValueError as e:
        print(f'Erro: {e}.')
        break
        
