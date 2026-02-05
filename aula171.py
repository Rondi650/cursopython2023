# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
import os
from itertools import count

os.system('cls')

caminho = os.path.join('/Users', 'rondi', 'Desktop', 'PROGRAMACAO', 
                       'PYTHON', 'CURSO_OTAVIO_MIRANDA_COMPLETO', 
                       'cursopython2023', 'exercicios_rondinelle')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    for dir_ in dirs:
        print('  ', the_counter, 'Dir:', dir_)

    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        print('  ', the_counter, 'FILE:', caminho_completo_arquivo)
        # NÃO FAÇA ISSO (VAI APAGAR TUDO DA PASTA)
        # os.unlink(caminho_completo_arquivo)


path2 = 'G:\\Meu Drive\\Pessoal'

for arquivo in os.listdir(path2):
    print(arquivo)
    
# path3 = 'C:\Users\rondi\Desktop\PROGRAMACAO\PYTHON\
    # CURSO_OTAVIO_MIRANDA_COMPLETO\cursopython2023\aula6.py'