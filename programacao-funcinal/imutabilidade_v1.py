from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

setlocale(LC_ALL, 'pt-br')

meses_com_31 = map(
                lambda mes: month_name[mes], 
                filter(
                    lambda meses: mdays[meses] == 31, range(1,13)
                )
            )

print(list(meses_com_31))

str_meses = reduce(lambda str, meses: f'{str}\n- {meses}', list(meses_com_31), 'Meses com 31 dias: ')
print(str_meses)