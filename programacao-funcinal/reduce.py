from functools import reduce

pessoas = [
    {"nome": "pedro", "idade":12},
    {"nome": "lucas", "idade":19},
    {"nome": "andre ferreira", "idade":26},
    {"nome": "bruna", "idade":23},
    {"nome": "carlos", "idade":20},
]
so_dades = map(lambda p: {"idade": p['idade']}, pessoas)
print(list(so_dades))
soma_idades = reduce(lambda idades, p: idades + p['idade'], pessoas, 0)
print(soma_idades)

soma_das_idades = reduce(lambda total, p: total + f"Nome: {p['nome']}, Idade: {p['idade']};\n", pessoas, 'Pessoas cadastradas: \n')
print(soma_das_idades)