compras = (
    {'quantidade':2, 'preco':10},
    {'quantidade':1, 'preco':15},
    {'quantidade':2, 'preco':20},
)

totais = tuple(
    map(
        lambda compra: compra['quantidade'] * compra['preco'],
        compras
    )
)

totais2 = [compra['quantidade'] * compra['preco'] for compra in compras]

print(totais)
print(sum(totais))
print(totais2)