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

str_meses = reduce(
    lambda str, meses: f'{str}\n- {meses}', meses_com_31, 'Meses com 31 dias: ')
print(str_meses)


def mes_com_31(mes): return mdays[mes] == 31

def get_nome_mes(mes): return month_name[mes]

def juntar_meses(todos, nomes_mes): return f'{todos}\n- {nomes_mes}'

print(
    reduce(
        juntar_meses, 
             map(get_nome_mes, 
                 filter(mes_com_31, range(1,13))
                 ),
            'Meses com 31 dias: ')
        )