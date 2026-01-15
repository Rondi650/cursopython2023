# # dir, hasattr e getattr em Python
# from rich import print

# string = 'Luiz'
# metodo = 'strip'

# if hasattr(string, metodo):
#     print('Existe upper')
#     print(getattr(string, metodo)())
# else:
#     print('Não existe o método', metodo)
    

# # print(dir(str))

# nome = 'RONDINELLE OLIVEIRA'
# print(hasattr(nome, 'lower'))
# print(getattr(nome, 'lower')())


# # Confere antes de usar
# s = "Rondi"
# if hasattr(s, "upper"):
#     print(getattr(s, "upper")())  # "RONDI"

# # Usando valor padrão para evitar exceção
# print(getattr(s, "nao_existe", "fallback"))  # "fallback"

# # Sem fallback -> erro se não existir
# try:
#     getattr(s, "nao_existe")
# except AttributeError as e:
#     print("Erro:", e)

# Atributos em objetos customizados
# class Pessoa:
#     def __init__(self, nome): self.nome = nome
#     def saudacao(self): return f"Olá, {self.nome}"

# p = Pessoa("Ana")
# print(hasattr(p, "saudacao"))          # True
# print(getattr(p, "saudacao")())        # "Olá, Ana"
# print(dir(p))

class Pessoa:
    def __init__(self, nome): 
        self.nome = nome
    def saudacao(self): 
        return f"Olá, {self.nome}"

p = Pessoa("Ana")

# Use hasattr para conferir antes
if hasattr(p, "saudacao"):
    getattr(p, "saudacao")()  # "Olá, Ana"

resultado = getattr(p, "nao_existe", lambda:"padrão")
print(resultado())   

# Ou direto getattr com fallback
resultado = getattr(p, "saudacao", None)
if resultado:
    print(resultado())  # "Olá, Ana"
else:
    print("padrão")

# Evita exceção
try:
    getattr(p, "nao_existe")  # sem fallback -> erro
except AttributeError:
    print("Não existe")