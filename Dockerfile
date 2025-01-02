# Utilizar una imagen base de Python
FROM python:3.9-slim

# Instalar make y otras herramientas necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    make \
    && rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de tu proyecto al contenedor
COPY . /app

# Ejecutar el comando make para configurar el entorno
RUN make install

# Exponer el puerto de Flask (por defecto 5000)
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["make", "run"]
