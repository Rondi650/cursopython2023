"""
Closure e funções que retornam outras funções
"""

from rich import print

def criar_saudacao(saudacao):
    def saudar(nome):
        print(f'local: ',locals())
        print()
        print(f'global: ',globals())
        return f'{saudacao}, {nome}!'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

teste = 'oi'

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))

# print(globals())
# print()
# print(locals())
# print()
print(dir())
print()
print(vars())

# print(dir(__builtins__))





# Escopo do módulo: Global (G)
var_global = "Estou no escopo global!"

def funcao_externa() -> None:
    # Escopo da função: Local (L) para esta função
    var_local = "Estou no escopo local!"

    # Busca de 'var_local':
    # O Python encontra 'var_local' no escopo Local (L).
    print(var_local)

    # Busca de 'var_global':
    # Não encontra 'var_global' no Local (L), então busca no Global (G).
    print(var_global)

    # Busca de 'print':
    # Não encontra 'print' em L ou G, então busca no Built-in (B).
    print(print) # Imprime a representação da própria função print


if __name__ == "__main__":
    funcao_externa()
    
# def = 10

# python -c "help('keywords')"

# Escopo global (G)

variavel = "global"

def funcao():
    # Tentativa de usar `variavel` (G)
    global variavel
    print(variavel) # <-- ISSO VAI GERAR O ERRO

    # Criei um novo nome `variavel` no escopo LOCAL (L)
    # Isso fez o nome `variavel` deixar de existir no print acima
    variavel = "local" # <-- ESSE É O MOTIVO DO ERRO

    # Agora, estamos tentando usar a `variavel` LOCAL
    print(variavel)

funcao() # <-- O interpretador não passa daqui
print(variavel)
# A `variavel` global original permanece inalterada


def soma_mais_um():
    # 'numero' está no escopo Enclosing para 'incrementa'
    numero = 0

    def incrementa():
        # 'nonlocal numero' informa que queremos modificar
        # o 'numero' do escopo Enclosing (soma_mais_um)
        numero = 1
        numero += 1
        print(f"Número atual (interno): {numero}")

    # Até aqui, nada alterado
    print(f"Número inicial (externo): {numero}")

    incrementa() # A alteração ocorre aqui
    print(f"Número final (externo): {numero}")

soma_mais_um()
# Saída esperada:
# Número inicial (externo): 0
# Número atual (interno): 1
# Número final (externo): 1



local = 0

def somar():
    global local
    local += 1
    return local