import csv
from urllib import request

def extrair_campus(url):
    with request.urlopen(url) as entrada:
        with open("ibge_limpo.csv" , "w") as saida:
            dados = entrada.read().decode("latin1")
            for cidade in csv.reader(dados.splitlines()):
                print("{},{}".format(cidade[0],cidade[3]),file=saida)


if __name__ == "__main__":
    extrair_campus("http://files.cod3r.com.br/curso-python/desafio-ibge.csv")
