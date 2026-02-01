from contas import Conta # agencia, conta
from clientes import Cliente # cliente

class Banco():
    def __init__(self, 
                 cliente: Cliente, 
                 agencia: Conta, 
                 conta: Conta) -> None:
        self.cliente = cliente
        self.agencia = agencia
        self.conta = conta
    
    def autenticacao(self):
        if isinstance(self.cliente, Cliente) \
        and isinstance(self.agencia, Conta) \
        and isinstance(self.conta, Conta):
            print('Autenticado')
        else:
            raise ValueError('Falha na autenticacao')
