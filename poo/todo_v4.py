from datetime import datetime, timedelta
from functools import reduce


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []


    def __iter__(self):
        return self.tarefas.__iter__()

    
    def add(self, descricao, vencimento=None):
        self.tarefas.append(Tarefa(descricao, vencimento))

    
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

    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento


    def concluir(self):
        self.feito = True


    def __str__(self):
        status = []
        if self.feito:
            status.append(' (Concluída)')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append(' (vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(Vence em {dias} dias)')

        return self.descricao + ' '.join(status)
    
def main():
    casa =  Projeto("Taferas de casa")
    casa.add("passar roupa", datetime.now())
    casa.add("limpar o chão", datetime.now() + timedelta(days=3))

    casa.procurar('limpar o chão')
    print(casa)

    for ativididade in casa:
        print(ativididade)



if __name__ == "__main__":
    main()