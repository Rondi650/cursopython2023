# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

import os
from datetime import datetime
from dateutil.relativedelta import relativedelta

data_inicio = datetime(2020, 12, 20)
data_fim = data_inicio + relativedelta(years=5)
delta = relativedelta(data_fim, data_inicio)

os.system('cls')

emprestimo = 1000000
tempo = delta.years * 12
parcela = emprestimo / tempo
juros = 0.12

prazo = delta.years * 12

soma = 0

for data in range(1, prazo+1):
    data_parcela = (data_inicio + relativedelta(months=data)) - relativedelta(months=1)
    datas = datetime.strftime(data_parcela, '%d/%m/%Y')
    parcela_juros = parcela + (parcela * juros)
    soma += parcela_juros
    parcela_string = f'R${
        parcela_juros: ,.2f} '.replace(
        ',', '#').replace(
        '.', ',').replace(
        '#', '.')
    print(
        f'Data {
            datas.ljust(13)} | Parcela {
            str(data).ljust(6)} | Valor {
                parcela_string.ljust(5)}')
print(f'R${soma:,.2f}'.replace(',', '#').replace('.', ',').replace('#', '.'))
