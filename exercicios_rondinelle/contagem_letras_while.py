import os
os.system('cls')

texto = 'Me chamo Rondinelle e tenho 35 anos' 

i: int = 0
string_incial: str = ''
valor_inicial: int = 0

while i < len(texto):
    letra = texto[i]
    
    contador = texto.count(letra)
    
    if letra == ' ':
        letra = 'Vazio'
    
    if valor_inicial <= contador:
        valor_inicial = contador
        string_incial = letra
    
    i += 1
    
print(valor_inicial, string_incial)