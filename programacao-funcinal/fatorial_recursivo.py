from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

setlocale(LC_ALL, 'pt_BR')

def meses_com_31(lista):
    return reduce( lambda str, mes: str + f'- {mes}\n',map(
                lambda mes: month_name[mes], 
                    filter(
                        lambda l: mdays[l] == 31, lista
                        )
                    )
                , "Meses com 31 dias:\n")

def fatorial(n):
    return n * fatorial(n - 1) if n > 1 else 1


def divide(lista, divisor):
    return reduce(lambda soma, n: soma + n % divisor, lista, 0)


def mdc(lista):
    divisor = min(lista)
    divisores = filter(lambda n: divide(lista,n) == 0, range(1, divisor + 1))
    return max(divisores)


if __name__ == "__main__":
    print(f'10! = {fatorial(0)}')
    print(meses_com_31(range(1,13)))
    print(mdc([5,10]))