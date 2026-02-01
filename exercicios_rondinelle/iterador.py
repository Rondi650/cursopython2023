class Contar():
    def __init__(self) -> None:
        self.numero = 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.numero <=3:
            cur = self.numero
            self.numero += 1
            return cur
        else:
            raise StopIteration

        
c1 = Contar()
print(c1.__next__())
print(c1.__next__())
print(c1.__next__())
print(c1.__next__())


c1 = Contar()
list(c1)


class Contar():
    def __init__(self) -> None:
        self.numero = 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.numero <=3:
            self.numero += 1
            return self.numero
        else:
            raise StopIteration

        
c1 = Contar()
print(c1.__next__())
print(c1.__next__())
print(c1.__next__())
print(c1.__next__())




def contar():
    numero = 1
    while numero <= 3:
        yield numero
        numero += 1
        
# for n in contar():
#     print(n)        
        
g = contar()

print(next(g))
print(next(g))
print(next(g))