# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True
# senha = input('Senha: ')
print(not True)  # False
print(not False)  # True

print('\n' + '#' * 50 + '\n')


class Dog:
    def __init__(self, name:str) -> None:
        self.name = name
        self.idade = 5

cachorro = Dog(name='Joao')
attribute_name = "name"

teste =  not isinstance(1,int) or not getattr(cachorro, 'name', False)
print(f'Teste de verdade: {teste}')

print(not 'joao')
