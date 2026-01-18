"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
import os
os.system('cls')

cpf: str = '093780746'
lista: list[int] = [10, 9, 8, 7, 6, 5, 4, 3, 2]
soma: int = 0
contador_regressivo: int = 10

i = 0
while i < len(cpf):
    print(f'indice {i}, digito {cpf[i]}')
    i += 1

print('\n','-' * 50, '\n')
print('PARTE 1 - PRIMEIRO DIGITO\n')

for indice, numero in enumerate(cpf):
    numero_int = int(numero)
    multiplicador = numero_int * lista[indice] # forma 1
    print(f'via indice {lista[indice]}')
    print(f'via contador {contador_regressivo}')
    contador_regressivo -= 1 # forma 2
    soma += multiplicador

resto_divisao1 = (soma * 10) % 11
print(resto_divisao1)
digito1 = 0 if resto_divisao1 > 9 else resto_divisao1
print(f'primeiro digito {digito1}')

print('\n','-' * 50, '\n')
print('PARTE 2 - SEGUNDO DIGITO\n')

resultado = cpf + str(digito1)
print(resultado)
iterador = 10

somatoria = 0
for digito in resultado:
    multiplicacao = int(digito) * iterador
    print(int(digito), ' x ', iterador, ' = ', multiplicacao)
    somatoria += multiplicacao
    print('soma = ',somatoria)
    iterador -= 1
print('resultado = ',somatoria)

resto_divisao2 = (somatoria * 10) % 11
print('diferenca', resto_divisao2)

digito2 = resto_divisao2 if resto_divisao2 <= 9 else 0
print(digito2)

print('\n','-' * 50, '\n')
print('CPF COMPLETO\n')
    
cpf_completo = cpf + ' ' + str(digito1) + str(digito2)
print(cpf_completo, '\n')
