import pandas as pd
import re
from datetime import date, datetime


def replace(match):
    return match.group(1)


def extract_text(text: str):
    ret = []
    aux = ""
    count = 0
    for i in range(len(text)-1):
        if(text[i] == '{' and text[i+1] == '|'):
            count = count+1
        if(text[i] == '|' and text[i+1] == '}'):
            count = count-1
            if(count == 0):
                ret.append(aux[2:])
                aux = ""
        if(count > 0):
            aux = aux+text[i]
    return ret


def array(fila: str):
    fila = re.sub(r'\{', '', fila)
    fila = re.sub(r'\}', '', fila)
    fila = re.sub(r'\!+', '!', fila)
    fila = re.sub(r'\|+', '|', fila)
    result = [substring for substring in re.split(
        r'[!|//]', fila) if substring.strip()]

    return result


def is_valid(table: str):
    index1 = table.find("|-")
    index2 = table.find("!")
    index3 = table.find("|")
    if(index1 >= 0):
        if(index2 >= 0):
            return index1 < index2
        else:
            if(index3 >= 0):
                return index1 <= index3
            return True
    else:
        return False


def calcular_edad(match):
    fecha = '|'.join(match.groups())
    hoy = date.today()
    fecha_nacimiento = datetime.strptime(fecha, '%d|%m|%Y')
    edad = hoy.year - fecha_nacimiento.year - \
        ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return f"edad={edad}"


def toString(matchobj: re.Match):
    table = matchobj.group()
    tab = ""
    # extract_outermost(tabla_wiki15e, '{|', '|}')
    tabar = extract_text(table)
    for i in tabar:
        tab = tab+i
    patron = r'\n(?!-\||$)'
    # elimino todos los saltos de linea menos el ultimo
    tab = re.sub(patron, '', tab)
    sust = r'\|\-'
    patron2 = re.compile(sust)
    # sustituyo donde quiera que halla |- por \n|- ya que ahi empieza una nueva fila y quiero identificar las filas desde |- hasta un salto de linea
    tab = patron2.sub("\n|-", tab)
    tab = tab+'\n'  # agrego un salto de linea al final en caso de que no lo tenga
    tab = re.sub(
        r'\s*(?:valign|width|bgcolor|scope|colspan|rowspan|class|border|align|cellpadding|cellspacing|cell|style)\s*=#?(\s*"[^"]*"|\w+)%?', '', tab)  # quitando el css de la tabla
    tab = re.sub(r"<ref[^>]*>.*?</ref>", "", tab)
    tab = re.sub(r'<[^>]*>', '', tab)
    # patron que identifica cuando es una fila desde |- hasta un salto de linea
    patron_fila = r'\|-(.*?)(?=\n)'
    if(not is_valid(tab)):
        tab = "|-"+tab
    asignar_edad = re.compile(r'edad=\{\{edad\|(\d+)\|(\d+)\|(\d+)\}\}')
    tab = asignar_edad.sub(calcular_edad, tab)

    asignar_fecha = re.compile(r'\{\{edad\|(\d+)\|(\d+)\|(\d+)\}\}')

    tab = asignar_fecha.sub(r'\1/\2/\3', tab)
    df = pd.DataFrame()

    filas = re.findall(patron_fila, tab)
    matrix = []
    for fila in filas:
        arr = array(fila)
        if(len(arr) > 0):
            matrix.append(arr)

    df = pd.DataFrame(matrix)
    return df.to_string(index=False, header=False)
