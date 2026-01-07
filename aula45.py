"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""


# for letra in texto
texto = 'Luiz'  # iterável

# iterador = iter(texto)  # iterator
iterador = texto.__iter__()  # iterator

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break

print()

for letra in texto:
    print(letra)

print()

texto = 'Rondi' # Iteravel
iterador = texto.__iter__()  # iterator
print(iterador.__next__())
print(iterador.__next__())
print(iterador.__next__())
print(iterador.__next__())
print(iterador.__next__())
print(iterador.__next__())

print()

texto = 'Luiz'  # iterável

# iterador = iter(texto)  # iterator
iterador = texto.__iter__()  # iterator

while True:
    print(next(iterador))
