from datetime import datetime, timedelta
from functools import reduce


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []


    def __iter__(self):
        return self.tarefas.__iter__()

    def __iadd__(self, tarefa):
        tarefa.dono = self
        self._add_tarefa(tarefa)
        return self
    
    def _add_tarefa(self, tarefa, **kwargs):
        self.tarefas.append(tarefa)

    
    def _add_nova_tarefa(self, descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento', None)))

    
    def add(self, tarefa, vencimento=None, **kwargs):
        funcao_escolhida = self._add_tarefa if isinstance(tarefa, Tarefa) \
            else self._add_nova_tarefa
        kwargs['vencimento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)

    
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
    

class TarefaRecorente(Tarefa):
    def __init__(self, descricao, vencimento=None, dias=7):
        super().__init__(descricao, vencimento)
        self.dias = dias
        self.dono = None

    
    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        nova_tarefa =  TarefaRecorente(self.descricao, novo_vencimento, self.dias)
        if self.dono:
            self.dono += nova_tarefa
        return nova_tarefa

def main():
    casa =  Projeto("Taferas de casa")
    casa.add("passar roupa", datetime.now())
    casa.add("limpar o chão", datetime.now() + timedelta(days=3))

    casa += (TarefaRecorente("Dar comida pra o cachorro", datetime.now()))
    casa.procurar("Dar comida pra o cachorro").concluir()



    casa.procurar('limpar o chão')
    print(casa)

    for ativididade in casa:
        print(ativididade)



if __name__ == "__main__":
    main()