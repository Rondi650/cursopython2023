# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))
from rich import print

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return


gen = generator(maximum=1000)
# for n in gen:
#     print(n)

# print(dir(gen))

sem_yield = [
    '__bool__',
    '__class__',
    '__delattr__',
    '__dir__',
    '__doc__',
    '__eq__',
    '__format__',
    '__ge__',
    '__getattribute__',
    '__getstate__',
    '__gt__',
    '__hash__',
    '__init__',
    '__init_subclass__',
    '__le__',
    '__lt__',
    '__ne__',
    '__new__',
    '__reduce__',
    '__reduce_ex__',
    '__repr__',
    '__setattr__',
    '__sizeof__',
    '__str__',
    '__subclasshook__'
]

com_yield = [
    '__class__',
    '__class_getitem__',
    '__del__',
    '__delattr__',
    '__dir__',
    '__doc__',
    '__eq__',
    '__format__',
    '__ge__',
    '__getattribute__',
    '__getstate__',
    '__gt__',
    '__hash__',
    '__init__',
    '__init_subclass__',
    '__iter__',
    '__le__',
    '__lt__',
    '__name__',
    '__ne__',
    '__new__',
    '__next__',
    '__qualname__',
    '__reduce__',
    '__reduce_ex__',
    '__repr__',
    '__setattr__',
    '__sizeof__',
    '__str__',
    '__subclasshook__',
    'close',
    'gi_code',
    'gi_frame',
    'gi_running',
    'gi_suspended',
    'gi_yieldfrom',
    'send',
    'throw'
]

print()
print(f'COM YIELD ', len(com_yield))
print(f'SEM YIELD ',len(sem_yield))
print()

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

set_com_yield = set(com_yield)
set_sem_yield = set(sem_yield)

com_yield_only_methods = set_com_yield - set_sem_yield
print('METODOS EXCLUSIVOS COM YIELD', com_yield_only_methods)
print(len(com_yield_only_methods))

sem_yield_only_methods = set_sem_yield - set_com_yield
print('METODOS EXCLUSIVOS SEM YIELD', sem_yield_only_methods)
print(len(sem_yield_only_methods))

print([n for n in com_yield if n.startswith('gi')])
