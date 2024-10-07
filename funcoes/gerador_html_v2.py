def tag_bloco(texto, *args, classe='sucess', inline = False):
    tag = 'span' if inline else 'div'
    html = texto if not callable(texto) else texto(*args)
    return f'<{tag} class="`{classe}>{html}</tag>"'

def tag_lista(*itens):
    lista = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul>{lista}</ul>'

if __name__ == "__main__":
    print(tag_bloco(tag_lista, "lucas", "ferreira", classe='info'))