def executa(funcao, *args):
    return funcao(*args)

# def soma(x, y):
#     return x + y

# teste = executa(soma, 5,2 )
# print(f'teste: ', teste)


def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica


duplica = cria_multiplicador(2)
print('teste func: ', duplica(5))

duplica = executa(
    lambda m: lambda n: n * m,
    2
)
print('teste lambda: ', duplica(2))

# print(
#     executa(
#         lambda x, y: x + y,
#         2, 3
#     ),
# )

print(
    executa(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )
)


def nova_soma(*args):
    lista = list(args)
    return sum(lista)

print(nova_soma(1,2,3,5,2,5,2,5,2,5,2))


tupla = 1,2,3,5,2,5,2,5,2,5,2
print(*tupla)

# tupla com "resto" empacotado
a, *resto = 1, 2, 3, 4  # resto = [2, 3, 4]

# em listas
primeiro, *meio, ultimo = [10, 20, 30, 40]  # meio = [20, 30]

# ao construir coleções
nums = [1, 2, 3]
empacotado = [*nums, 4, 5]  # [1, 2, 3, 4, 5]

*teste, = (1, 2, 3)
print(teste)  # [1, 2, 3]