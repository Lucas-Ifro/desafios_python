def tag(tag, *args, **kwargs):
    if 'html_class' in kwargs:
        kwargs['class'] = kwargs.pop('html_class')
    conteudo_html = ''.join(f"{conteudo} " for conteudo in args)
    classes = ''.join(f' {classes}="{valor}"' for classes, valor in kwargs.items())
    return ''.join(f'<{tag}{classes}>{conteudo_html}</{tag}>')


if __name__ == "__main__":
    print(
        tag('p',
            tag('span', 'Curso de python 3, por'),
            tag('strong', 'Curso de python 3, por', id='jl', ik='jl'),
            tag('span', ' e '),
            tag('strong', 'Curso de python 3, por', id='ll'),
            tag('span', '.'),
            html_class='alert'
            )
    )