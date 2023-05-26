import re
import regex as reg
import tables as tb


def supr_special_characters(contents):
    """
    Text Cleaning
    ---
    ---

    This method cleans the text using regular expressions and removes Wikipedia formatting.

    Parameters:
    -
    contents (str): the text to be cleaned

    Returns:
    -
    str: the cleaned text
    """

    contents = reg._space.sub(" ", contents)

    contents = reg._asignar_edad.sub(tb._calcular_edad, contents)

    contents = reg._abreviacion.sub(tb._replace, contents)

    contents = reg._asignar_fecha.sub(r"\1/\2/\3", contents)

    contents = reg._ref.sub("", contents)  ##

    contents = reg._https.sub("", contents)

    while True:
        aux = reg._curly_brackets.sub("", contents)
        if contents == aux:
            break
        contents = aux

    while True:
        aux = reg._links.sub(r"\1", contents)
        if aux == contents:
            break
        contents = aux

    while True:
        aux = reg._html.sub("", contents)
        if aux == contents:
            break
        contents = aux

    contents = reg._formato.sub("", contents)

    contents = reg._css.sub(tb._toString, contents)

    contents = reg._line_break.sub("\n\n", contents)

    contents = reg._ascii.sub("", contents)

    contents = reg._none.sub("-", contents)

    return contents


def summary(contents):
    """
    Summary of the text
    ---
    ---

    Extracts the summary of the text

    Parameters:
    -
    contents (str): the text

    Returns:
    -
    str: summary of the text
    """
    summary = "---RESUMEN---"
    index = re.search(r"\n+[\S\s]*?\n\n\=", contents)
    for i in range(index.start(), index.end() - 1):
        summary += contents[i]
    return summary


def body(contents):
    """
    Body of the text
    ---
    ---

    Extracts the body of the text

    Parameters:
    -
    contents (str): the text

    Returns:
    -
    str: body of the text
    """
    body = "---CUERPO---\n"
    index = re.search(r"\n\=[\S\s]*", contents)
    for i in range(index.start(), index.end() - 1):
        body += contents[i]
    return re.compile(r"\=+\s*(.*?)\s*\=+").sub(r"\1:", body)
