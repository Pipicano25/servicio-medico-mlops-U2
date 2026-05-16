# Servicio Médico con Flask y Docker

**Equipo**:
|Nombres |
|---------|
|Anderson Daniel Pipicano Ruiz|
|Fredy Yamid Alvarez Palechor |

## 1. Problema

Actualmente, el sector salud genera grandes volúmenes de información provenientes de historias
clínicas, registros hospitalarios, laboratorios y plataformas epidemiológicas, creando la posibilidad de
implementar soluciones inteligentes que apoyen el diagnóstico médico y mejoren la toma de
decisiones clínicas. En este contexto, se propone desarrollar una solución basada en Machine Learning
y MLOps capaz de predecir la posible presencia de enfermedades comunes y huérfanas a partir de
síntomas, antecedentes y datos clínicos de los pacientes, integrando información proveniente de
múltiples fuentes médicas. La solución busca reducir diagnósticos tardíos o incorrectos, optimizar la
priorización de pacientes y mejorar la asignación de recursos médicos mediante modelos predictivos
confiables, monitoreados y capaces de adaptarse continuamente a nuevos datos y cambios
epidemiológicos.

El pipeline integra procesos de adquisición de datos, aseguramiento de calidad, ingeniería de
características, entrenamiento de modelos, despliegue de servicios inteligentes y monitoreo continuo,
permitiendo construir una solución escalable, reproducible y adaptable a nuevos datos clínicos.

## 2. Proposito

El objetivo es construir un sistema de Machine Learning capaz de predecir, a partir de síntomas y datos clínicos de un paciente, la posible presencia de enfermedades tanto comunes (muchos datos disponibles) como huérfanas (muy pocos datos disponibles).

Debido a la naturaleza médica del problema, el pipeline debe considerar aspectos de calidad de datos, interpretabilidad, privacidad, actualización continua y monitoreo clínico.

Reducir el riesgo clínico y mejorar la toma de decisiones médicas mediante la detección temprana y automatizada de posibles enfermedades (comunes y huérfanas) a partir de datos de síntomas y registros clínicos, optimizando recursos del sistema de salud y mejorando la precisión diagnóstica.

## 3. Finalidad de la solución

Este proyecto implementa una solución mediante un servicio web que simula el uso de un modelo clínico.

El objetivo es que un médico pueda ingresar datos básicos de un paciente y recibir uno de los siguientes estados:

- `NO ENFERMO`
- `ENFERMEDAD LEVE`
- `ENFERMEDAD AGUDA`
- `ENFERMEDAD CRÓNICA`

En el desarrollo del modelo de machine learning se realizó una simulación del comportamiento del modelo se simula mediante una función llamada `predecir_estado`, ubicada en el archivo `model/model.py`.

> Importante: esta solución es académica, demostrativa y como se puede implementar una solución a futuro para dicha problemática, esto no debería reemplazar el criterio médico ni debe usarse para diagnóstico real.

---

## 4. Estructura del proyecto

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
