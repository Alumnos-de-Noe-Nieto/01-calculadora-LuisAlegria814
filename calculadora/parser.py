"""
Nivel 7: Parsing de Expresiones
Este módulo contiene las funciones para parsear expresiones aritméticas con números romanos.
"""

from dataclasses import dataclass

from calculadora.error import ExpresionInvalida


@dataclass
class Token:
    """
    Representa un token en una expresión aritmética de números romanos.

    Attributes:
        tipo: El tipo de token ("ROMANO", "SUMA", "RESTA", "ESPACIO")
        valor: El valor del token (cadena)
        posicion: La posición del token en la expresión original
    """

    tipo: str
    valor: str
    posicion: int


def evaluar_expresion(expresion: str) -> list[Token]:
    """
    Tokeniza y valida una expresión aritmética de números romanos.

    Nivel 7.1: Parsing completo de expresiones aritméticas de números romanos.
    💡 PISTA: Primero llama a tokenizar_expresion(expresion) para obtener los tokens
    💡 PISTA: Luego llama a validar_estructura_tokens(tokens) para validar la estructura
    💡 PISTA: Si validar_estructura_tokens(tokens) retorna False, lanza ExpresionInvalida
    💡 PISTA: Si la expresión está vacía (no tokens), retorna lista vacía []
    💡 PISTA: Usa try-except para capturar errores de tokenizar_expresion
    💡 PISTA: Mensaje de error: f'La expresión "{expresion}" tiene una estructura inválida'

    Args:
        expresion (str): La expresión a parsear

    Returns:
        List[Token]: La lista de tokens encontrados (vacía si la expresión es vacía)

    Raises:
        ExpresionInvalida: Si la expresión contiene caracteres inválidos o tiene estructura inválida

    Examples:
        >>> evaluar_expresion("XIV + LX")
        [Token("ROMANO", "XIV", 0), Token("ESPACIO", " ", 3), Token("SUMA", "+", 4), ...]
        >>> evaluar_expresion("")
        []
    """
    try:
        tokens = tokenizar_expresion(expresion)
    except ExpresionInvalida:
        raise

    tokens_sin_espacios = [t for t in tokens if t.tipo != "ESPACIO"]

    if not tokens_sin_espacios:
        return []

    if not validar_estructura_tokens(tokens):
        raise ExpresionInvalida(
            f'La expresión "{expresion}" tiene una estructura inválida'
        )

    return tokens


def tokenizar_expresion(expresion: str) -> list[Token]:
    """
    Tokeniza una expresión de texto en una lista de tokens.

    Nivel 7.2: Tokenización de expresiones aritméticas.
    """
    tokens = []
    i = 0
    romanos = "IVXLCDM"

    while i < len(expresion):
        char = expresion[i]

        if char == " ":
            tokens.append(Token("ESPACIO", " ", i))
            i += 1

        elif char == "+":
            tokens.append(Token("SUMA", "+", i))
            i += 1

        elif char == "-":
            tokens.append(Token("RESTA", "-", i))
            i += 1

        elif char in romanos:
            inicio = i
            while i < len(expresion) and expresion[i] in romanos:
                i += 1
            tokens.append(Token("ROMANO", expresion[inicio:i], inicio))

        else:
            raise ExpresionInvalida(
                f"Carácter inválido '{expresion[i]}' en posición {i}"
            )

    return tokens


def validar_estructura_tokens(tokens: list[Token]) -> bool:
    """
    Valida que la expresión tenga una estructura válida.

    Nivel 7.3: Validación de estructura de tokens.
    """

    tokens_filtrados = [t for t in tokens if t.tipo != "ESPACIO"]


    if len(tokens_filtrados) < 3:
        return False


    if len(tokens_filtrados) % 2 == 0:
        return False


    if tokens_filtrados[0].tipo != "ROMANO":
        return False
    if tokens_filtrados[-1].tipo != "ROMANO":
        return False

    for i, token in enumerate(tokens_filtrados):
        if i % 2 == 0:
            if token.tipo != "ROMANO":
                return False
        else:
            if token.tipo not in ("SUMA", "RESTA"):
                return False

    return True
