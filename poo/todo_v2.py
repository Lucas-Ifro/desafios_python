from datetime import datetime
from functools import reduce


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    
    def add(self, descricao):
        self.tarefas.append(Tarefa(descricao))

    
    def pendentes(self):
        return [tarefa for tarefa in self.tarefas \
                if not tarefa.feito]
    

    def procurar(self,descricao):
        return [tarefa for tarefa in self.tarefas \
                if tarefa.descricao == descricao][0]


    def __str__(self):
        return f'{self.nome}: {
            reduce(
                lambda string, tarefa: f"{string}\n - {tarefa.descricao 
                                                       if not tarefa.feito else 'Concluída'}"
            , self.tarefas, "")}'


class Tarefa:

    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()


    def concluir(self):
        self.feito = True


    def __str__(self):
        return self.descricao + (" (Concluída)" if self.feito else '')
    
def main():
    casa =  Projeto("Taferas de casa")
    casa.add("passar roupa")
    casa.add("limpar o chão")

    casa.procurar('limpar o chão').concluir()
    print(casa)



if __name__ == "__main__":
    main()