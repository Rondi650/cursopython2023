
class Motor():
    def __init__(self, nome: float) -> None:
        self.nome = nome
        
    def __repr__(self) -> str:
        return str(self.nome)

class Fabricante():
    def __init__(self, nome: str) -> None:
        self.nome = nome
        
    def __repr__(self) -> str:
        return self.nome

class Carro():
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def fabricante(self) ->  Fabricante | None:
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor: Fabricante) -> None:
        self._fabricante = valor
         
    @property
    def motor(self) -> Motor | None:
        return self._motor
    
    @motor.setter
    def motor(self, valor: Motor) -> None:
        self._motor = valor
        
    def __repr__(self) -> str:
        return f'{self.nome} | {self.fabricante} | {self.motor}'

carro = Carro('Fusca')
motor = Motor(1.0)
fabricante = Fabricante('Volks')
carro.fabricante = fabricante
carro.motor = motor

print(carro)