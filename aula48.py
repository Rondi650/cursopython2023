"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
# lista_a = ['Luiz', 'Maria', 1, True, 1.2]
# lista_b = lista_a.copy()

# lista_a[0] = 'Qualquer coisa'
# print(lista_a)
# print(lista_b)


# lista_a = ['Luiz', 'Maria', 1, True, 1.2]
# lista_a.pop(0)
# del lista_a[0]
# print(lista_a)
# removido = lista_a.pop()
# print(lista_a, removido)
# lista_a.insert(100, 123)
# print(lista_a)

nome = 'rondi'
outra_variavel = nome
nome = 'samara'
print(nome)
print(outra_variavel)

lista1 = ['original', 'original']
lista1[0] = 'ori'
lista_beta = lista1
lista1 = ['copia', 'copia']
lista1[0] = 'cop'
print(lista1)
print(lista_beta)

lista_a = ['rondi', 'samara']
listab = lista_a.copy()
# lista_a = ['pedro', 'joao']
lista_a[0] = 'heitor'

print(listab)