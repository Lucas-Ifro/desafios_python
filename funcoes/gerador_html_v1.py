def tag_bloco(texto, classe='sucess', inline = False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="`{classe}>{texto}</tag>"'

def tag_lista(*itens):
    lista = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul>{lista}</ul>'