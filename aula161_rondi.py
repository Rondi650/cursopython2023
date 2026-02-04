
class MyList():
    def __init__(self) -> None:
        self.data: dict[int, str] = {}
        self.indice: int = 0
        
    def append(self, valor: str) :
        self.data[self.indice] = valor
        self.indice += 1
        
    def __repr__(self) -> str:
        print(self.data)
        itens = []
        for chave, valor in self.data.items():
             itens.append(f'{chave}: {valor}')
        print(itens)
        return '\n'.join(itens)
        
lista = MyList()
lista.append('Rondi')
lista.append('Samara')
print(lista)
    