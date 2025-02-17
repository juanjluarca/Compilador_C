import re

# Op relacional = <, >, =, !, <=, >=, ==, !=,
# Op lógicos = &, &&, |, ||, !
# Definir patrones de tokens
token_patron = {
    "KEYWORD": r'\b(if|else|while|for|return|int|float|void|class|def|print)\b',
    "IDENTIFIER": r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',
    "NUMBER": r'\b\d+\b',
    "OPERATOR": r'<=|>=|==|!=|&&|"|[\+\-\*/=<>\!\||\|\']',
    "DELIMITER": r'[(),;{}]',  # Paréntesis, llaves, punto y coma
    "WHITESPACE": r'\s+'  # Espacios en blanco
}


def tokenize(text):
    patron_general = "|".join(f"(?P<{token}>{patron})" for token, patron in token_patron.items())
    patron_regex = re.compile(patron_general)

    tokens_encontrados = []

    for match in patron_regex.finditer(text):
        for token, valor in match.groupdict().items():
            if valor is not None and token != "WHITESPACE":
                tokens_encontrados.append((token, valor))
    return tokens_encontrados


class NodoAST:
    # Clase base para todos los nodos del AST
    pass


class NodoFuncion(NodoAST):
    # Nodo que representa una función
    def __init__(self, nombre, parametros, cuerpo):
        self.nombre = nombre
        self.parametros = parametros
        self.cuerpo = cuerpo


class NodoParametro(NodoAST):
    # Nodo que representa un parámetro de función
    def __init__(self, tipo, nombre):
        self.tipo = tipo
        self.nombre = nombre


class NodoAsignacion(NodoAST):
    # Nodo que representa una asignación de variable
    def __init__(self, nombre, expresion):
        self.nombre = nombre
        self.expresion = expresion


class NodoOperacion(NodoAST):
    # Nodo que representa una operación aritmética
    def __init__(self, izquierda, operador, derecha):
        self.izquierda = izquierda
        self.operador = operador
        self.derecha = derecha

