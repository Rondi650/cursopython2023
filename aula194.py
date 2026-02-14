# Usando subprocess para executar e comandos externos
# subprocess é um módulo do Python para executar
# processos e comandos externos no seu programa.
# O método mais simples para atingir o objetivo é usando subprocess.run().
# Argumentos principais de subprocess.run():
# - stdout, stdin e stderr -> Redirecionam saída, entrada e erros
# - capture_output -> captura a saída e erro para uso posterior
# - text -> Se True, entradas e saídas serão tratadas como texto
# e automaticamente codificadas ou decodificadas com o conjunto
# de caracteres padrão da plataforma (geralmente UTF-8).
# - shell -> Se True, terá acesso ao shell do sistema. Ao usar
# shell (True), recomendo enviar o comando e os argumentos juntos.
# - executable -> pode ser usado para especificar o caminho
# do executável que iniciará o subprocesso.
# Retorno:
# stdout, stderr, returncode e args
# Importante: a codificação de caracteres do Windows pode ser
# diferente. Tente usar cp1252, cp852, cp850 (ou outros). Linux e
# mac, use utf_8.
# Comando de exemplo:
# Windows: ping 127.0.0.1
# Linux/Mac: ping 127.0.0.1 -c 4

# import sys

# # sys.platform = linux, linux2, darwin, win32

# cmd = ['ls -lah /']
# encoding = 'utf_8'
# system = sys.platform

# if system == "win32":
#     cmd = ['ping', '127.0.0.1']
#     encoding = 'cp850'


# proc = subprocess.run(
#     cmd, capture_output=True,
#     text=True, encoding=encoding,
#     shell=True,
# )

# print()

# # print(proc.args)
# # print(proc.stderr)
# print(proc.stdout)
# print(proc.returncode)

# import subprocess
# import os

# # Lista com os caminhos completos dos seus 10 scripts
# scripts = [
#     r'C:\Projetos\Automacao\script_vendas.py',
#     r'C:\Users\Admin\Documents\limpeza.py',
#     '/home/user/scripts/processamento.py',  # Exemplo Linux/Mac
#     # ... adicione os outros aqui
# ]

# processos = []

# for caminho in scripts:
#     # 'python' chama o interpretador; caminho é o arquivo
#     p = subprocess.Popen(['python', caminho])
#     processos.append(p)

# # Garante que o script principal espere todos os 10 terminarem
# for p in processos:
#     p.wait()

# print("Todos os 10 scripts foram executados com sucesso!")

from concurrent.futures import ProcessPoolExecutor
import subprocess
import time
import os

os.system('cls')

lista = [
    r'C:\Users\rondi\Desktop\PROGRAMACAO\PYTHON\CURSO_OTAVIO_MIRANDA_COMPLETO\cursopython2023\aula1.py',
    r'C:\Users\rondi\Desktop\PROGRAMACAO\PYTHON\CURSO_OTAVIO_MIRANDA_COMPLETO\cursopython2023\aula2.py',
    r'C:\Users\rondi\Desktop\PROGRAMACAO\PYTHON\CURSO_OTAVIO_MIRANDA_COMPLETO\cursopython2023\aula3.py',
    r'C:\Users\rondi\Desktop\PROGRAMACAO\PYTHON\CURSO_OTAVIO_MIRANDA_COMPLETO\cursopython2023\aula4.py',
    r'C:\Users\rondi\Desktop\PROGRAMACAO\PYTHON\CURSO_OTAVIO_MIRANDA_COMPLETO\cursopython2023\aula5.py',
    r'C:\Users\rondi\Desktop\PROGRAMACAO\PYTHON\CURSO_OTAVIO_MIRANDA_COMPLETO\cursopython2023\aula6.py',
    r'C:\Users\rondi\Desktop\PROGRAMACAO\PYTHON\CURSO_OTAVIO_MIRANDA_COMPLETO\cursopython2023\aula7.py',
    r'C:\Users\rondi\Desktop\PROGRAMACAO\PYTHON\CURSO_OTAVIO_MIRANDA_COMPLETO\cursopython2023\aula8.py',
    r'C:\Users\rondi\Desktop\PROGRAMACAO\PYTHON\CURSO_OTAVIO_MIRANDA_COMPLETO\cursopython2023\aula9.py',
    r'C:\Users\rondi\Desktop\PROGRAMACAO\PYTHON\CURSO_OTAVIO_MIRANDA_COMPLETO\cursopython2023\aula10.py',
]

PATH_ = r'C:\Users\rondi\Desktop\PROGRAMACAO\PYTHON\CURSO_OTAVIO_MIRANDA_COMPLETO\cursopython2023'

with open('saida.txt', 'w', encoding='utf-8') as f:
    for dirpath, dirnames, filenames in os.walk(PATH_):
        f.write(f'📁 Pasta atual: {dirpath}\n')

        for dirname in dirnames:
            f.write(f'   📂 Subpasta: {dirname}\n')

        for filename in filenames:
            f.write(f'   📄 Arquivo: {filename}\n')

with open('saida_py1.txt', 'w', encoding='utf-8') as f:
    for dirpath, dirnames, filenames in os.walk(PATH_):
        if 'venv' in dirnames:
            dirnames.remove('venv')
        if 'django' in dirnames:
            dirnames.remove('django')

        for filename in filenames:
            if filename.endswith('.py'):
                f.write(f'{os.path.join(dirpath, filename)}\n')

remover = ['aula119.py', 'aula194.py', 'aula15.py', 'aula16.py']

i = 0
with open('saida_py2.txt', 'w', encoding='utf-8') as f:
    for arquivo in os.listdir(PATH_):
        if arquivo.endswith('.py') and i <= 100 and arquivo not in remover:
            f.write(f'{os.path.join(PATH_, arquivo)}\n')
            i += 1

# inicio1 = time.time()
# processos: list[subprocess.Popen[bytes]] = []

# for i, caminho in enumerate(lista):
#     print(caminho)
#     p = subprocess.Popen(['python', caminho])
#     processos.append(p)

# for p in processos:
#     p.wait()

# fim1 = time.time()

# print('#' * 100)

def executar(caminho):
    subprocess.run(['python', caminho])
    
if __name__ == '__main__':
    with open('saida_py2.txt', 'r', encoding='utf-8') as f:
        lista = f.read().split('\n')

    inicio = time.time()
    
    with ProcessPoolExecutor(max_workers=5) as executor:
        executor.map(executar, lista)
        
    fim = time.time()
    
    print(f'Tempo total com ProcessPoolExecutor: {fim - inicio:.2f}s')
# print(f'Tempo total com Popen: {fim1 - inicio1:.2f}s')
