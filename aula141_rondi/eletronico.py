from log import LogFileMixin, LogPrintMixin

class Eletronico:
    def __init__(self, nome) -> None:
        self._nome = nome
        self.ligado = False
        
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            
    def desligar(self):
        if self.ligado:
            self.ligado = False
            
class Smartphone(Eletronico, LogPrintMixin):
    def ligar(self):
        super().ligar()
        
        if self.ligado:
            lp = LogFileMixin()
            lp.log_success(f'Sucesso Total Totalissimo para o {self._nome}')
            self.log_success(f'Sucesso Total Totalissimo para o {self._nome}')
            
            
    def desligar(self):
        super().desligar()
        
        if not self.ligado:
           lp = LogFileMixin()
           lp.log_error(f'Sem sucesso nao total, nao totalissimo para o Galaxy S {self._nome}')
           self.log_error(f'Sem sucesso nao total, nao totalissimo para o Galaxy S {self._nome}')