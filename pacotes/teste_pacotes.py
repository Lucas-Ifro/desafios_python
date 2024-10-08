from app.utils.gerador import novo_nome
from app.negocio import nome_existe
from app.negocio.backend import add_nome

def main():
    nome = novo_nome
    if nome_existe(nome):
        print(add_nome(nome))
    else:
        print(None)

if __name__ == "__main__":
    main()