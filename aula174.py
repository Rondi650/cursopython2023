# os + shutil - Apagando, copiando, movendo e renomeando pastas com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename
import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'EXEMPLO')
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')
NOVA_PASTA_EITA = os.path.join(DESKTOP, 'NOVA_PASTA_EITA')

# shutil.move(NOVA_PASTA_EITA, DESKTOP)
shutil.copytree(NOVA_PASTA, NOVA_PASTA_EITA)
# os.unlink(os.path.join(DESKTOP, 'NOVA_PASTA_EITA'))
# shutil.rmtree(os.path.join(DESKTOP, 'NOVA_PASTA_EITA'), ignore_errors=True)
# shutil.rmtree(NOVA_PASTA, ignore_errors=True)
# shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA, dirs_exist_ok=True)
# shutil.move(NOVA_PASTA, NOVA_PASTA + '_EITA')
# shutil.rmtree(PASTA_ORIGINAL, ignore_errors=True)


# os.makedirs(NOVA_PASTA, exist_ok=True)

# for root, dirs, files in os.walk(PASTA_ORIGINAL):
#     for dir_ in dirs:
#         caminnho_novo_diretorio = os.path.join(
#             root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
#         )
#         os.makedirs(caminnho_novo_diretorio, exist_ok=True)

#     for file in files:
#         caminho_arquivo = os.path.join(root, file)
#         caminnho_novo_arquivo = os.path.join(
#             root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
#         )
#         shutil.copy(caminho_arquivo, caminnho_novo_arquivo)
