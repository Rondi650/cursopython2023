
def multiplicar(*args):
    base = 1
    for arg in args:
        base *= arg
    return base



def par_impar(retorno):
    if retorno % 2 == 0:
        return f' {retorno:,.0f} = Numero Par'
    return f' {retorno:,.0f} = Numero Impar'

teste = 5,5
multi = multiplicar(*teste)
retorno2 = par_impar(multi) 
print(retorno2)