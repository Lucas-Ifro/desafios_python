class Potencia:
    def __init__(self, expoente):
        self.expoente = expoente

    def __call__(self, base,*args, **kwds):
        return base ** self.expoente
    

if __name__ == "__main__":
    quadrado = Potencia(5)
    print(quadrado(2))