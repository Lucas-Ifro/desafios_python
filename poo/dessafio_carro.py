class Carro:
    velocidade = 0
    velocidade_max = 0

    def __init__(self, velocidade_max):
        self.velocidade_max = velocidade_max

    
    def acelerar(self, delta):
        self.velocidade += delta if self.velocidade + delta <= self.velocidade_max else delta - ((self.velocidade + delta) - self.velocidade_max)
        return self.velocidade

    def frear(self, delta = 5):
        self.velocidade -= delta if self.velocidade >= delta and 0 < delta  else 0
        return self.velocidade

if __name__ == "__main__":
    c1 = Carro(180)

    for _ in range(25):
        print(c1.acelerar(8))

    for _ in range(10):
        print(c1.frear(delta=20))