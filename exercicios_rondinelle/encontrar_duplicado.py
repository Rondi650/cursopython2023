import os
os.system('cls')

"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros: list[list[int]] = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]


i = 0
def func(lista: list[int]) -> str:
    nova_lista: list[int | str] = []
    duplicado_encontrado: bool = False
    
    for numero in lista:
        if numero not in nova_lista:
            nova_lista.append(numero)
        else:
            if not duplicado_encontrado:
                variavel = f'>{numero}<'
                nova_lista.append(variavel)
                duplicado_encontrado = True
            else:
                nova_lista.append(numero)
    global i
    i += 1
    if not duplicado_encontrado:
        return f'Lista {i}: {nova_lista} <- Sem dados duplicados'
    else:
        return f'Lista {i}: {nova_lista}'

for lista in lista_de_listas_de_inteiros:
    print(func(lista))

print(func([5, 3, 1, 8, 5, 7, 1, 8, 8, 7]))
