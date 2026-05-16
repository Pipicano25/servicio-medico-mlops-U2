"""
Aplicación Flask para un servicio médico simulado.

Este módulo define un servicio web que recibe datos de salud mediante un
formulario HTML o una petición JSON, y utiliza la función predecir_estado
para determinar el estado de salud del paciente.

Funciones:
    home: Renderiza la página principal y procesa el formulario HTML.
    predecir_api: Expone un endpoint REST para recibir datos JSON y devolver
        la predicción en formato JSON.
    salud: Endpoint de verificación de estado del servicio.
"""

from flask import Flask, request, jsonify, render_template
from model.model import predecir_estado

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    """Renderiza la interfaz web y procesa el formulario de predicción.

    Si la petición es POST, se extraen los datos de salud del formulario,
    se llama a predecir_estado y se muestran los resultados en la plantilla
    HTML.

    Returns:
        str: Contenido HTML renderizado para la página principal.
    """
    resultado = None
    error = None

    if request.method == "POST":
        try:
            datos = {
                "edad": request.form.get("edad"),
                "temperatura": request.form.get("temperatura"),
                "frecuencia_cardiaca": request.form.get("frecuencia_cardiaca"),
                "dias_sintomas": request.form.get("dias_sintomas"),
                "dolor": request.form.get("dolor"),
            }
            resultado = predecir_estado(datos)
        except ValueError as exc:
            error = str(exc)

    return render_template("index.html", resultado=resultado, error=error)


@app.route("/predecir", methods=["POST"])
def predecir_api():
    """Endpoint REST que recibe datos JSON y retorna la predicción.

    La solicitud debe contener un objeto JSON con las claves:
    edad, temperatura, frecuencia_cardiaca, dias_sintomas y dolor.

    Returns:
        Response: Respuesta JSON con la predicción y metadatos.

    Raises:
        ValueError: Si los datos de entrada no son válidos.
    """
    try:
        datos = request.get_json(force=True)
        resultado = predecir_estado(datos)
        return (
            jsonify(
                {
                    "estado": resultado,
                    "estados_posibles": [
                        "NO ENFERMO",
                        "ENFERMEDAD LEVE",
                        "ENFERMEDAD AGUDA",
                        "ENFERMEDAD CRÓNICA",
                    ],
                    "entrada": datos,
                    "advertencia": "Resultado simulado. No reemplaza valoración médica profesional.",
                }
            ),
            200,
        )
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400
    except Exception as exc:
        return jsonify({"error": "Solicitud inválida", "detalle": str(exc)}), 400


@app.route("/salud", methods=["GET"])
def salud():
    """Devuelve el estado de disponibilidad del servicio.

    Returns:
        Response: JSON con el estado del servicio y el nombre del modelo.
    """
    return jsonify({"status": "ok", "servicio": "modelo-medico-simulado"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
