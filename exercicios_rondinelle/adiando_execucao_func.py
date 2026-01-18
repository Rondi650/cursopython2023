# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, y):
    def func_auxiliar(x):
        return funcao(x,y)
    return func_auxiliar


teste = criar_funcao(multiplica, 5)
print(teste(2))
print(teste(10))
