import re
import tables as tb


def supr_special_characters(contents):
    contents = re.sub(r'&nbsp;', ' ', contents)

    asignar_edad = re.compile(r'edad=\{\{edad\|(\d+)\|(\d+)\|(\d+)\}\}')##
    contents = asignar_edad.sub(tb.calcular_edad, contents)

    abreviacion = re.compile(r"\{\{abreviación\|.*\|(.*)\}\}")##
    contents = abreviacion.sub(tb.replace,contents)

    asignar_fecha = re.compile(r'\{\{edad\|(\d+)\|(\d+)\|(\d+)\}\}')##
    contents = asignar_fecha.sub(r'\1/\2/\3', contents)

    contents = re.sub(r"<ref[^>]*>.*?</ref>", "", contents)##

    https = re.compile(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    contents = https.sub("", contents)

    curly_brackets = re.compile(r"\{\{[^{]*?\}\}")

    while(True):
        aux = curly_brackets.sub("", contents)
        if contents == aux:
            break
        contents = aux

    links = re.compile(r"\[\[(?:[^|\]\[]*\|)*([^\]]+)\]\]")

    while(True):
        aux = links.sub(r"\1", contents)
        if aux == contents:
            break
        contents = aux

    html = re.compile(r"<[\s\S]*?>")

    while(True):
        aux = html.sub("", contents)
        if aux == contents:
            break
        contents = aux

    formato = re.compile(r"'{2,}|\({2,}|\){2,}|\"{2,}")
    contents = formato.sub("", contents)

    css = re.compile(r"\{\|[\s\S]*?\|\}")
    contents = css.sub(tb.toString, contents)

    """
    css = re.compile(r"\{\|[\s\S]*?\|\}")
    contents = css.sub("cojone", contents)

    pipes = re.compile(r"\|[\S\s]*?\n")
    contents = pipes.sub("", contents)"""

    line_break = re.compile(r"\n{2,}")
    contents = line_break.sub("\n\n", contents)

    return contents


def summary(contents):
    summary = "---RESUMEN---"
    index = re.search(r"\n+[\S\s]*?\n\n\=", contents)
    for i in range(index.start(), index.end() - 1):
        summary += contents[i]
    return summary


def body(contents):
    body = "---CUERPO---\n"
    index = re.search(r"\n\=[\S\s]*", contents)
    for i in range(index.start(), index.end() - 1):
        body += contents[i]
    return re.compile(r"\=+\s*(.*?)\s*\=+").sub(r"\1:", body)


def contents_board(contents):
    pass
