frase = 'eRondinelle Nunes de Oliveira seria o meu nome, tenho 35 anos de idade'

i = 0
qtd = 0
mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    print(letra_atual)
    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if qtd <= qtd_atual:
        qtd = qtd_atual
        mais_vezes = letra_atual

    i += 1

print(f'\nA letra que apareceu mais vezes foi "{mais_vezes}" que apareceu {qtd}x\n')
