# Imagen base liviana con Python
FROM python:3.11-slim

# Evita archivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el proyecto
COPY . .

# Puerto usado por Flask/Gunicorn
EXPOSE 5000

# Comando de producción usando Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
