# copy, sorted, produtos.sort
# Exercícios

import os
import copy
from rich import print
from typing import TypedDict

os.system('cls')


class Dict_Exercicio(TypedDict):
    nome: str
    preco: float

produtos: list[Dict_Exercicio] = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

'''EXERCICIO 1'''
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

novos_produtos = copy.deepcopy(produtos)

for produto in novos_produtos:
    preco = produto['preco']
    produto['preco'] = round(preco + (preco * 0.1),2)
    
print('EXERCICIO 1', novos_produtos)
    
'''EXERCICIO 2'''
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = copy.deepcopy(produtos)

produtos_ordenados_por_nome.sort(key=lambda x: x['nome'])

print('EXERCICIO 2', produtos_ordenados_por_nome)

'''EXERCICIO 3'''
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = copy.deepcopy(produtos)
produtos_ordenados_por_preco.sort(key=lambda x: x['preco'])

print('EXERCICIO 3', produtos_ordenados_por_preco)

print('LISTA ORIGINAL', produtos)

for p in produtos:
    print(*p)