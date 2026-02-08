from pathlib import Path
import os

os.system('cls')

caminho = Path(__file__)
caminho_os = os.path.abspath('')

print(caminho.absolute())
print(caminho.parent.parent)
print(caminho_os)
novo_caminho = caminho / 'teste'
print(novo_caminho)
arquivop = caminho.home() / 'Desktop' /'teste.txt'
arquivop.touch()
arquivop.mkdir()
arquivop.glob



 


# class CaminhoDivertido:
#     def __init__(self, caminho):
#         # Normaliza o caminho para o formato do Sistema Operacional atual
#         self.caminho = os.path.normpath(caminho)

#     def _fazer_novo_caminho(self, base, novo):
#         # A função os.path.join é a "mágica" por trás do pathlib.
#         # Ela sabe que:
#         # 1. Se 'novo' for uma string, junta com a 'base'.
#         # 2. Se 'novo' for outro objeto CaminhoDivertido, pega a string dele.
        
#         if isinstance(novo, CaminhoDivertido):
#             novo = novo.caminho
            
#         uniao = os.path.join(str(base), str(novo))
#         return CaminhoDivertido(uniao)

#     def __truediv__(self, outro):
#         return self._fazer_novo_caminho(self.caminho, outro)

#     def __repr__(self):
#         return f"CaminhoDivertido('{self.caminho}')"

# # --- Testando ---
# base = CaminhoDivertido("/home/usuario")
# completo = base / "downloads" / "foto.png"

# print(completo) 
# No Linux: CaminhoDivertido('/home/usuario/downloads/foto.png')
# No Windows: CaminhoDivertido('\home\usuario\downloads\foto.png')