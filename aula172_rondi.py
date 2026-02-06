import os
from rich import print

os.system('cls')

str1 = 'basename'
str2 = 'dirname'
str3 = 'abspath'
str4 = 'join'


def formata(string: str):
    return string.upper().ljust(10)


path1 = os.path.basename(__file__)
path2 = os.path.dirname(__file__)
path3 = os.path.abspath(__file__)
path4 = os.path.join(path2, path1)

print(formata(str1), path1)
print(formata(str2), path2)
print(formata(str3), path3)
print(formata(str4), path4)

print(path3 == path4)
print(__file__)
print(__file__ == path3)

# for arquivo in os.listdir(path2):
#     print(arquivo)

print('\n',os.path.split(path3),'\n', sep='')
diretorio, arquivo = os.path.split(path3)

print(f'Diretorio: {diretorio}')
print(f'Arquivo: {arquivo}\n')

diretorio2, extensao = os.path.splitext(path3)
print(f'Diretorio: {diretorio2}')
print(f'Extensao: {extensao}\n')

print(type(os.path))
print(hasattr(os.path, 'exists'))
print(isinstance('exists', os))
