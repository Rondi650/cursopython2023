from collections.abc import Callable

# Exercício - Adiando execução de funções
def soma(x: int, y: int) -> int:
    return x + y


def multiplica(x: int, y: int):
    return x * y


def criar_funcao(funcao: Callable[[int,int], int], y: int) -> Callable[[int], int]:
    def func_auxiliar(x: int) -> int:
        return funcao(x,y)
    return func_auxiliar


teste = criar_funcao(multiplica, 5)
print(teste(2))
print(teste(10))
