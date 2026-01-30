# Funções decoradoras e decoradores com métodos
from typing import Callable

def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr


def adiciona_repr(cls):
    cls.__repr__ = meu_repr
    return cls


def meu_planeta(metodo: Callable):
    print('ID da função ORIGINAL (metodo):', id(metodo)) # 68

    def interno(*args, **kwargs):
        print('ID da função INTERNO (antes de retornar):', id(interno)) # 28
        print('ID da função ORIGINAL chamada de dentro:', id(metodo)) # 68
        return metodo(*args, **kwargs)

    print('ID da função INTERNO (retornada):', id(interno)) # 28
    return interno


@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome


@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @meu_planeta
    def falar_nome(self): # 28
        return f'O planeta é {self.nome}'


brasil = Time('Brasil')
portugal = Time('Portugal')

# terra = Planeta('Terra')
marte = Planeta('Marte')

# print(brasil)
# print(portugal)

# print(terra)
# print(marte)

# print(terra.falar_nome())
print(marte.falar_nome())
