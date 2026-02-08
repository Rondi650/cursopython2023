# csv.writer e csv.DictWriter para escrever em CSV
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import random
import csv
import os
from pathlib import Path

os.system('cls')

CAMINHO_CSV = Path(__file__).parent / 'aula180.csv'

lista_clientes: list[dict[str, str]] = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]

with open(CAMINHO_CSV, 'w', encoding='utf8', newline='') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas
    )
    escritor.writeheader()

    for cliente in lista_clientes:
        print(cliente)
        escritor.writerow(cliente)


nomes = [
    'Ana',
    'Bruno',
    'Carlos',
    'Daniela',
    'Eduardo',
    'Fernanda',
    'Gabriel',
    'Helena']
sobrenomes = ['Silva', 'Souza', 'Oliveira', 'Pereira', 'Costa', 'Almeida', 'Santos']
ruas = ['Av Brasil', 'Rua das Flores', 'Av Central', 'Rua A', 'Rua B', 'Av Paulista']


def gerar_clientes(qtd: int) -> list[list[str]]:
    clientes = []

    for _ in range(qtd):
        nome = f"{random.choice(nomes)} {random.choice(sobrenomes)}"
        endereco = f"{random.choice(ruas)}, {random.randint(1, 200)}"
        clientes.append([nome, endereco])

    return clientes


gerar_lista: list[list[str]] = gerar_clientes(5)
print(gerar_lista)


lista_clientes_list: list[list[str]] = [
    ['Gabriel Santos', 'Rua das Flores, 17'],
    ['Bruno Costa', 'Av Central, 96'],
    ['Eduardo Pereira', 'Rua B, 34'],
    ['Daniela Santos', 'Rua B, 49'],
    ['Helena Silva', 'Av Paulista, 143']
]

with open(CAMINHO_CSV, 'w', encoding='utf8', newline='') as arquivo:
    nome_colunas = ['Nome', 'Endereço']
    escritor = csv.writer(arquivo)

    escritor.writerow(nome_colunas)

    for cliente in lista_clientes_list:
        escritor.writerow(cliente)
