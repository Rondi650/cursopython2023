# ZIP - Compactando / Descompactando arquivos com zipfile.ZipFile
import os
import shutil
from pathlib import Path
from zipfile import ZipFile

os.system('cls')

# Caminhos
CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_ZIP_DIR = CAMINHO_RAIZ / 'aula186_diretorio_zip'
CAMINHO_COMPACTADO = CAMINHO_RAIZ / 'aula186_compactado.zip'
CAMINHO_DESCOMPACTADO = CAMINHO_RAIZ / 'aula186_descompactado'

shutil.rmtree(CAMINHO_ZIP_DIR, ignore_errors=True)
Path.unlink(CAMINHO_COMPACTADO, missing_ok=True)
shutil.rmtree(str(CAMINHO_COMPACTADO).replace('.zip', ''), ignore_errors=True)
shutil.rmtree(CAMINHO_DESCOMPACTADO, ignore_errors=True)

# raise Exception()

# Cria o diretório para a aula
CAMINHO_ZIP_DIR.mkdir(exist_ok=True)

def criar_arquivos(qtd: int, zip_dir: Path):
    for i in range(1, qtd+1):
        texto = f'arquivo_{i}'
        with open(zip_dir / f'{texto}.txt', 'w') as arquivo:
            arquivo.write(texto)


criar_arquivos(20, CAMINHO_ZIP_DIR)

# Criando um zip e adicionando arquivos
with ZipFile(CAMINHO_COMPACTADO, 'w') as zip:
    for root, dirs, files in os.walk(CAMINHO_ZIP_DIR):
        for file in files:
            zip.write(filename=os.path.join(root, file), arcname=file)
            
with ZipFile(CAMINHO_COMPACTADO, 'w') as zip:           
    for file in os.listdir(CAMINHO_ZIP_DIR):
        zip.write(filename=os.path.join(os.path.abspath(CAMINHO_ZIP_DIR), file),
                  arcname=file)

# Lendo arquivos de um zip
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

# Extraindo arquivos de um zip
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    zip.extractall(CAMINHO_DESCOMPACTADO)
