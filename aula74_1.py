
# def externa1(a):
#     def interna(b):
#         return f'{a} {b}'
#     return interna('Dia')

# passo1_1 = externa1('Bom')
# # passo2 = passo1('Dia')

# print(passo1_1)

# print()

from rich import print

def externa2(a):
    def interna(b):
        return f'{a} {b}'
    return interna

passo1_2 = externa2('Bom')
print(externa2.__code__.co_varnames)
print(externa2.__code__.co_freevars)
print(externa2.__code__.co_cellvars)
print(externa2.__closure__)

print()

passo2_2 = passo1_2('Dia')
print(passo1_2.__code__.co_varnames)
print(passo1_2.__code__.co_freevars)
print(passo1_2.__code__.co_cellvars)
print(dir(passo1_2.__closure__))
print(passo1_2.__closure__.__subclasshook__)
print(passo1_2.__closure__.__repr__())