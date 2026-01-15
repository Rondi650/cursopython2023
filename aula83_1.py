
def func(*args, **kwargs):
    return args, kwargs


retorno = func(1,2,3, 
               [1,2,3], 
               'rondi', 
               35, 
               True,
               None,
               {'nome': 'samara', 'idade': 29}, 
               {'nome': 'joana', 'idade': 18},
               nome='joao', idade=30, 
               )
for dado in retorno:
    print(dado)
    for i in dado:
        print(i)
        