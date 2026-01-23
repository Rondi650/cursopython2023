# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import os
import time
import json
os.system('cls')

lista = []
lista_reserva = []

PATH = "C:\\Users\\rondi\\Desktop\\PROGRAMACAO\\PYTHON\\CURSO_OTAVIO_MIRANDA_COMPLETO\\cursopython2023\\exercicios_rondinelle\\"

def sair(lista):
    lista.clear()
    os.system('cls')
    print('Saindo da aplicacao...')
    time.sleep(1)
    os.system('cls')
    
def limpar(lista):
    os.system('cls')
    lista.pop()
    salvar_dados(lista)
    

def salvar_dados(lista):
    with open(file=PATH + 'dados_salvos.json', mode='w', encoding='utf-8') as arquivo:
        retorno = json.dump(lista, arquivo, ensure_ascii=False, indent=4)
        return retorno
    
def listar_dados():
    with open(file=PATH+'dados_salvos.json', mode='r', encoding='utf-8') as arquivo:
        retorno = json.load(arquivo)
        return retorno

def main():
    while True:

        tarefa = input('\nLista de tarefas com desfazer e refazer\nInclua uma tarefa: ')
        
        if tarefa == 'desfazer':
            try:
                desfazer = lista.pop()
                salvar_dados(lista)
                lista_reserva.append(desfazer)
            except IndexError:
                ...
        elif tarefa == 'refazer':
            try:
                recarregar = lista_reserva[-1]
                lista.append(recarregar)
                salvar_dados(lista)
                lista_reserva.pop()
            except IndexError:
                ...
        else:
            lista.append(tarefa)
            salvar_dados(lista)
        
        if tarefa == 'limpar':
            limpar(lista)
            
            continue
        if tarefa == 'sair':
            sair(lista)
            break
        else:
            print()
            print(listar_dados())
            for item in lista:
                print(item)


if __name__ == '__main__':
    main()
