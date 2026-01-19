# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def zipper(lista1: list[str], lista2: list[str]):
    
    intervalo: int = min(len(lista1), len(lista2))
    nova_lista: list[tuple[str, str]] = []
    
    for i in range(intervalo):
        nova_tupla: tuple[str , str] = (lista1[i], lista2[i])
        nova_lista.append(nova_tupla)
        
    return nova_lista

lista1: list[str] = ['BA', 'SP', 'MG', 'RJ']
lista2: list[str] = ['Salvador', 'Ubatuba', 'Belo Horizonte']

retorno = zipper(lista1, lista2)
print(retorno)

retorno_zip = zip(lista1,lista2)
print(list(retorno_zip))
    
from itertools import zip_longest

retorno_zip_longo = zip_longest(lista1,lista2, fillvalue='Sem cidade') 
print(list(retorno_zip_longo))
