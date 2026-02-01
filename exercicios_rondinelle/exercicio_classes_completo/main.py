import os
from clientes import Cliente
from contas import ContaCorrente, ContaPoupanca
from bancos import Banco

os.system('cls')

conta1 = ContaCorrente('123', '456')
conta1.depositar(500)
conta1.depositar(300)
conta1.sacar(850)
conta1.sacar(50)
conta1.sacar(1)
cliente1 = Cliente('rondi', 35, conta1)
autentica = Banco(cliente1, conta1, conta1)
autentica.autenticacao()
print(cliente1)

print()

conta2 = ContaPoupanca('789', '321')
conta2.depositar(300)
conta2.sacar(400)
cliente1 = Cliente('samara', 29, conta2)
print(cliente1)