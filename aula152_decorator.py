import os

os.system('cls')

def decorador(metodo):
    def logs_func(a,b):
        return metodo(a,b)
    print('depois')
    return logs_func
        


@decorador
def soma(a,b):
    return a + b


print(soma(5,5))