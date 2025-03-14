from main import *

test_cases = [
    "x = 10;",                          # Asignación simple
    "y = x + 5;",                       # Suma con variable
    "z = (3 + 2) * 4;",                 # Expresión con paréntesis
    "a = b * c + d;",                   # Expresión con variables
    "num = 20 / 4;",                     # División
    "res = 3 + (5 * (2 + 1));",         # Expresión anidada
    "var1 = 7; var2 = var1 + 3;",       # Múltiples asignaciones
    "temp = (x + y) / (z - 1);",        # Expresión compleja con variables
]

invalid_cases = [
    "x = ;",                            # Falta la expresión
    "y = 3 + * 2;",                     # Operador mal ubicado
    "z = (4 + 2;",                      # Paréntesis no cerrado
    "= 5 + 3;",                         # Falta el identificador
    "num = 10 + ;",                     # Falta el operando derecho
    "var 10 = x;",                      # Identificador mal formado
    "x = 2 + 3"                         # Falta el punto y coma
]

for code in test_cases:
    print(f"Probando: {code}")
    result = parser.parse(code)
    print("Resultado:", result, "\n")

for code in invalid_cases:
    print(f"Probando: {code}")
    try:
        result = parser.parse(code)
        print("Resultado:", result, "\n")
    except Exception as e:
        print("Error detectado:", e, "\n")
