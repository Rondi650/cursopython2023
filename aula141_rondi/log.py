# Abstracao
import os
from pathlib import Path

os.system('cls')

LOG_FILE =Path(__file__).parent / 'log.txt'
print(LOG_FILE)


class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o metodo log')
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_success(self, msg):
        return self._log(f'Success: {msg}')
    
    
class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})\n'
        with open(LOG_FILE, 'a', encoding='utf8') as arquivo:
            arquivo.write(msg_formatada)
    
    
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')
        
        
if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('teste')
    lp.log_success('teste')
    
    lf = LogFileMixin()
    lf.log_error('teste')
    lf.log_success('teste')
