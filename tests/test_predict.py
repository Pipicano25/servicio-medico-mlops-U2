"""
Módulo de pruebas unitarias para la función de predicción de estado médico.

Contiene un conjunto de pruebas unitarias que cubren diferentes escenarios
clínicos, incluyendo personas sanas y pacientes con diferentes grados de
enfermedad (leve, aguda y crónica).

Las pruebas utilizan datos médicos simulados que incluyen edad, temperatura,
frecuencia cardíaca, días de síntomas y nivel de dolor para validar que
el modelo de predicción clasifique segun las categorías definidas.

Módulos importados:
    app: Módulo principal que contiene la función predecir_estado.
"""

from app import predecir_estado


def test_no_enfermo():
    """
    Prueba que valida la predicción correcta de un paciente sano.

    Esta función prueba el caso de un paciente sin síntomas de enfermedad,
    con signos vitales normales y sin dolor. Los parámetros simulan a un
    paciente joven y saludable.

    Args:
        None

    Returns:
        None: La función ejecuta una aserción que verifica que la predicción
              sea "NO ENFERMO".

    Raises:
        AssertionError: Si la predicción no es "NO ENFERMO".
    """
    datos = {
        "edad": 25,
        "temperatura": 36.5,
        "frecuencia_cardiaca": 75,
        "dias_sintomas": 0,
        "dolor": 0,
    }
    assert predecir_estado(datos) == "NO ENFERMO"


def test_enfermedad_leve():
    """
    Prueba que valida la predicción correcta de una enfermedad leve.

    Esta función prueba el caso de un paciente con síntomas leves, incluyendo
    una ligera elevación de temperatura y frecuencia cardíaca, acompañados de
    dolor moderado y pocos días de síntomas.

    Args:
        None

    Returns:
        None: La función ejecuta una aserción que verifica que la predicción
              sea "ENFERMEDAD LEVE".

    Raises:
        AssertionError: Si la predicción no es "ENFERMEDAD LEVE".
    """
    datos = {
        "edad": 30,
        "temperatura": 37.8,
        "frecuencia_cardiaca": 90,
        "dias_sintomas": 2,
        "dolor": 3,
    }
    assert predecir_estado(datos) == "ENFERMEDAD LEVE"


def test_enfermedad_aguda():
    """
    Prueba que valida la predicción correcta de una enfermedad aguda.

    Esta función prueba el caso de un paciente con síntomas graves y agudos,
    incluyendo fiebre alta, elevada frecuencia cardíaca y dolor considerable.
    Simula una enfermedad de onset reciente pero seria.

    Args:
        None

    Returns:
        None: La función ejecuta una aserción que verifica que la predicción
              sea "ENFERMEDAD AGUDA".

    Raises:
        AssertionError: Si la predicción no es "ENFERMEDAD AGUDA".
    """
    datos = {
        "edad": 40,
        "temperatura": 39.4,
        "frecuencia_cardiaca": 125,
        "dias_sintomas": 4,
        "dolor": 8,
    }
    assert predecir_estado(datos) == "ENFERMEDAD AGUDA"


def test_enfermedad_cronica():
    """
    Prueba que valida la predicción correcta de una enfermedad crónica.

    Esta función prueba el caso de un paciente de edad avanzada con una
    enfermedad de larga duración (65 días de síntomas). A pesar de tener
    signos vitales relativamente estables, la duración prolongada de los
    síntomas indica una condición crónica.

    Args:
        None

    Returns:
        None: La función ejecuta una aserción que verifica que la predicción
              sea "ENFERMEDAD CRÓNICA".

    Raises:
        AssertionError: Si la predicción no es "ENFERMEDAD CRÓNICA".
    """
    datos = {
        "edad": 68,
        "temperatura": 37.0,
        "frecuencia_cardiaca": 88,
        "dias_sintomas": 65,
        "dolor": 5,
    }
    assert predecir_estado(datos) == "ENFERMEDAD CRÓNICA"
