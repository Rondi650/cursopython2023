"""
Higher Order Functions
Funções de primeira classe
"""


def saudacao1(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)


var1 = executa(saudacao1, 'Bom dia', 'Luiz')
var2 =executa(saudacao1, 'Boa noite', 'Maria')
print(var1)
print(var2)


prefixo = "Olá"

def saudacao(nome):
    global prefixo 
    prefixo = 'toma la da ca'
    return f"{prefixo}, {nome}!"

print(saudacao("Luiz"))  # usa prefixo do escopo global
