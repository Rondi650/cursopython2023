# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

def criar_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            e_string(arg)
        return func(*args, **kwargs)
    return interna


def inverte_string(*string):
    return (i[::-1] for i in string)


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string_checando_parametro('rondinelle','samara')
print(next(invertida))
print(next(invertida))
