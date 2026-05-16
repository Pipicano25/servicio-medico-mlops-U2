# Servicio Médico con Flask y Docker

**Equipo**:
|Nombres |
|---------|
|Anderson Daniel Pipicano Ruiz|
|Fredy Yamid Alvarez Palechor |

## 1. Finalidad de la solución

Este proyecto implementa una solución mediante un servicio web que simula el uso de un modelo clínico.

El objetivo es que un médico pueda ingresar datos básicos de un paciente y recibir uno de los siguientes estados:

- `NO ENFERMO`
- `ENFERMEDAD LEVE`
- `ENFERMEDAD AGUDA`
- `ENFERMEDAD CRÓNICA`

En el desarrollo del modelo de machine learning se realizó una simulación del comportamiento del modelo se simula mediante una función llamada `predecir_estado`, ubicada en el archivo `model/model.py`.

> Importante: esta solución es académica, demostrativa y como se puede implementar una solución a futuro para dicha problemática, esto no debería reemplazar el criterio médico ni debe usarse para diagnóstico real.

---

## 2. Estructura del proyecto

```text
servicio_medico_flask/
│
├── app.py                      # Aplicación Flask y función simulada del modelo
├── requirements.txt            # Dependencias del proyecto
├── Dockerfile                  # Archivo para construir la imagen Docker
├── README.md                   # Instrucciones de uso
├── .dockerignore               # Archivos ignorados por Docker
│
├── docs/
│   └── Pipeline de MLOps.pdf   # Descripción de un Pipeline de MLOps
│
├── templates/
│   └── index.html              # Página web sencilla para ingresar datos
│
├── static/
│   └── style.css               # Estilos de la página web
│
├── model/
│   └── model.py                # Módulo de predicción clínica simulada
│
├── utils/
│   └── convertir_valores.py    # Módulo de conversión de valores para validación y normalización de datos
│
└── tests/
    └── test_predict.py         # Pruebas básicas de la función de predicción
```

---

## 3. Variables de entrada

La función recibe 5 variables para hacer la simulación más real referente al diagnóstico:

| Variable              | Descripción                             | Ejemplo |
| --------------------- | --------------------------------------- | ------- |
| `edad`                | Edad del paciente en años               | `45`    |
| `temperatura`         | Temperatura corporal en grados Celsius  | `38.2`  |
| `frecuencia_cardiaca` | Latidos por minuto                      | `105`   |
| `dias_sintomas`       | Días que lleva el paciente con síntomas | `3`     |
| `dolor`               | Nivel de dolor de 0 a 10                | `4`     |

---

## 4. Lógica simulada del modelo

La función `predecir_estado` retorna un estado según reglas sencillas:

- Retorna `ENFERMEDAD CRÓNICA` si los síntomas llevan mucho tiempo o existe persistencia clínica.
- Retorna `ENFERMEDAD AGUDA` si hay fiebre alta, frecuencia cardiaca muy elevada o dolor intenso reciente.
- Retorna `ENFERMEDAD LEVE` si hay síntomas moderados sin señales de severidad alta.
- Retorna `NO ENFERMO` si no hay señales relevantes en los valores ingresados.

Ejemplos que permiten obtener cada estado:

| Estado esperado      | Edad | Temperatura | Frecuencia cardiaca | Días síntomas | Dolor |
| -------------------- | ---: | ----------: | ------------------: | ------------: | ----: |
| `NO ENFERMO`         |   25 |        36.5 |                  75 |             0 |     0 |
| `ENFERMEDAD LEVE`    |   30 |        37.8 |                  90 |             2 |     3 |
| `ENFERMEDAD AGUDA`   |   40 |        39.4 |                 125 |             4 |     8 |
| `ENFERMEDAD CRÓNICA` |   68 |        37.0 |                  88 |            65 |     5 |

---

## 5. Ejecutar sin Docker

### 5.1. Crear entorno virtual

En Windows PowerShell:

```bash
python -m venv venv
```

```bash
.\venv\Scripts\activate
```

En Linux/Mac:

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

### 5.2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5.3. Ejecutar la aplicación

```bash
python app.py
```

Luego abrir en el navegador:

```text
http://localhost:5000
```

---

## 6. Construir y ejecutar con Docker

### 6.1. Construir la imagen

Desde la carpeta del proyecto:

```bash
docker build -t servicio-medico-flask .
```

### 6.2. Ejecutar el contenedor

```bash
docker run -p 5000:5000 servicio-medico-flask
```

Luego abrir en el navegador:

```text
http://localhost:5000
```

---

## 7. Usar el servicio desde la página web

1. Abra `http://localhost:5000`.
2. Ingrese los datos del paciente.
3. Presione el botón **Obtener respuesta**.
4. El sistema mostrará uno de los estados definidos.

---

## 8. Usar el servicio desde API

El servicio también expone un endpoint tipo API:

```text
POST http://localhost:5000/predecir
```

### Ejemplo con curl

```bash
curl -X POST http://localhost:5000/predecir \
  -H "Content-Type: application/json" \
  -d '{
    "edad": 40,
    "temperatura": 39.4,
    "frecuencia_cardiaca": 125,
    "dias_sintomas": 4,
    "dolor": 8
  }'
```

### Ejemplo con curl en consola

```bash
curl -X POST http://localhost:5000/predecir -H "Content-Type: application/json" -d "{\"edad\":40,\"temperatura\":39.4,\"frecuencia_cardiaca\":125,\"dias_sintomas\":4,\"dolor\":8}"
```

### Respuesta esperada

```json
{
  "estado": "ENFERMEDAD AGUDA",
  "estados_posibles": [
    "NO ENFERMO",
    "ENFERMEDAD LEVE",
    "ENFERMEDAD AGUDA",
    "ENFERMEDAD CRÓNICA"
  ],
  "entrada": {
    "edad": 40,
    "temperatura": 39.4,
    "frecuencia_cardiaca": 125,
    "dias_sintomas": 4,
    "dolor": 8
  },
  "advertencia": "Resultado simulado. No reemplaza valoración médica profesional."
}
```

---

## 9. Probar que la función retorna todos los estados

Se incluyen pruebas unitarias en la carpeta `tests`.

Para ejecutarlas:

```bash
pytest
```

Estas pruebas validan que la función puede retornar los cuatro estados requeridos.

---

## 10. Endpoints disponibles

| Endpoint    | Método | Descripción                                       |
| ----------- | ------ | ------------------------------------------------- |
| `/`         | GET    | Muestra formulario web                            |
| `/`         | POST   | Recibe datos desde formulario y muestra resultado |
| `/predecir` | POST   | Recibe JSON y retorna predicción en formato JSON  |
| `/salud`    | GET    | Verifica que el servicio esté activo              |

---
