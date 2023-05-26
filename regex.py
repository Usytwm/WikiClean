import re

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

# patron para eliminar todos los saltos de linea menos el ultimo
_del_saltos_d_linea = re.compile(r'\n(?!-\||$)')

# patron para sustituir donde quiera que halla |- por \n|- ya que ahi empieza una nueva fila y quiero identificar las filas desde |- hasta un salto de linea
_ident_newFile = re.compile(r'\|\-')

# patron que identifica cuando es una fila desde |- hasta un salto de linea
_patron_fila = re.compile(r'\|-(.*?)(?=\n)')

#patron para buscar sustituir la edad 
_asignar_edad = re.compile(r'edad=\{\{edad\|(\d+)\|(\d+)\|(\d+)\}\}')

_asignar_fecha = re.compile(r'\{\{edad\|(\d+)\|(\d+)\|(\d+)\}\}')

# para quitar el css de la tabla
_css_table = re.compile(r'\s*(?:valign|width|bgcolor|scope|colspan|rowspan|class|border|align|cellpadding|cellspacing|cell|style)\s*=#?(\s*"[^"]*"|\w+)%?')

_ref = re.compile(r'<ref[^>]*>.*?</ref>')

_chtml=re.compile(r'<[^>]*>')

