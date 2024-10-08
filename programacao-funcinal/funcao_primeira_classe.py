def doblo(x):
    return x * 2


def quadrado(x):
    return x ** 2


if __name__ == "__main__":
    funcs = [doblo, quadrado] * 5
    for func, numero in zip(funcs, range(1,10)):
        print(f"O {func.__name__} de {numero} é {func(numero)}")