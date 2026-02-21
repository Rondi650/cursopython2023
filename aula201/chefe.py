# # chefe.py
import subprocess
import sys



print("[CHEFE]: Vou mandar o operário trabalhar.")

# O subprocess 'digita' no terminal: python operario.py "Limpar Sala"
subprocess.run([sys.executable, "operario.py", "Limpar Sala"])

print("[CHEFE]: O operário já terminou.")
