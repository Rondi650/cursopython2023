"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',')

lista_frases: list[str] = []
for frase in lista_frases_cruas:
    frase_ajustada = frase.strip()
    lista_frases.append(frase_ajustada)
print(lista_frases)

# print(lista_frases_cruas)
# print(lista_frases)
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)
