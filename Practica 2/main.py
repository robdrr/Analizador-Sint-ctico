import ply.lex as lex
import ply.yacc as yacc

# Definición de tokens para el analizador léxico
tokens = (
    'IDENTIFIER', 'NUMBER',
    'PLUS', 'TIMES', 'DIVIDE', 'EQUALS', 'LPAREN', 'RPAREN', 'SEMICOLON'
)

# Definición de expresiones regulares para los tokens
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_PLUS      = r'\+'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_EQUALS    = r'='
t_SEMICOLON = r';'

# Regla para los identificadores (variables)
def t_IDENTIFIER(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'  # Debe comenzar con una letra y puede contener letras, números y guiones bajos
    return t

# Regla para los números enteros
def t_NUMBER(t):
    r'\d+'  # Coincide con uno o más dígitos
    t.value = int(t.value)  # Convierte el valor a un número entero
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Regla para manejar nuevas líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)  # Incrementa el número de línea

# Manejo de errores en el análisis léxico
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")  # Muestra el carácter no reconocido
    t.lexer.skip(1)  # Salta el carácter no válido

# Construcción del analizador léxico
lexer = lex.lex()

# Definición de la gramática para el analizador sintáctico

def p_program(p):
    '''program : assignment
               | assignment program'''
    # Un programa puede ser una única asignación o una asignación seguida de otro programa
    if len(p) == 2:
        p[0] = [p[1]]  # Si es una única asignación, se almacena en una lista
    else:
        p[0] = [p[1]] + p[2]  # Si hay más asignaciones, se concatenan en una lista

def p_assignment(p):
    'assignment : IDENTIFIER EQUALS expression SEMICOLON'
    # Una asignación tiene la forma: identificador = expresión ;
    p[0] = ('assign', p[1], p[3])  # Se almacena como una tupla ('assign', identificador, expresión)

def p_expression(p):
    '''expression : term
                  | term PLUS expression'''
    # Una expresión puede ser un término solo o un término seguido de una suma y otra expresión
    if len(p) == 2:
        p[0] = p[1]  # Si es solo un término, se devuelve como está
    else:
        p[0] = ('+', p[1], p[3])  # Si hay una suma, se almacena como una tupla ('+', término, expresión)

def p_term(p):
    '''term : factor
            | factor TIMES term
            | factor DIVIDE term'''
    # Un término puede ser un factor solo o un factor multiplicado o dividido por otro término
    if len(p) == 2:
        p[0] = p[1]  # Si es solo un factor, se devuelve directamente
    else:
        p[0] = (p[2], p[1], p[3])  # Si hay multiplicación o división, se almacena como una tupla (operador, factor, término)

def p_factor(p):
    '''factor : IDENTIFIER
              | NUMBER
              | LPAREN expression RPAREN'''
    # Un factor puede ser un identificador, un número o una expresión entre paréntesis
    if len(p) == 2:
        p[0] = p[1]  # Si es un identificador o número, se devuelve directamente
    else:
        p[0] = p[2]  # Si está entre paréntesis, se devuelve la expresión interna

# Manejo de errores en el análisis sintáctico
def p_error(p):
    print("Error de sintaxis")  # Mensaje de error cuando hay una estructura incorrecta

# Construcción del analizador sintáctico
parser = yacc.yacc()

