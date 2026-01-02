import os
os.system('cls')

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um numero inteiro: ')

try:
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print(f'\nEsse numero {numero_int} e par\n')
    else:
        print(f'\nEsse numero {numero_int} e impar\n')
except Exception as e:
    print(f'\nFavor digitar um numero inteiro. \nErro: {e}\n')

print('-' * 50, '\n')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Informe a hora: ')

try:
    hora_int = int(hora)
    
    if hora_int >= 0 and hora_int <= 11:
        print('\nBom dia\n')
    elif hora_int >= 12 and hora_int <= 17:
        print('\nBoa tarde\n')
    elif hora_int >= 17 and hora_int <= 23:
        print('\nBoa noite\n')
    else:
        print('Digitar hora valida, numero inteiro de 0 a 23')
except Exception as e:
    print(f'\nFavor digitar um numero inteiro. \nErro: {e}\n')

print('-' * 50, '\n')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome: ')

try: # nao precisava de try except aqui
    nome_str = str(nome)
    print(nome_str)
    tamanho = len(nome_str)
    if tamanho >=2 and tamanho <= 4:
        print('\nSeu nome é curto\n')
    elif tamanho >= 5 and tamanho <= 6:
        print('\nSeu nome é normal\n')
    elif tamanho > 6 and tamanho <= 20:
        print('\nSeu nome é muito grande\n')
    else:
        print('\nO nome deve ter em 2 e 20 caracteres\n')
except Exception as e:
    print(f'\nO nome aceita apenas textos.\nErro{e}')