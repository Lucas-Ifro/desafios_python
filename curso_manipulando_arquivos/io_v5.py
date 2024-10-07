with open('./pessoas.csv') as arquivo:
    with open('./pessoas.txt', 'w') as saida:
        for registro in arquivo:
            print("nome: {}, Idade:{}".format(*registro.strip().split(',')), file=saida)

