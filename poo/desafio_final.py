from datetime import datetime, timedelta
from functools import reduce

class Pessoa:
    def __init__(self,nome,idade):
        self.idade = idade
        self.nome = nome


    def isAdult(self):
        return self.idade >= 18
    

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"
    

class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario=1400):
        super().__init__(nome, idade)
        self.salario = salario
    

class Cliente(Pessoa):
    
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []
    
    def registrar_compra(self, compra):
        self.compras.append(compra)

    
    def get_data_ultima_compra(self):
        if len(self.compras) >= 1:
            return self.compras[len(self.compras)-1].data
        else:
            return "Não a compras"
        

    def total_compras(self):
        return reduce(lambda total, compra: total + compra.valor, self.compras, 0)
    

class Compra:
    def __init__(self, vendedor, data, valor):
        self.vendedor = vendedor
        self.data = data
        self.valor = valor
        self.comissao()

    def comissao(self):
        self.vendedor.salario += self.valor * 0.10

    def comprador(self, cliente):
        cliente.registrar_compra(self)


def main():
    vendedor1 = Vendedor("lucas", 19)
    vendedor2 = Vendedor("nivaldo", 49)

    cliente1 = Cliente("bruna",23)
    cliente2 = Cliente("Maria", 49)

    cliente1.registrar_compra(Compra(vendedor1, datetime.now(), 100).comissao())
    cliente2.registrar_compra(Compra(vendedor2, datetime.now(), 200))
    print(cliente2.get_data_ultima_compra())
    print(cliente2.total_compras())
    print(vendedor1.salario)





if __name__ == "__main__":
    main()
        
    

    