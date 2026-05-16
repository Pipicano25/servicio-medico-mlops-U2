"""
Módulo de predicción clínica simulada.

Este módulo contiene la lógica para evaluar el estado de salud de un paciente
basado en variables clínicas de entrada.

Está diseñado como una simulación para ilustrar el despliegue de una
aplicación Flask con Docker.

Nota:
    Este código no reemplaza la valoración médica real.
"""

from typing import Any, Dict
from utils.convertir_valores import convertir_float


def predecir_estado(datos: Dict[str, Any]) -> str:
    """Predice el estado de salud del paciente según datos clínicos.

    Args:
        datos: Diccionario con los valores de entrada del paciente. Se esperan
            las siguientes claves:
            - edad: años del paciente.
            - temperatura: temperatura corporal en °C.
            - frecuencia_cardiaca: latidos por minuto.
            - dias_sintomas: cantidad de días con síntomas (opcional).
            - dolor: escala de dolor de 0 a 10 (opcional).

    Returns:
        Una cadena con el estado clínico simulado:
        "NO ENFERMO", "ENFERMEDAD LEVE", "ENFERMEDAD AGUDA" o
        "ENFERMEDAD CRÓNICA".

    Raises:
        ValueError: Si alguno de los valores está fuera de rango o no es válido.
    """

    edad = convertir_float(datos.get("edad"), "edad")
    temperatura = convertir_float(datos.get("temperatura"), "temperatura")
    frecuencia_cardiaca = convertir_float(
        datos.get("frecuencia_cardiaca"), "frecuencia_cardiaca"
    )
    dias_sintomas = convertir_float(datos.get("dias_sintomas", 0), "dias_sintomas")
    dolor = convertir_float(datos.get("dolor", 0), "dolor")

    if (
        edad < 0
        or temperatura < 30
        or frecuencia_cardiaca <= 0
        or dias_sintomas < 0
        or not (0 <= dolor <= 10)
    ):
        raise ValueError(
            "Valores fuera de rango. Revise edad, temperatura, frecuencia cardiaca, días de síntomas y dolor."
        )

    # Regla 1: enfermedad terminal.
    # Se prioriza cuando los síntomas llevan mucho tiempo o no hay persistencia clínica.
    if (
        dias_sintomas >= 100
        or (dias_sintomas >= 70 and dolor >= 8)
        or (edad >= 45 and dias_sintomas >= 70)
    ):
        return "ENFERMEDAD TERMINAL"

    # Regla 1: enfermedad crónica.
    # Se prioriza cuando los síntomas llevan mucho tiempo o hay persistencia clínica.
    if (
        dias_sintomas >= 60
        or (dias_sintomas >= 30 and dolor >= 5)
        or (edad >= 65 and dias_sintomas >= 30)
    ):
        return "ENFERMEDAD CRÓNICA"

    # Regla 2: enfermedad aguda.
    # Cuadros intensos de aparición relativamente reciente.
    if (
        temperatura >= 39
        or frecuencia_cardiaca >= 120
        or (dolor >= 8 and dias_sintomas < 30)
    ):
        return "ENFERMEDAD AGUDA"

    # Regla 3: enfermedad leve.
    # Síntomas moderados, sin señales de severidad alta ni cronicidad.
    if (
        temperatura >= 37.5
        or dolor >= 1
        or dias_sintomas >= 1
        or frecuencia_cardiaca >= 100
    ):
        return "ENFERMEDAD LEVE"

    # Regla 4: sin señales clínicas relevantes según la simulación.
    return "NO ENFERMO"
