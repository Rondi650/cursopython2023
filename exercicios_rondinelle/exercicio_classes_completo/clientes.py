from abc import ABC, abstractmethod
from contas import ContaCorrente, ContaPoupanca

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, idade: int) -> None:
        self._nome = nome
        self._idade = idade
        
    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def idade(self) -> int:
        return self._idade
        
    
class Cliente(Pessoa):
    # contas: list[ContaCorrente | ContaPoupanca] = []
    
    def __init__(self,
                 nome: str, 
                 idade: int, 
                 conta: ContaCorrente | ContaPoupanca) -> None:
        super().__init__(nome, idade)
        self._conta = conta
        # Cliente.contas.append(self._conta)
        
    @property
    def conta(self) -> ContaCorrente | ContaPoupanca:
        return self._conta
        
    def __repr__(self) -> str:
        return f'Cliente: {self.nome} Idade:{self.idade} {self.conta}'
