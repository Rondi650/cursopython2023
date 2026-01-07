"""
Iterando strings com while
"""
#       012345678910
# nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321


nome = 'Rondinelle Oliveira'  # Iteráveis
i = 0
espaco = '*'

while i <= (len(nome)-1):
    letra = nome[i]
    espaco += letra + '*'
    i += 1
print(espaco)

