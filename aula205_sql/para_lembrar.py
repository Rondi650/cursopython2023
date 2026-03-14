def lista_de_compras(*itens):
    print(f"Tipo do objeto: {type(itens)}")
    print(itens)

lista_de_compras("Maçã", "Pão", "Leite", "Café", 1, bool, None, [], {}, ())
# Aqui, todos os nomes viraram uma única tupla 'itens'


def criar_perfil(nome, **informacoes_extras):
    print(f"Usuário: {nome}")
    
    # O 'informacoes_extras' virou um dicionário comum aqui dentro
    for chave, valor in informacoes_extras.items():
        print(f"- {chave.capitalize()}: {valor}")

# --- Chamando a função de formas diferentes ---

# 1. Com apenas o argumento obrigatório
criar_perfil("Alice")

print("-" * 20)

# 2. Passando argumentos nomeados extras (eles serão empacotados)
criar_perfil("Bruno", idade=25, cidade="São Paulo", profissao="Dev")

print("-" * 20)

# 3. Usando um dicionário existente e desempacotando com **
dados = {"hobby": "Guitarra", "clima": "Frio"}
criar_perfil("Carla", **dados)