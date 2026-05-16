"""
Módulo de conversión de valores para validación y normalización de datos.

Este módulo proporciona funciones de utilidad para convertir y validar valores
de diferentes tipos de datos, garantizando la integridad y compatibilidad de los
datos en la aplicación de servicio médico.

Ejemplos:
    Conversión básica de un valor a float::

        from utils.convertir_valores import convertir_float

        valor_convertido = convertir_float("25.5", "edad")
        print(valor_convertido)  # Salida: 25.5
"""

from typing import Any


def convertir_float(valor: Any, nombre: str) -> float:
    """Convierte un valor a float con validación y manejo de errores.

    Intenta convertir el valor proporcionado a tipo float y si la conversión
    no es posible lanza una excepción ValueError con un mensaje descriptivo
    que incluye el nombre del campo para facilitar la depuración.

    Args:
        valor (Any): El valor a convertir a float puede ser de cualquier tipo
            que sea convertible a float en su formato (str, int, float, etc.).
        nombre (str): El nombre del campo o variable siendo convertida para utilizarlo
            en el mensaje de error para identificar qué campo causó el problema.

    Returns:
        float: El valor convertido exitosamente a tipo float.

    Raises:
        ValueError: Si el valor no puede ser convertido a float se lanza un
            ValueError con un mensaje descriptivo para facilitar la
            identificación del problema.

    Ejemplos:
        Conversión exitosa de una cadena numérica::

            >>> convertir_float("42.5", "temperatura")
            42.5

        Conversión exitosa de un entero::

            >>> convertir_float(100, "presion")
            100.0

        Error con valor inválido::

            >>> convertir_float("abc", "edad")
            Traceback (most recent call last):
                ...
            ValueError: El campo 'edad' debe ser numérico.
    """
    try:
        return float(valor)
    except (TypeError, ValueError):
        raise ValueError(f"El campo '{nombre}' debe ser numérico.")
