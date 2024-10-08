from funcao_primeira_classe import doblo, quadrado


def processar(titulo, lista, funcao):
    print(f"Processando: {titulo}")
    for i in lista:
        print(i, '=>', funcao(i))


if __name__ == "__main__":
    processar("dobros", range(10), doblo)