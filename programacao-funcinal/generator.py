def cores_arco_iris():
    yield "vermelho"
    yield "laranja"
    yield "amarelo"
    yield "verde"
    yield "azul"


def sequencia():
    s = -1
    while True:
        s+= 1
        yield s


if __name__ == "__main__":
    generator = cores_arco_iris()
    print(type(generator))

    for cor in generator:
        print(cor)

    generator_n = sequencia()

    for n in generator_n:
        print(n)