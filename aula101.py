from collections.abc import Callable

# Exercício - Adiando execução de funções
def soma(x: int, y: int) -> int:
    return x + y


def multiplica(x: int, y: int) -> int:
    return x * y


def criar_funcao(funcao: Callable[[int, int], int], x: int) -> Callable[[int], int]:
    def interna(y: int) -> int:
        return funcao(x, y)
    return interna


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(10))
print(multiplica_por_dez(10))
