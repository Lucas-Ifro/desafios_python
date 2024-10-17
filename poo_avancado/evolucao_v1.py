class Humano:
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome
    
    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self


if __name__ == "__main__":
    jose = Humano('josé')
    grokn = Humano('grokn').das_cavernas()

    print(f'Humano.especie: {Humano.especie}')
    print(f"Humano.especie: {jose.especie}")
    print(f"Humano.especie: {grokn.especie}")