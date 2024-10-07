def soma_n(*numeros):
    soma = 0
    for n in numeros:
        soma+=n
    return soma


if __name__ == "__main__":
    print(soma_n(1,2,3,4,5))
    numeros = (1,2,3,4,5)

    print(soma_n(*numeros))