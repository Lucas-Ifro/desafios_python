def get_tipo_dia(dia):
    dias = {
        (1,7): "fim de semana",
        tuple(range(2,7)): "dia de semana"
    }

    tipo_dia = (tipo for numero, tipo in dias.items() if dia in numero)
    print(next(tipo_dia, "dia invalido"))

if __name__ == "__main__":
    for i in range(0,9):
        get_tipo_dia(i)