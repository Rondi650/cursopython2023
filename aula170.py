# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'
import os

# caminho = os.path.join('/Users', 'luizotavio', 'Desktop', 'EXEMPLO')

# for pasta in os.listdir(caminho):
#     caminho_completo_pasta = os.path.join(caminho, pasta)
#     print(pasta)

#     if not os.path.isdir(caminho_completo_pasta):
#         continue

#     for imagem in os.listdir(caminho_completo_pasta):
#         print('  ', imagem)

# path = 'G:\\Meu Drive\\Pessoal'
# if os.path.exists(path):
#     print("Acesso confirmado!")
#     print(os.listdir(path))  # Lista os arquivos da pasta

path2 = 'G:\\Meu Drive\\Pessoal'

for arquivo in os.listdir(path2):
    print(arquivo)

# if os.path.exists(path2):
#     os.startfile(path2) # Isso simula o duplo clique do mouse
