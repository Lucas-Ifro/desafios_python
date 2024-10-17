bloco_atrs = ('bloco_accesskey', 'bloco_id')
ul_atrs = ('ul_id', 'ul_style')


def get_atrs(informados, suportados):
    return ''.join(f'{k.split('_')[-1]}="{v}" ' for k, v in informados.items() if k in suportados) 


def tag_bloco(comteudo, *args, classe='sucess', inline = False, **kwargs):
    tag = 'span' if inline else 'div'
    html = comteudo if not callable(comteudo) else comteudo(*args,**kwargs)
    atributos = get_atrs(kwargs, bloco_atrs)
    return f'<{tag} {atributos}class="{classe}">{html}</tag>'


def tag_lista(*itens, **kwargs):
    lista = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul {get_atrs(kwargs, ul_atrs)}>{lista}</ul>'


if __name__ == "__main__":
    print(tag_bloco(tag_lista, "lucas", "ferreira", classe='info', inline=True))
    print(tag_bloco(tag_lista, "lucas", "ferreira", classe='info', bloco_accesskey='m', bloco_id="1", ul_id=2, ul_style="none"))