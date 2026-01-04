"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
from time import sleep
contador = 0

while contador <= 10:
    print(contador)
    contador +=1
    
    
# MINI EXERCICIO COM TIPAGEM

frase = 'Qual a letra que apareceu mais vezes nessa frase?'
dicionario: dict[str, int] = {}

for letra in frase:
    if letra not in dicionario:
        dicionario[letra] = 1
    else:
        dicionario[letra] += 1
        
print(dicionario)
for k,v in dicionario.items():
    print(k,v)

def fun(x: tuple[str, int]) -> int:
    return x[1] # ao acessar o colchete, estamos em outro tipo

mais_frequente = max(dicionario.items(), key=fun)
print('Mais frequente:', mais_frequente)

