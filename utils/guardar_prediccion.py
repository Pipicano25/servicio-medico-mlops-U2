import json
import os
from datetime import datetime

# Ruta absoluta del archivo actual: utils/historial.py
RUTA_ARCHIVO_ACTUAL = os.path.abspath(__file__)

# Ruta de la carpeta utils/
RUTA_UTILS = os.path.dirname(RUTA_ARCHIVO_ACTUAL)

# Ruta raíz del proyecto
# Como historial.py está dentro de utils/, subimos un nivel
RUTA_PROYECTO = os.path.dirname(RUTA_UTILS)

# Ruta de la carpeta data/
RUTA_DATA = os.path.join(RUTA_PROYECTO, "data")

# Ruta final del archivo JSON
RUTA_HISTORIAL = os.path.join(RUTA_DATA, "historial_predicciones.json")

print(f"Ruta del archivo de historial: {RUTA_HISTORIAL}")

CATEGORIAS = [
    "NO ENFERMO",
    "ENFERMEDAD LEVE",
    "ENFERMEDAD AGUDA",
    "ENFERMEDAD CRÓNICA",
    "ENFERMEDAD TERMINAL",
]


def crear_historial():
    """
    Guarda el historial completo en el archivo JSON.
    """
    os.makedirs(os.path.dirname(RUTA_HISTORIAL), exist_ok=True)
    print(f"Creando archivo de historial en: {RUTA_HISTORIAL}")

    if not os.path.exists(RUTA_HISTORIAL):
        with open(RUTA_HISTORIAL, "w", encoding="utf-8") as archivo:
            json.dump([], archivo, indent=4, ensure_ascii=False)

        print(f"Archivo creado en: {RUTA_HISTORIAL}")
    else:
        print(f"El archivo ya existe en: {RUTA_HISTORIAL}")


def cargar_historial():
    """
    Carga el historial de predicciones desde un archivo JSON.
    Si el archivo no existe, retorna una lista vacía.
    """
    if not os.path.exists(RUTA_HISTORIAL):
        return []

    with open(RUTA_HISTORIAL, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_historial(historial):
    """
    Guarda el historial completo en el archivo JSON.
    """
    os.makedirs(os.path.dirname(RUTA_HISTORIAL), exist_ok=True)

    with open(RUTA_HISTORIAL, "w", encoding="utf-8") as archivo:
        json.dump(historial, archivo, indent=4, ensure_ascii=False)


def registrar_prediccion(estado, datos_entrada):
    """
    Registra una nueva predicción realizada por el médico.
    """
    historial = cargar_historial()
    print(f"Historial actual antes de agregar nueva predicción: {historial}")
    nueva_prediccion = {
        "estado": estado,
        "datos_entrada": datos_entrada,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    print(f"Registrando nueva predicción: {nueva_prediccion}")

    historial.append(nueva_prediccion)

    guardar_historial(historial)


def obtener_reporte():
    """
    Genera un reporte con:
    - Total de predicciones por categoría.
    - Últimas 5 predicciones.
    - Fecha de la última predicción.
    """
    historial = cargar_historial()

    total_por_categoria = {}

    for categoria in CATEGORIAS:
        total_por_categoria[categoria] = 0

    for prediccion in historial:
        estado = prediccion["estado"]
        if estado in total_por_categoria:
            total_por_categoria[estado] += 1

    ultimas_5 = historial[-5:]
    ultimas_5.reverse()

    if historial:
        fecha_ultima_prediccion = historial[-1]["fecha"]
    else:
        fecha_ultima_prediccion = None

    reporte = {
        "total_predicciones": len(historial),
        "total_por_categoria": total_por_categoria,
        "ultimas_5_predicciones": ultimas_5,
        "fecha_ultima_prediccion": fecha_ultima_prediccion,
    }

    return reporte


crear_historial()
