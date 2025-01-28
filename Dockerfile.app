# Utilizar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos necesarios para la aplicación
COPY requirements-app.txt /app/
RUN pip install --no-cache-dir -r requirements-app.txt

COPY . /app

# Exponer el puerto de Flask (por defecto 5000)
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app-desacoplada.py"]
