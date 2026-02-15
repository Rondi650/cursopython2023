import os
from time import sleep
from threading import Thread

os.system('cls')

class MinhaThread(Thread):
    def __init__(self, texto: str, tempo: int):
        self.texto = texto
        self.tempo = tempo
        
        super().__init__()
        
    def run(self):
        sleep(self.tempo)
        print(self.texto)
        
t1 = MinhaThread('ola 1',1)
t1.start()

t2 = MinhaThread('ola 2',2)
t2.start()

t3 = MinhaThread('ola 3',3)
t3.start()

for i in range(10):
    print(i)
    sleep(0.5)