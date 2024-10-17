from abc import ABCMeta, abstractproperty


class Humano(metaclass=ABCMeta):
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    @property
    def idade(self):
        return self._idade
    
    @property
    def inteligente(self):
        raise NotImplementedError()
    
    @idade.setter
    def idade(self, valor):
        if valor > 0 :
            self._idade = valor 
        else:
            raise ValueError("idade deve ser maior que zero")
    
    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self
    
    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopteco', ) + tuple(f'Homo {adj}' for adj in adjetivos)


    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]

class Neanderthal(Humano):
    especie = Humano.especies()[-2]

    @property
    def inteligente(self):
        return False


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

    @property
    def inteligente(self):
        return True



if __name__ == "__main__":
    jose = HomoSapiens('josé')
    jose.idade = 40
    grokn = Neanderthal('grokn')

    try:
        print(jose.inteligente)
        print(grokn.inteligente)
    except NotImplementedError:
        print("propriedade abstrata")

    

    print(f'Evolução (a partir das classe): {", ".join(HomoSapiens.especies())}')
    print(f'Evolução (a partir das instancia): {", ".join(jose.especies())}')
    print(f'Homo Sapiens evoluido? {HomoSapiens.is_evoluido()}')
    print(f'Neanderthal evoluido? {Neanderthal.is_evoluido()}')

