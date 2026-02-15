from asyncio import as_completed
from concurrent.futures import ProcessPoolExecutor, as_completed
import subprocess
from pathlib import Path
import time
import os

os.system('cls')

DIRETORIO_SAIDAS = Path(__file__).parent / 'arquivos_txt'
os.makedirs(DIRETORIO_SAIDAS, exist_ok=True)

DIRETORIO_CURSO = r'C:\Users\rondi\Desktop\PROGRAMACAO\PYTHON\CURSO_OTAVIO_MIRANDA_COMPLETO\cursopython2023'

with open(DIRETORIO_SAIDAS / 'estrutura_completa_diretorios.txt', 'w', encoding='utf-8') as arquivo_saida:
    for caminho_atual, subdiretorios, arquivos in os.walk(DIRETORIO_CURSO):
        arquivo_saida.write(f'📁 Pasta atual: {caminho_atual}\n')

        for subdiretorio in subdiretorios:
            arquivo_saida.write(f'   📂 Subpasta: {subdiretorio}\n')

        for arquivo in arquivos:
            arquivo_saida.write(f'   📄 Arquivo: {arquivo}\n')

with open(DIRETORIO_SAIDAS / 'listagem_arquivos_python.txt', 'w', encoding='utf-8') as arquivo_saida:
    for caminho_atual, subdiretorios, arquivos in os.walk(DIRETORIO_CURSO):
        if 'venv' in subdiretorios:
            subdiretorios.remove('venv')
        if 'django' in subdiretorios:
            subdiretorios.remove('django')

        for arquivo in arquivos:
            if arquivo.endswith('.py'):
                arquivo_saida.write(f'{os.path.join(caminho_atual, arquivo)}\n')

arquivos_ignorados = ['aula119.py', 'aula194.py', 'aula15.py', 'aula16.py',
                      'aula20.py', 'aula196.py', 'aula22.py', 'aula24.py',
                      'aula28.py', 'aula29.py', 'aula32.py', 'aula34.py',
                      'aula40.py', 'aula47.py', 'aula54.py', 'aula63.py',
                      'aula77.py', 'aula79.py', 'aula196_1_threads.py']

contador_arquivos = 0
with open(DIRETORIO_SAIDAS / 'arquivos_python_principais.txt', 'w', encoding='utf-8') as arquivo_saida:
    for arquivo in os.listdir(DIRETORIO_CURSO):
        if arquivo.endswith(
                '.py') and arquivo not in arquivos_ignorados and contador_arquivos <= 200:
            arquivo_saida.write(f'{os.path.join(DIRETORIO_CURSO, arquivo)}\n')
            contador_arquivos += 1

with open(DIRETORIO_SAIDAS / 'arquivos_python_principais.txt', 'r', encoding='utf-8') as arquivo_entrada:
    caminhos_scripts = arquivo_entrada.read().split('\n')

'''
ASINCRONO FULL
'''

# tempo_inicio = time.time()
# processos_em_execucao: list[subprocess.Popen[bytes]] = []

# for indice, caminho_script in enumerate(caminhos_scripts):
#     print(caminho_script)
#     processo = subprocess.Popen(['python', caminho_script])
#     processos_em_execucao.append(processo)

# for processo in processos_em_execucao:
#     processo.wait()

# tempo_fim = time.time()

# print(f'Tempo total com Popen: {tempo_fim - tempo_inicio:.2f}s')


'''
SINCRONO
'''

# tempo_inicio = time.time()

# for indice, caminho_script in enumerate(caminhos_scripts):
#     print(f'Processo numero {indice}')
#     print(caminho_script)
#     processo = subprocess.run(['python', caminho_script])

# tempo_fim = time.time()

# print(f'Tempo total Sincrono: {tempo_fim - tempo_inicio:.2f}s')


'''
ASINCRONO COM CONTROLE DE EXECUCAO SUBMIT
'''

def executar_script_submit(caminho_script):
    subprocess.run(['python', caminho_script], capture_output=True)


if __name__ == '__main__':
    with open('saida_py2.txt', 'r', encoding='utf-8') as arquivo_entrada:
        caminhos_scripts = arquivo_entrada.read().split('\n')

    tempo_inicio = time.time()

    with ProcessPoolExecutor(max_workers=5) as executor:
        futures = []
        for caminho in caminhos_scripts:
            ex = executor.submit(executar_script_submit, caminho.strip())
            futures.append(ex)
            
        for future in as_completed(futures):
            future.result()

    tempo_fim = time.time()

    print(f'Tempo total com ProcessPoolExecutor: {tempo_fim - tempo_inicio:.2f}s')
  
    
'''
ASINCRONO COM CONTROLE DE EXECUCAO MAP
'''

# def executar_script_map(caminho_script):
#     subprocess.run(['python', caminho_script])

# if __name__ == '__main__':
#     tempo_inicio = time.time()

#     with ProcessPoolExecutor(max_workers=5) as executor:
#          executor.map(executar_script_map, caminhos_scripts)

#     tempo_fim = time.time()

#     print(f'Tempo total com ProcessPoolExecutor: {tempo_fim - tempo_inicio:.2f}s')