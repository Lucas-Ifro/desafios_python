with open('./pessoas.csv') as arquivo:
    for registro in arquivo:
        print("nome: {}, Idade:{}".format(*registro.strip().split(',')))

