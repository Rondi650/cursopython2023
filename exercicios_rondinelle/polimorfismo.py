import os
from abc import abstractmethod, ABC

os.system('cls')

class Notificacao(ABC):
    def __init__(self, mensagem: str) -> None:
        self.mensagem = mensagem
        
    @abstractmethod
    def enviar(self) -> str:  
        ...
    
    
class NotificacaoEmail(Notificacao):
    def enviar(self):
        return f'EMAIL - {self.mensagem}'
    
    
class NotificacaoSMS(Notificacao):
    def enviar(self):
        return f'SMS - {self.mensagem}'
        
        
email = NotificacaoSMS('bom dia')
retorno = email.enviar()
print(retorno)
# sms = NotificacaoSMS('bom dia')