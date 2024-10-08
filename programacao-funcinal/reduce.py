from functools import reduce

pessoas = [
    {"nome": "pedro", "idade":12},
    {"nome": "lucas", "idade":19},
    {"nome": "andre ferreira", "idade":26},
    {"nome": "bruna", "idade":23},
    {"nome": "carlos", "idade":20},
]

soma_idades = reduce(lambda idades, p: idades + p['idade'], pessoas, 0)
print(soma_idades)