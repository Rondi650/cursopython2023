"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os
os.system('cls')

lista = []

while True:
    selecao = input('Selecione uma opção\n\
    [I]nserir [A]pagar [L]istar: ').lower()
    
    if selecao not in 'ial':
        print('Operador de entrada invalido')
        continue
        
    if selecao == 'i':
        os.system('cls')
        valor = input('Digite o item a ser adicionado: ')
        lista.append(valor)
        print(f'Item {valor} adicionado com sucesso')
    elif selecao == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('Nada para listar')
        for item in enumerate(lista):
            indice, valor = item 
            print(indice, valor)
    else:
        apagar = input('Escolha o indice para apagar: ')
        try:
            apagar_int = int(apagar)
            lista.pop(apagar_int)
        except Exception as e:
            print(f'Erro: {e}')
            continue

