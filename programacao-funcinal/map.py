lista_1 = [1,2,3]

dobro = map(lambda i: i * 2, lista_1)

print(list(dobro))

compras = (
    {'quantidade':2, 'preco':10},
    {'quantidade':1, 'preco':15},
    {'quantidade':2, 'preco':20},
)

[print(frase) for frase in list(
    map(
        lambda compra: 
        f"quantidade = {compra['quantidade']}, preco = {compra['preco']}, total = {compra['quantidade'] * compra['preco']}", 
        compras
        ))]