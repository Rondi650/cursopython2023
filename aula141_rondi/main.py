from log import LogFileMixin, LogPrintMixin
from eletronico import Smartphone

# lp = LogPrintMixin()
# lp.log_error('teste')
# lp.log_success('teste')

# lf = LogFileMixin()
# lf.log_error('teste')
# lf.log_success('teste')

galaxy_s = Smartphone('Galaxy S')
iphone = Smartphone('iPhone')

galaxy_s.ligar()
print(galaxy_s.ligado)
galaxy_s.desligar()
print(galaxy_s.ligado)

iphone.ligar()
print(iphone.ligado)
iphone.desligar()
print(iphone.ligado)




