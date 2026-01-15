# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
import pprint


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [
    numero * 2
    for numero in range(10)
]
# print(list(range(10)))
# print(lista)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]
print(*novos_produtos, sep='\n')

# print(novos_produtos)
print(novos_produtos)
p(novos_produtos)
lista = [n for n in range(10) if n < 5]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
]
p(novos_produtos)

numeros = [1, 2, 3, 4, 5]

# MAPEAMENTO - transforma
dobrados = [n * 2 for n in numeros]
print(dobrados)  # [2, 4, 6, 8, 10] - todos transformados

# FILTRO - seleciona
pares = [n for n in numeros if n % 2 == 0]
print(pares)  # [2, 4] - só os pares

# MAPEAMENTO + FILTRO - transforma E seleciona
dobrados_pares = [n * 2 for n in numeros if n % 2 == 0]
print(dobrados_pares)  # [4, 8] - pares transformados

lista_vazia = []
for n in numeros:
    if n % 2 == 0:
        lista_vazia.append(n*2)
print(lista_vazia)

print()

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
]

novos_produtos = []
for produto in produtos:
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10:
        if produto['preco'] > 20:
            novos_produtos.append({**produto, 'preco': produto['preco'] * 1.05})
        else:
            novos_produtos.append({**produto})
            
            
# ...existing code...

# ═══════════════════════════════════════════════════════════════════
# 📊 ANATOMIA DA LIST COMPREHENSION COMPLETA
# ═══════════════════════════════════════════════════════════════════

novos_produtos = [
    # ┌─────────────────────────────────────────────────────────────┐
    # │ 🎨 MAPEAMENTO (Expressão de Transformação)                  │
    # └─────────────────────────────────────────────────────────────┘
    {**produto, 'preco': produto['preco'] * 1.05}  # ← Valor quando TRUE
    
    # ┌─────────────────────────────────────────────────────────────┐
    # │ ⚖️  CONDICIONAL DE MAPEAMENTO (if...else)                   │
    # │    Define COMO transformar cada elemento                    │
    # └─────────────────────────────────────────────────────────────┘
    if produto['preco'] > 20  # ← Condição
    else {**produto}           # ← Valor quando FALSE
    
    # ┌─────────────────────────────────────────────────────────────┐
    # │ 🔄 ITERAÇÃO (Loop)                                          │
    # │    Percorre cada elemento da coleção                        │
    # └─────────────────────────────────────────────────────────────┘
    for produto in produtos
    
    # ┌─────────────────────────────────────────────────────────────┐
    # │ 🔍 FILTRO (if sem else)                                     │
    # │    Define QUAIS elementos serão processados                 │
    # └─────────────────────────────────────────────────────────────┘
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
]

# ═══════════════════════════════════════════════════════════════════
# 📝 ORDEM DE EXECUÇÃO:
# ═══════════════════════════════════════════════════════════════════
# 1️⃣  for produto in produtos         → Itera cada produto
# 2️⃣  if (produto['preco'] >= 20...)  → FILTRO: mantém ou descarta?
# 3️⃣  if produto['preco'] > 20        → MAPEAMENTO: qual transformação?
# 4️⃣  {**produto, 'preco': ...}       → Aplica a transformação
# ═══════════════════════════════════════════════════════════════════

print("Resultado:", novos_produtos)