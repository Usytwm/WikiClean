import re
import regex as reg
import pandas as pd
from datetime import date, datetime


def replace(match):
    """
    Replace
    ---
    ---

    Replaces a text string.

    Parameters:
    -----------
    match (re.Match): a regular expression match object containing the text string to replace.

    Returns:
    --------
    str: a string representing the replaced text string.

    Example:
    --------
    >>> text = "Hello, world!"
    >>> match = re.search(r'Hello, (.*)!', text)
    >>> _replace(match)
    'world'

    """
    return match.group(1)


def _extract_text(text: str):
    """
    Extract Text
    ---
    ---

    Extracts text from a string containing a Wikipedia template.

    Parameters:
    -----------
    text (str): a string containing a Wikipedia template.

    Returns:
    --------
    list: a list of strings representing the extracted text.

    Example:
    --------
    >>> text = "{|Example template|} text {|Wikipedia template.|}"
    >>> _extract_text(text)
    ['Example template', 'Wikipedia template.']

    """
    ret = []
    aux = ""
    count = 0
    for i in range(len(text) - 1):
        if text[i] == "{" and text[i + 1] == "|":
            count = count + 1
        if text[i] == "|" and text[i + 1] == "}":
            count = count - 1
            if count == 0:
                ret.append(aux[2:])
                aux = ""
        if count > 0:
            aux = aux + text[i]
    return ret


####
def _array(fila: str):
    """
    Converts a text string into a list of elements.

    Parameters:
    -----------
    fila (str): a text string representing a row of a table.

    Returns:
    --------
    list: a list of elements.

    Example:
    --------
    >>> fila = '{|a|b|c|}'
    >>> _array(fila)
    ['a', 'b', 'c']
    """

    def ins(list: list, indice, posiciones):
        for i in range(posiciones):
            list.insert(indice + i, " ")
        return list

    fila = re.sub(r"\{", "", fila)
    fila = re.sub(r"\}", "", fila)
    fila = re.sub(r"\/", "", fila)
    fila = re.sub(r"\"", "", fila)
    fila = re.sub(r"\!+", "!", fila)
    fila = re.sub(r"\|+", "|", fila)
    result = [substring for substring in re.split(r"[!|//]", fila) if substring.strip()]
    # Definimos la expresión regular
    pattern = r'colspan[":=]?(\d+)'

    # Iteramos sobre las cadenas y extraemos el número usando la expresión regular
    ind = 0
    k = len(result)
    while ind < k:
        match = re.search(pattern, result[ind])
        if match:
            number = int(match.group(1))
            result[ind] = ""
            result = ins(result, ind, number - 2)
            ind += number - 1
            # print(f'Número extraído de "{result[ind]}": {number}')
        k = len(result)
        ind += 1

    return result


def _is_valid(table: str):
    """
    is valid
    ---
    ---
    verifies if a Wikipedia table is valid.

    Parameters:
    -
    table (str): a string representing the Wikipedia table.

    Returns:
    -
    bool: True if the table is valid, otherwise.

    Example:
    -
    >>> table = '|-| a | b | c |-| 1 | 2 | 3 '
    >>> _is_valid(table)
    True

    """
    index1 = table.find("|-")
    index2 = table.find("!")
    index3 = table.find("|")
    if index1 >= 0:
        if index2 >= 0:
            return index1 < index2
        else:
            if index3 >= 0:
                return index1 <= index3
            return True
    else:
        return False


def _calcular_edad(match):
    """
    Calculate age
    ---
    ---

    Calculates the age based on a date of birth.

    Parameters:
    -
    match (re.Match): a regular expression match object containing the date of birth in the formatdd|mm|yyyy'.

    Returns:
    -
    str: a string indicating the calculated age.

    Example:
    -
    >>> date_of_birth = '01|01|1990'
    >>> match = re.search(r'(\d{2})\|(\d{2})\|(\d{4})', date_of_birth)
    >>> _calculate_age(match)
    'age=33'
    """
    fecha = "|".join(match.groups())
    hoy = date.today()
    fecha_nacimiento = datetime.strptime(fecha, "%d|%m|%Y")
    edad = (
        hoy.year
        - fecha_nacimiento.year
        - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    )
    return f"edad={edad}"


def toString(matchobj: re.Match):
    """
    A String
    ---
    ---

    This method takes a regular expression match object and extracts the captured text, which is a table, using the given pattern. It then cleans the table using regular expressions and stores it in a DataFrame to print it as a matrix.

    Parameters:
    -
    matchobj (re.Match): a regular expression match object.

    Returns:
    -
    str: a string representation of the matrix.

    Example:
    -
    >>> contents = '{|
    >>> '|-
    >>> '| Competición
    >>> '| Partidos ganados
    >>> '| Partidos empatados}
    >>> '| Partidos perdidos
    >>> '|-
    >>> '|  Primera division
    >>> '|  1270|| 698|| 984
    >>> '|-
    >>> '|  Copa del Rey
    >>> '|  336|| 112|| 163
    >>> '|-
    >>> '| Copa de la Liga
    >>> '| 3|| 4|| 5||
    >>> '|}
    >>> _css = re.compile(r"\{\|[\s\S]*?\|\}")
    >>> contents = _css.sub(tb._toString, contents)
    >>> print(contents)
    '      Competición   Partidos ganados   Partidos empatados   Partidos perdidos'
    ' Primera division               2952                 1270                 698'
    ' Copa del Rey                    336                  112                 163'
    ' Copa de la Liga                   3                    4                   5'
    """

    table = matchobj.group()

    tabar = _extract_text(table)

    tab = ""
    for i in tabar:
        tab = tab + i

    tab = reg.Del_saltos_d_linea.sub("", tab)

    tab = reg.Ident_newFile.sub("\n|-", tab)

    tab = tab + "\n"  # agrego un salto de linea al final en caso de que no lo tenga

    tab = reg.Css_table.sub("", tab)

    tab = reg.Ref.sub("", tab)

    tab = reg.Chtml.sub("", tab)

    if not _is_valid(tab):
        tab = "|-" + tab

    tab = reg.Asignar_edad.sub(_calcular_edad, tab)

    tab = reg.Asignar_fecha.sub(r"\1/\2/\3", tab)

    filas = re.findall(reg.Patron_fila, tab)
    matrix = []
    for fila in filas:
        arr = _array(fila)
        if len(arr) > 0:
            matrix.append(arr)
    if len(matrix) != 0:
        df = pd.DataFrame(matrix)
        return df.to_string(index=False, header=False)
