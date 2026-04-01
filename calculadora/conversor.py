"""
Nivel 6: Generación de Código - Conversión de Romano a Entero
Este módulo contiene la función para convertir números romanos a enteros.
"""

from calculadora.error import ExpresionInvalida
from calculadora.validaciones import (
    validar_orden_descendente,
    validar_repeticiones_icxm,
    validar_repeticiones_vld,
    validar_restas,
)
from calculadora.validaciones.alfabeto import validar_simbolos


def romano_a_entero(cadena: str) -> int:
    if not validar_simbolos(cadena):
        raise ExpresionInvalida("contiene símbolos inválidos")

    if not validar_repeticiones_icxm(cadena):
        raise ExpresionInvalida("repetición inválida de I/X/C/M")

    if not validar_repeticiones_vld(cadena):
        raise ExpresionInvalida("repetición inválida de V/L/D")

    if not validar_orden_descendente(cadena):
        raise ExpresionInvalida("orden descendente inválido")

    if not validar_restas(cadena):
        raise ExpresionInvalida("restas inválidas")

    valores = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    total = 0
    valor_previo = 0

    for simbolo in reversed(cadena):
        valor = valores[simbolo]

        if valor < valor_previo:
            total -= valor
        else:
            total += valor

        valor_previo = valor

    return total
"""
    Convierte una cadena de números romanos válida a su valor entero correspondiente.

    Nivel 6: Generación de Código - Conversión Romano → Entero

    💡 PISTA PRIMERO: Llama a todas las validaciones (Niveles 1-5) ANTES de convertir
    💡 PISTA: Usa validar_simbolos(cadena), validar_repeticiones_icxm(cadena), etc.
    💡 PISTA: Si alguna validación retorna False, lanza ExpresionInvalida con mensaje descriptivo (ej: 'contiene símbolos inválidos', 'repetición I/X/C/M', etc.)

    Args:
        cadena (str): La cadena de números romanos validada en Niveles 1-5

    Returns:
        int: El valor entero correspondiente

    Raises:
        ExpresionInvalida: Si la cadena no es válida
"""

