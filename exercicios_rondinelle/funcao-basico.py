
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

prefixo = "Olá"

'''SOBRE ESCOPO'''
def saudacao(nome):
    # Tenta LER prefixo ANTES de atribuir
    global prefixo
    resultado = f"{prefixo}, {nome}!"  # ❌ UnboundLocalError!
    prefixo = "Oi"  # Mas tem atribuição embaixo...
    return resultado

print(saudacao("Luiz"))
print(prefixo)
# ❌ UnboundLocalError: local variable 'prefixo' referenced before assignment