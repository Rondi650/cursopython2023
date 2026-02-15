from concurrent.futures import ProcessPoolExecutor, as_completed
import subprocess
from pathlib import Path
import time
import os


MAX_WORKERS = 5
TIMEOUT_SCRIPT = 20  # segundos

DIRETORIO_SAIDAS = Path(__file__).parent / 'arquivos_txt'
os.makedirs(DIRETORIO_SAIDAS, exist_ok=True)

with open(DIRETORIO_SAIDAS / 'arquivos_python_principais.txt', 'r', encoding='utf-8') as arquivo_entrada:
    caminhos_scripts = arquivo_entrada.read().split('\n')

def executar_script(caminho_script: str) -> dict:
    inicio = time.perf_counter()

    try:
        resultado = subprocess.run(
            ['python', caminho_script],
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SCRIPT
        )

        duracao = time.perf_counter() - inicio

        return {
            "script": caminho_script,
            "returncode": resultado.returncode,
            "stdout": resultado.stdout,
            "stderr": resultado.stderr,
            "duracao": duracao,
            "erro": None,
        }

    except subprocess.TimeoutExpired:
        return {
            "script": caminho_script,
            "returncode": None,
            "stdout": "",
            "stderr": "",
            "duracao": TIMEOUT_SCRIPT,
            "erro": "Timeout",
        }

    except Exception as e:
        return {
            "script": caminho_script,
            "returncode": None,
            "stdout": "",
            "stderr": "",
            "duracao": 0,
            "erro": str(e),
        }


def main(caminhos_scripts: list[str]) -> None:
    inicio_total = time.perf_counter()

    sucesso = 0
    falhas = 0

    with ProcessPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {}

        for caminho in caminhos_scripts:
            future = executor.submit(executar_script, caminho.strip())
            futures[future] = caminho

        for future in as_completed(futures):
            resultado = future.result()
            print(resultado)

            if resultado["erro"]:
                print(f"❌ {resultado['script']} | ERRO: {resultado['erro']}")
                falhas += 1

            elif resultado["returncode"] != 0:
                print(f"⚠ {resultado['script']} | Código: {resultado['returncode']}")
                falhas += 1

            else:
                print(f"✔ {resultado['script']} | {resultado['duracao']:.2f}s")
                sucesso += 1

    tempo_total = time.perf_counter() - inicio_total

    print("\n===== RELATÓRIO FINAL =====")
    print(f"Sucesso: {sucesso}")
    print(f"Falhas : {falhas}")
    print(f"Tempo total: {tempo_total:.2f}s")


if __name__ == "__main__":
    main(caminhos_scripts)
