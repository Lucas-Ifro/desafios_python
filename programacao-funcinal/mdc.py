def mdc2(lista):
    divisor = min(lista)
    dividiu = False

    for divisor_atual in reversed(list(range(1, divisor + 1))):
        if dividiu:
            divisor = divisor_atual + 1
            break
        dividiu = True
        for numero in lista:
            if numero % divisor_atual > 0:
                dividiu = False

    return divisor


def mdc(lista):
    def calc(divisor):
        return divisor if sum(map(lambda x: x % divisor, lista))  == 0 else calc(divisor - 1)
    return calc(min(lista))
    

    

if __name__ == "__main__":
    print(mdc([21, 7]))
    print(mdc([125, 40]))
    print(mdc([9, 564, 66, 3]))
    print(mdc([55, 22]))
    print(mdc([15, 150]))
