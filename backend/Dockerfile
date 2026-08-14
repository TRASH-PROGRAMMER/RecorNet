FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias del sistema necesarias para psycopg2
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar e instalar dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY . .

# Exponer el puerto de la API
EXPOSE 3000

# Variables de entorno por defecto
ENV FLASK_APP=src.main:create_app
ENV FLASK_ENV=development

# Comando por defecto: servidor de desarrollo Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=3000"]
