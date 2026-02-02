from abc import ABC
from contas import ContaCorrente, ContaPoupanca


class Pessoa():
    def __init__(self, nome: str, idade: int) -> None:
        self._nome = nome
        self._idade = idade

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._idade = valor

    @property
    def idade(self) -> int:
        return self._idade

    @idade.setter
    def idade(self, valor):
        self._idade = valor


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
