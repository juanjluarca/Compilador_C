import re

texto = """
int suma(int a, int b) {
  int c = a + b;
  int d;
  d = a - b;
  int e = a * b;
  int f = a / b;

  if (c >= d) {
    a = b + c;
    int z = d / a;
    if (z < b) {
      b = a - b;
    } else {
      b = a + b;
    }
  }

  while (e <= f) {
    e = e + 1;
  }

  for(int i = 0; i < 10; i = i + 3) print(i);

  print("El resultado de la suma es: ");

  return f;
}
"""
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


tokens = tokenize(texto)


# Analizador sintáctico

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def obtener_token_actual(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def coincidir(self, tipo_esperado):
        token_actual = self.obtener_token_actual()
        if token_actual and token_actual[0] == tipo_esperado:
            self.pos += 1
            return token_actual
        else:
            raise SyntaxError(f'Error sintáctico: se esperaba {tipo_esperado}, pero se encontró: {token_actual}')

    def parsear(self):
        # Punto de entrada del analizador: se espera una función
        self.funcion()

    # Función para reconocer declaraciones de variables dentro del cuerpo de la función y evaluar operaciones aritméticas más complejas:
    def funcion(self):
        # Gramática para una función: int IDENTIFICADOR (int IDENTIFICADOR*) {cuerpo}
        self.coincidir('KEYWORD')  # Tipo de retorno (ej. int)
        self.coincidir('IDENTIFIER')  # Nombre de la función
        self.coincidir('DELIMITER')  # Se espera un "("
        self.parametros()
        self.coincidir('DELIMITER')  # Se espera un ")"
        self.cuerpo()

    def parametros(self):
        # Reglas para parámetros: int IDENTIFIER(, int IDENTIFIER)*
        self.coincidir('KEYWORD')  # Tipo del parámetro
        self.coincidir('IDENTIFIER')  # Nombre del parámetro
        while self.obtener_token_actual() and self.obtener_token_actual()[1] == ',':
            self.coincidir('DELIMITER')  # Espera una ","
            self.coincidir('KEYWORD')  # Tipo del parámetro
            self.coincidir('IDENTIFIER')  # Nombre del parámetro

    # Función para reconocer declaraciones de variables dentro del cuerpo de la función y evaluar operaciones aritméticas más complejas:

    def cuerpo(self):
        # Gramática para el cuerpo de la función: return IDENTIFIER OPERATOR IDENTIFIER
        # Reconocer declaraciones de variables dentro del cuerpo de la función y evaluar operaciones aritméticas más complejas:
        if self.obtener_token_actual() and self.obtener_token_actual()[1] == '{':
            self.coincidir('DELIMITER')  # Se espera un "{"
        while self.obtener_token_actual() and self.obtener_token_actual()[1] != 'return' and \
                self.obtener_token_actual()[1] != '}':
            if self.obtener_token_actual()[1] == 'int':
                self.declaracion_variable()
            elif self.obtener_token_actual()[0] == 'IDENTIFIER':
                self.coincidir('IDENTIFIER')  # Identificador <nombre de la variable>
                self.operacion_aritmetica()
            elif self.obtener_token_actual()[0] == 'KEYWORD':
                if self.obtener_token_actual()[1] == 'if':
                    self.sentencia_if()
                elif self.obtener_token_actual()[1] == 'while':
                    self.sentencia_while()
                elif self.obtener_token_actual()[1] == 'for':
                    self.sentencia_for()
                elif self.obtener_token_actual()[1] == 'print':
                    self.sentencia_print()
                else:
                    break;
            else:
                break;
        if self.obtener_token_actual() and self.obtener_token_actual()[1] == 'return':
            self.coincidir('KEYWORD')  # return
            self.coincidir('IDENTIFIER')  # Identificador <nombre de la variable>
            if (self.obtener_token_actual() and self.obtener_token_actual()[0] == 'OPERATOR'):
                self.coincidir('OPERATOR')  # Operador ej. +
                self.coincidir('IDENTIFIER')  # Identificador <nombre de la variable
            self.coincidir('DELIMITER')  # Final del statement ";"
        if self.obtener_token_actual() and self.obtener_token_actual()[1] == '}':
            self.coincidir('DELIMITER')  # Se espera un "}"

    def sentencia_if(self):
        self.coincidir('KEYWORD')  # if
        self.coincidir('DELIMITER')  # (
        self.condicion_a_evaluar()  # Condición ej x < 8
        self.coincidir('DELIMITER')  # )
        self.cuerpo()
        if self.obtener_token_actual() and self.obtener_token_actual()[1] == 'else':
            self.coincidir('KEYWORD')  # else
            self.cuerpo()

    def sentencia_while(self):
        self.coincidir('KEYWORD')  # while
        self.coincidir('DELIMITER')  # (
        self.condicion_a_evaluar()  # Condición ej x < 8
        self.coincidir('DELIMITER')  # )
        self.cuerpo()

    def sentencia_for(self):
        self.coincidir('KEYWORD')  # for
        self.coincidir('DELIMITER')  # (
        self.coincidir('KEYWORD')  # int
        self.coincidir('IDENTIFIER')  # Identificador <nombre de la variable>
        self.coincidir('OPERATOR')  # Asignación ej =
        self.number_or_identifier()  # Número o identificador
        self.coincidir('DELIMITER')  # ;
        self.condicion_a_evaluar()  # Condición ej x < 8
        self.coincidir('DELIMITER')  # ;
        self.coincidir('IDENTIFIER')  # i
        self.coincidir('OPERATOR')  # =
        self.condicion_a_evaluar()
        self.coincidir('DELIMITER')  # )
        self.cuerpo()

    def sentencia_print(self):
        self.coincidir('KEYWORD')  # print
        self.coincidir('DELIMITER')  # (
        if self.obtener_token_actual() and self.obtener_token_actual()[1] == '"':
            self.coincidir('OPERATOR')  # OPERADOR "
            while self.obtener_token_actual() and (
                    self.obtener_token_actual()[0] == 'IDENTIFIER' or self.obtener_token_actual()[0] == 'NUMBER'):
                self.number_or_identifier()
            self.coincidir('OPERATOR')  # OPERADOR "
        else:
            self.number_or_identifier()
        self.coincidir('DELIMITER')  # )
        self.coincidir('DELIMITER')  # ;

    def declaracion_variable(self):
        # Gramática para declaraciones de variables: IDENTIFIER OPERATOR IDENTIFIER
        self.coincidir('KEYWORD')  # palabra para declarar variable ej. int
        self.coincidir('IDENTIFIER')  # Identificador <nombre de la variable>
        if self.obtener_token_actual() and self.obtener_token_actual()[0] == 'DELIMITER':
            self.coincidir('DELIMITER')  # Final del statement ";"
        elif self.obtener_token_actual() and self.obtener_token_actual()[0] == 'NUMBER':
            self.coincidir('NUMBER')  # Valor numérico de la variable
            self.coincidir('DELIMITER')  # Final del statement ";"
        else:
            self.operacion_aritmetica()

    def operacion_aritmetica(self):
        # Gramática para operaciones aritméticas: IDENTIFIER OPERATOR IDENTIFIER
        self.coincidir('OPERATOR')  # Asignación ej =
        self.number_or_identifier()
        self.coincidir('OPERATOR')  # Operador ej. +
        self.number_or_identifier()
        self.coincidir('DELIMITER')  # Final del statement ";"

    def condicion_a_evaluar(self):
        self.number_or_identifier()
        self.coincidir('OPERATOR')
        self.number_or_identifier()

    def number_or_identifier(self):
        if self.obtener_token_actual() and self.obtener_token_actual()[0] == 'NUMBER':
            self.coincidir('NUMBER')
        else:
            self.coincidir('IDENTIFIER')


#  Aquí se prueba
try:
    print('Se inicia el análisis sintáctico')
    parser = Parser(tokens)
    parser.parsear()
    print('Análisis sintáctico exitoso')
except SyntaxError as e:
    print(e)
