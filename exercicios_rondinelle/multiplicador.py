

def primeiro_numero(numero_base: int):
    def duplicar(fator: int):
        try:
            resultado = numero_base * fator
            if fator == 2:
                return f'O dobro de {numero_base} é {resultado}'
            elif fator == 3:
                return f'O triplo de {numero_base} é {resultado}'
            elif fator == 4:
                return f'O quadruplo de {numero_base} é {resultado}'
            else:
                return f'Numero invalido'
        except Exception as e:
            return f'Erro: {e}'
    return duplicar

number_multiplier = primeiro_numero(10)

dobro = number_multiplier(2)
triplo = number_multiplier(3)
quadruplo = number_multiplier(4)
quintuplo = number_multiplier(5)
resultado_nulo = number_multiplier(None)

print(dobro)
print(triplo)
print(quadruplo)
print(quintuplo)
print(resultado_nulo)


def saudacao(nome):
    def ola(ola):
        return f'{ola} {nome}'
    return ola

n1 = saudacao('Samara')
retorno = n1('Seja bem vindo')
print(retorno)