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

    contents = reg.Space.sub(" ", contents)

    contents = reg.Assign_age.sub(tb.calculate_age, contents)

    contents = reg.Abbreviation.sub(tb.replace, contents)

    contents = reg.Assign_date.sub(r"\1/\2/\3", contents)

    contents = reg.Ref.sub("", contents)  ##

    contents = reg.Https.sub("", contents)

    while True:
        aux = reg.Curly_brackets.sub("", contents)
        if contents == aux:
            break
        contents = aux

    while True:
        aux = reg.Links.sub(r"\1", contents)
        if aux == contents:
            break
        contents = aux

    while True:
        aux = reg.Html.sub("", contents)
        if aux == contents:
            break
        contents = aux

    contents = reg.Format.sub("", contents)

    contents = reg.Css.sub(tb.toString, contents)

    contents = reg.Line_break.sub("\n\n", contents)

    contents = reg.Ascii.sub("", contents)

    contents = reg.Tnone.sub("-", contents)

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
