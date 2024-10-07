try:
    arquivo = open('./pessoas.csv')
    for registro in arquivo:
        print("nome: {}, Idade:{}".format(*registro.strip().split(',')))
finally:
    arquivo.close()
