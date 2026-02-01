from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia: str, conta: str) -> None:
        self.agencia = agencia
        self.conta = conta
        self._saldo: float = 0
        
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor: int) -> None:
        self._saldo = valor
        
    def __repr__(self) -> str:
        return f'Ag:{self.agencia} Conta:{self.conta} Saldo:R${self.saldo}'
        
    def depositar(self, valor: float) -> float:
        print(f'Solicitado deposito de R${valor}')
        if valor < 0:
            raise ValueError('O deposito deve ser maior que 0')
        self._saldo += valor
        print(f'Novo saldo de R${self._saldo}')
        
        return self._saldo
        
    @abstractmethod
    def sacar(self, valor): 
        ...
    
    
class ContaCorrente(Conta):
    def sacar(self, valor):
        print(f'Solicitado novo saque de R${valor}')
        limite_conta = -100
        if (self.saldo - valor) <= 0 and (self.saldo - valor) >= limite_conta:
            print('Usando limite extra')
            
        elif (self.saldo - valor) < limite_conta:
            print('Sem Saldo ou limite especial disponivel')
            print(f'Voce tem disponivel para sacar R${self.saldo - limite_conta}')
            return
        
        self.saldo -= valor
        print(f'Saldo Restante Conta Corrente R${self.saldo}') 
        
    
class ContaPoupanca(Conta):
    def sacar(self, valor):
        print(f'Solicitado novo saque de R${valor}')
        if self.saldo <=0:
            print('Sem dinheiro na conta')
        elif valor > self.saldo:
            print(f'Voce pode sacar no maximo R${self.saldo}, voce solicitou R${valor}')    
            return
        
        self.saldo -= valor
        print(f'Saldo Restante Poupanca R${self.saldo}')   
