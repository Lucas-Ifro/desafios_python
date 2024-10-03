import pandas as pd

df_inventario = pd.read_csv("./inventarios.csv", header=0)



inventario = []

def adicionar_item(nome, quantidade, categoria):
    global df_inventario
    df_filtrado = df_inventario[df_inventario['nome'] == nome]
    if df_filtrado.shape[0] < 1:
        novo_item = pd.DataFrame({"nome":[nome], "categoria":[categoria],"quantidade":[quantidade]})
        df_inventario = pd.concat([df_inventario, novo_item], ignore_index=True)
    else:
        print("o item já está no inventario")

def remover_item(nome):
    global df_inventario
    item_index = df_inventario[df_inventario['nome'] == nome].index
    df_inventario = df_inventario.drop(item_index)

def ordenar_inventario():
    global df_inventario
    df_inventario = df_inventario.sort_values(by='nome').reset_index(drop=True)

def contar_itens():
    print(df_inventario.shape[0])

def buscar_item(nome):
    print(df_inventario[df_inventario['nome'] == nome])

def atualizar_quantidade(nome, nova_quantidade):
    global df_inventario
    df_filtrado = df_inventario[df_inventario['nome'] == nome]
    if df_filtrado.shape[0] > 0:
        df_filtrado.loc[1,"quantidade"] = nova_quantidade
        df_inventario = pd.concat([df_inventario, df_filtrado], ignore_index=True)
    else:
        print("O item não foi cadastrado")
def salvar_alteracoes():
    df_inventario.to_csv("./inventarios.csv")
def menu():
    print("1. Adicionar Item")
    print("2. Remover Item")
    print("3. Ordenar Inventário")
    print("4. Contar Itens")
    print("5. Buscar Item")
    print("6. Sair")

if __name__ == "__main__":
    adicionar_item("caneta2",5,"escritorio")
    adicionar_item("lapis",5,"escritorio")
    adicionar_item("borracha",5,"escritorio")
    adicionar_item("regua",5,"escritorio")
    remover_item("caneta2")
    ordenar_inventario()
    contar_itens()
    buscar_item("caneta")
    atualizar_quantidade("caneta", 10)
    print(df_inventario.head())


    
