"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
lista_a = [10, 2, 3, 40, 5, 6, 7]
lista_b = [1, 2, 3, 4]

tamanho = min(len(lista_a),len(lista_b))

lista = [i[0] + i[1] for i in zip(lista_a, lista_b)]
print(lista)

nova_lista = []
for i in range(tamanho):
    soma = lista_a[i] + lista_b[i]
    nova_lista.append(soma)
print(nova_lista)


for a,b in zip(lista_a, lista_b):
    print(a + b)
