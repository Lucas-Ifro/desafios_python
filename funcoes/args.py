def calcula_valor_final(valor_bruto, tipo_imposto, **kwargs):
    valor =  valor_bruto + valor_bruto * tipo_imposto(**kwargs)
    print(valor)

def imposto_x(internacional):
    return 0.22 if internacional else 0.13


def imposto_y(explosivo, mult):
    return 0.12 * mult if explosivo else 0


if __name__ == "__main__":
    calcula_valor_final(135, imposto_x, internacional=True)
    calcula_valor_final(135, imposto_y, explosivo=True, mult=1.5)
