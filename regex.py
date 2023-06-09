import re

Space = re.compile(
    r"&nbsp;"
)  # Busca la expresión " " que representa un espacio en blanco en HTML.

Assign_age = re.compile(
    r"edad=\{\{edad\|(\d+)\|(\d+)\|(\d+)\}\}"
)  # Busca la expresión "{{edad|día|mes|año}}" y captura los valores de día, mes y año en grupos.

Abbreviation = re.compile(
    r"\{\{abreviación\|.*\|(.*)\}\}"
)  # Busca la expresión "{{abreviación|idioma|abreviatura}}" y captura la abreviatura en un grupo.

Assign_date = re.compile(
    r"\{\{edad\|(\d+)\|(\d+)\|(\d+)\}\}"
)  # Busca la expresión "{{edad|día|mes|año}}" y captura los valores de día, mes y año en grupos.

Ref = re.compile(
    r"<ref[^>]*>.*?</ref>"
)  # Busca las etiquetas <ref> y </ref> y todo lo que hay entre ellas.

Https = re.compile(
    r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
)  # Busca las URLs que comienzan con "http://" o "https://" y captura toda la URL.

Curly_brackets = re.compile(
    r"\{\{[^{]*?\}\}"
)  # Busca las expresiones que comienzan y terminan con doble llave "{{" y "}}" y captura todo lo que hay entre ellas.

Links = re.compile(
    r"\[\[(?:[^|\]\[]*\|)*([^\]]+)\]\]"
)  # Busca las expresiones que comienzan y terminan con doble corchete "[[" y "]]" y captura el texto después del último "|" en un grupo.

Html = re.compile(
    r"<[\s\S]*?>"
)  # Busca las etiquetas HTML y todo lo que hay entre ellas.

Format = re.compile(
    r"'{2,}|\({2,}|\){2,}|\"{2,}"
)  # Busca las comillas dobles o simples repetidas dos o más veces, o los paréntesis repetidos dos o más veces.

Css = re.compile(
    r"\{\|[\s\S]*?\|\}"
)  # Busca las expresiones que comienzan y terminan con doble llave y barra vertical "{{|" y "|}}" y captura todo lo que hay entre ellas.

Line_break = re.compile(r"\n{2,}")  # Busca dos o más saltos de línea consecutivos.

Ascii = re.compile(
    r"[^\x00-\x7FÁáÉéÍíÓóÚúÜü¡¿Ññ]+"
)  # Busca todos los caracteres que no son ASCII o caracteres especiales en español.

delete_line_breaks = re.compile(
    r"\n(?!-\||$)"
)  # Busca los saltos de línea que no están seguidos por "-|" o el final de la línea.

Ident_newFile = re.compile(
    r"\|\-"
)  # Busca la expresión "|-" que indica el inicio de una nueva fila en una tabla.

Patron_fila = re.compile(
    r"\|-(.*?)(?=\n)"
)  # Busca las filas de una tabla que comien con "|-" y terminan con un salto de línea.

Css_table = re.compile(
    r'\s*(?:valign|width|bgcolor|scope|rowspan|class|border|align|cellpadding|cellspacing|cell|style)\s*=#?(\s*"[^"]*"|\w+)%?'
)  # Busca las propiedades CSS de una tabla

Ref = re.compile(
    r"<ref[^>]*>.*?</ref>"
)  # Busca las etiquetas <ref> y </ref> y todo lo que hay entre ellas.

Chtml = re.compile(r"<[^>]*>")  # Busca las etiquetas HTML

Tnone = re.compile(r"\bNone\b")  # Busca la palabra "None" como una palabra completa
