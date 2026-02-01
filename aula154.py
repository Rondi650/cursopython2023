# Classes decoradoras (Decorator classes)
from rich import print

class Multiplicar:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador

    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self._multiplicador
        return interna


@Multiplicar(100)
def soma(x, y):
    return x + y


dois_mais_quatro = soma(2, 4)
print(dois_mais_quatro)

print(Multiplicar.__dict__)
print(dir(Multiplicar))
