# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import os
import json
from rich import print

os.system('cls')

PATH = 'C:\\Users\\rondi\\Desktop\\PROGRAMACAO\\PYTHON\\CURSO_OTAVIO_MIRANDA_COMPLETO\\cursopython2023\\exercicios_rondinelle\\classe_para_json\\'
ARQUIVO = 'dados_classe.json'
 
class Pessoa:
    lista = []
    
    def __init__(self, nome, idade, trabalhando=False) -> None:
        self.nome = nome
        self.idade = idade
        self.trabalhando = trabalhando
        Pessoa.lista.append({'nome': self.nome,'idade': self.idade,'trabalhando': self.trabalhando})
    
    def salvar_json(self):
        arquivo = Pessoa.lista
        
        with open(file= PATH + ARQUIVO, mode= 'w', encoding='utf8') as dados:
            json.dump(arquivo, dados, ensure_ascii=False, indent=3)
            
    def listar_json(self):
        with open(file= PATH + ARQUIVO, mode= 'r', encoding='utf8') as dados:
            return json.load(dados)
     
p1 = Pessoa('rondi', 35, True)
p2 = Pessoa('samara', 29)
p3 = Pessoa('heitor', 8)
p1.salvar_json()

retorno = p1.listar_json()
print(retorno)

Pessoa.lista.clear()
for x in retorno:
    Pessoa(**x)
print(Pessoa.lista)

