from datetime import datetime, timedelta
from locale import setlocale, LC_ALL
from calendar import mdays

data = datetime(2019,4,20,10,53,20)
print(data)
print(data.strftime('%d/%m/%Y %H:%M:%S'))

datat = datetime.strptime('20/04/2019', '%d/%m/%Y')
print(datat)
print(datat.timestamp())

datat1 = datetime.timestamp(123213123123)
print(datat1)

data2 = datetime.strptime('20/04/1923', '%d/%m/%Y')
data2 = data2 + timedelta(day=5)
print(data2.strftime('%d/%m/%Y'))

dif = data - datat
print(dif.total_seconds())
print(dif.days)


print(data.time())






setlocale(LC_ALL, '')
setlocale(LC_ALL, 'pt_BR.utf-8')

dt = datetime.now()
mes_atual = int(dt.strftime('%m'))
ultimo_dia_mes = mdays[mes_atual]

# sábado, 13 de julho de 2019
formatacao1 = dt.strftime('%A, %d de %B de %Y')
# 13/07/2019 11:21:20
formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')

print(formatacao1, formatacao2)
print(mes_atual, mdays[mes_atual])
