"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))


nome = "Alice"
idade = 30
mensagem_percent = "Olá, %s! Você tem %d anos." % (nome, idade)
print(mensagem_percent) # Saída: Olá, Alice! Você tem 30 anos.

nome = "Alice"
idade = 30
print(f'Ola {nome:^30s}, voce tem {str(idade):s} anos')

nome1 = "Ana"
nome2 = "Leonardo"
nome3 = 'Maximilianus' 

# Alinha à esquerda ocupando 10 espaços
print(f"Nome: {nome1:10s} | Fim")
print(f"Nome: {nome2:10s} | Fim")
print(f"Nome: {nome3:10.10s} | Fim")

teste = "Paralelepipedo"[0:10]
print(teste)