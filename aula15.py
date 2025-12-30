# nome = input('Qual o seu nome? ')
# print(f'O seu nome é {nome}')


numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

if not numero_1.isdigit() or not numero_2.isdigit():
    print('Por favor, digite apenas números inteiros.')
    exit()

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')
