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
os.system('cls')

lista = []
lista_reserva = []


def sair(lista):
    lista.clear()
    os.system('cls')
    print('Saindo da aplicacao...')
    time.sleep(1)
    os.system('cls')
    
def limpar():
    os.system('cls')
    lista.pop()

def main():
    while True:

        tarefa = input('\nLista de tarefas com desfazer e refazer\nInclua uma tarefa: ')
        
        if tarefa == 'desfazer':
            try:
                desfazer = lista.pop()
                lista_reserva.append(desfazer)
            except IndexError:
                ...
        elif tarefa == 'refazer':
            try:
                recarregar = lista_reserva[-1]
                lista.append(recarregar)
                lista_reserva.pop()
            except IndexError:
                ...
        else:
            lista.append(tarefa)
        
        if tarefa == 'limpar':
            limpar()
            continue
        if tarefa == 'sair':
            sair(lista)
            break
        else:
            print()
            for item in lista:
                print(item)


if __name__ == '__main__':
    main()