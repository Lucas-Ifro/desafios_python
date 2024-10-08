def multiplicar(x):
    def calcular(y):
        return x * y
    
    return calcular


if __name__ == "__main__":
    doblo = multiplicar(2)
    print(doblo(2))