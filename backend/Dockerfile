FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar dependencias (asumiendo requirements.txt)
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY . .

# Comando por defecto (para desarrollo)
CMD ["flask", "run", "--host=0.0.0.0", "--port=3000"]
