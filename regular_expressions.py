import re
import tables as tb


_space = re.compile(r'&nbsp;')

_asignar_edad = re.compile(r'edad=\{\{edad\|(\d+)\|(\d+)\|(\d+)\}\}')##

_abreviacion = re.compile(r"\{\{abreviación\|.*\|(.*)\}\}")##

_asignar_fecha = re.compile(r'\{\{edad\|(\d+)\|(\d+)\|(\d+)\}\}')##

_ref = re.compile(r'<ref[^>]*>.*?</ref>')

_https = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

_curly_brackets = re.compile(r"\{\{[^{]*?\}\}")

_links = re.compile(r"\[\[(?:[^|\]\[]*\|)*([^\]]+)\]\]")

_html = re.compile(r"<[\s\S]*?>")

_formato = re.compile(r"'{2,}|\({2,}|\){2,}|\"{2,}")

_css = re.compile(r"\{\|[\s\S]*?\|\}")

_line_break = re.compile(r"\n{2,}")

_ascii = re.compile(r"[^\x00-\x7FÁáÉéÍíÓóÚúÜü¡¿Ññ]+")




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
    
    contents = _space.sub(' ', contents)

    contents = _asignar_edad.sub(tb._calcular_edad, contents)
    
    contents = _abreviacion.sub(tb._replace,contents)
    
    contents = _asignar_fecha.sub(r'\1/\2/\3', contents)
   
    contents = _ref.sub( "", contents)##

    contents = _https.sub("", contents)

    while(True):
        aux = _curly_brackets.sub("", contents)
        if contents == aux:
            break
        contents = aux

    while(True):
        aux = _links.sub(r"\1", contents)
        if aux == contents:
            break
        contents = aux

    while(True):
        aux = _html.sub("", contents)
        if aux == contents:
            break
        contents = aux
    
    contents = _formato.sub("", contents)
    
    contents = _css.sub(tb._toString, contents)
    
    contents = _line_break.sub("\n\n", contents)

    contents = _ascii.sub("", contents)
    
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

