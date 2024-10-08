pessoas = [
    {"nome": "pedro", "idade":12},
    {"nome": "lucas", "idade":19},
    {"nome": "andre ferreira", "idade":26},
    {"nome": "bruna", "idade":23},
    {"nome": "carlos", "idade":20},
]

menores = filter(lambda p: len(p['nome']) > 6, pessoas)
print(list(menores))