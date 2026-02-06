from hmac import new
import os
import shutil

os.system('cls')

PATH = os.path.expanduser('~')
DESKTOP = os.path.join(PATH, 'Desktop')
EXEMPLO = os.path.join(DESKTOP, 'EXEMPLO')
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')

os.makedirs(NOVA_PASTA, exist_ok=True)

for arquivo in os.listdir(NOVA_PASTA):
    old_ = os.path.join(EXEMPLO, arquivo)
    new_ = os.path.join(NOVA_PASTA, arquivo)
    shutil.copy(new_, old_)