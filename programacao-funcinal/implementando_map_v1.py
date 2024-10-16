def mapear(funcao, lista):
    for n in lista:
        yield funcao(n)


def mapear2(funcao, lista):
    return (funcao(elemento) for elemento in lista)


if __name__ == "__main__":
    print(list(mapear(lambda x: x ** 2, [2,3,4])))
    print(list(mapear2(lambda x: x ** 2, [2,3,4])))