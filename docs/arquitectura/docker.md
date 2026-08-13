# 🐳 RecorNet — Arquitectura de Contenedores con Docker

## 📝 Descripción general

Este documento define la estrategia de contenerización de **RecorNet** mediante **Docker** y **Docker Compose**. Docker se utiliza para garantizar la reproducibilidad del entorno de desarrollo y despliegue de todos los servicios de la plataforma: la base de datos PostgreSQL, la caché y broker Redis, los workers asíncronos de Celery (worker y beat) y la API REST de Flask. Cada servicio se ejecuta en un contenedor aislado con su propia configuración, volúmenes persistentes y red interna, de modo que cualquier miembro del equipo pueda levantar el sistema completo con un solo comando sin depender de instalaciones locales específicas.

## 🏗️ Arquitectura de contenedores

El sistema se compone de cinco servicios coordinados por `docker-compose.yml`, que comparte una red interna (`recornet-net`) para que los servicios se comuniquen por nombre de host, y volúmenes nombrados para la persistencia de datos.

```text
RecorNet/
├── backend/
│   ├── Dockerfile.worker         # Imagen del Celery worker
│   ├── Dockerfile.beat           # Imagen del Celery beat (planificador)
│   └── init.py
├── docker/
│   ├── postgres/
│   │   └── init-db.sql           # Inicialización de esquemas (opcional)
│   ├── redis/
│   │   └── redis.conf            # Configuración personalizada
│   ├── celery-worker/
│   │   └── Dockerfile            # Imagen alternativa del worker
│   └── celery-beat/
│       └── Dockerfile            # Imagen alternativa del beat
└── docker-compose.yml            # Orquestación de todos los servicios
```

### Diagrama de contenedores

```mermaid
flowchart LR
    subgraph "Servicios de datos"
        PG[(PostgreSQL<br/>postgres:16-alpine)]
        RD[(Redis<br/>redis:7-alpine)]
    end

    subgraph "Aplicación"
        API[API REST Flask<br/>uvicorn + gunicorn]
        WORK[worker<br/>Celery worker]
        BEAT[beat<br/>Celery beat]
    end

    API --> PG
    API --> RD
    WORK --> RD
    WORK --> PG
    BEAT --> RD
    WORK --> BEAT

    API -.-"Puerto 3000".-> EXT[Frontend web<br/>y app móvil]
```

## ⚙️ Servicios de Docker Compose

| Servicio | Imagen base | Función | Puerto | Volumen |
|----------|-------------|---------|--------|---------|
| `postgres` | `postgres:16-alpine` | Base de datos principal (usuarios, medicamentos, tratamientos, historial) | 5432 | `pgdata:/var/lib/postgresql/data` |
| `redis` | `redis:7-alpine` | Caché de estadísticas y broker de mensajes de Celery | 6379 | — (datos volátiles por diseño) |
| `worker` | Misma imagen que `api` | Procesamiento asíncrono: notificaciones push, carga de imágenes, estadísticas y reportes | — | `./backend:/app` |
| `beat` | Misma imagen que `api` | Planificador de tareas programadas: genera recordatorios de dosis según horarios | — | `./backend:/app` |

Los tres servicios de aplicación comparten la misma imagen de construcción (build con `Dockerfile`), lo que garantiza coherencia de dependencias entre la API y los workers.

## 📄 docker-compose.yml (estructura de referencia)

```yaml
version: "3.9"

services:
  postgres:
    image: postgres:16-alpine
    container_name: recornet-postgres
    restart: unless-stopped
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
      - ./docker/postgres:/docker-entrypoint-initdb.d
    networks:
      - recornet-net
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    container_name: recornet-redis
    restart: unless-stopped
    command: redis-server /usr/local/etc/redis/redis.conf
    ports:
      - "6379:6379"
    volumes:
      - ./docker/redis/redis.conf:/usr/local/etc/redis/redis.conf
    networks:
      - recorner-net
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5

  api:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: recornet-api
    ports:
      - "3000:3000"
    env_file:
      - .env
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    networks:
      - recornet-net

  worker:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: recornet-worker
    restart: unless-stopped
    command: celery -A src.main worker --loglevel=info --concurrency=2
    environment:
      - DATABASE_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@postgres:5432/${POSTGRES_DB}
      - REDIS_URL=redis://redis:6379/0
    volumes:
      - ./backend:/app
    depends_on:
      - api
    networks:
      - recorner-net

  beat:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: recornet-beat
    restart: unless-stopped
    command: celery -A src.main beat --loglevel=info
    environment:
      - DATABASE_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@postgres:5432/${POSTGRES_DB}
      - REDIS_URL=redis://redis:6379/0
    volumes:
      - ./backend:/app
    depends_on:
      - redis
    networks:
      - recorner-net

volumes:
  pgdata:

networks:
  recornet-net:
    driver: bridge
```


```

## 🔐 Variables de entorno (.env)

```env
# Base de datos
POSTGRES_DB=recornet_db
POSTGRES_USER=recornet_user
POSTGRES_PASSWORD=<contraseña-segura-generada>

# Aplicación
SECRET_KEY=<clave-secreta-para-JWT>
JWT_EXPIRATION_MINUTES=60
CLOUDINARY_URL=<url-de-cloudinary>
FIREBASE_CREDENTIALS_FILE=./credentials/firebase.json
```

> **Regla de seguridad:** el archivo `.env` nunca se sube al repositorio (está en `.gitignore`). Cada entorno (desarrollo, pruebas, producción) utiliza su propio archivo de variables.

## 🚀 Comandos esenciales

```bash
# Levantar toda la plataforma (posterior a docker compose build)
docker compose up -d

# Ver el estado de los contenedores
docker compose ps

# Ver logs en tiempo real de un servicio
docker compose logs -f worker

# Detener la plataforma sin perder datos
docker compose down

# Detener y eliminar volúmenes (BORRA la base de datos local)
docker compose down -v

# Reconstruir imágenes tras cambios en dependencias
docker compose build --no-cache

# Ejecutar un comando dentro de un contenedor
docker compose exec api flask db upgrade   # migraciones
docker compose exec api pytest             # pruebas del backend
docker compose exec postgres psql -U recornet_user -d recornet_db
```

## 📊 Ciclo de vida de los servicios

1. **Inicio ordenado:** Docker Compose arranca primero `postgres` y `redis`, espera sus *healthchecks* y solo entonces inicia `api`; `worker` y `beat` arrancan después, pues dependen de la API y del broker respectivamente.
2. **Desarrollo:** con el volumen `./backend:/app` montado, los cambios en el código Python se reflejan dentro del contenedor sin reconstruir la imagen (solo es necesario reiniciar el servicio afectado).
3. **Migraciones:** las migraciones de Flask-Migrate se ejecutan con `flask db upgrade` dentro del contenedor `api`, una vez que la base de datos está disponible.
4. **Planificación:** `beat` ejecuta el horario Celery que delega a `worker` las tareas de recordatorios, notificaciones push, estadísticas y reportes.

## ✅ Buenas prácticas aplicadas

1. **Imágenes alpine/slim** para reducir superficie de ataque y tamaño de imagen.
2. **Healthchecks** en los servicios de datos para un inicio ordenado y fiable.
3. **Volúmenes nombrados** (`pgdata`) para persistencia independiente del ciclo de vida del contenedor.
4. **Variables de entorno** para credenciales; nada se hardcodea en imágenes ni en `docker-compose.yml`.
5. **`restart: unless-stopped`** para que los servicios se recuperen de caídas del daemon.
6. **Red interna aislada** (`recornet-net`); solo la API expone puertos al host (3000).
7. **Dependencias declaradas** (`depends_on` con condición `service_healthy`) para evitar errores de arranque.

## 🔗 Relación con la arquitectura general

Docker es la capa de infraestructura que soporta los componentes documentados en `backend.md`: PostgreSQL como motor de persistencia con SQLAlchemy/Flask-Migrate, Redis como caché y broker de Celery, Celery Worker/Beat como sistema de procesamiento asíncrono y planificador, y la API de Flask como punto de entrada RESTful. Para la fase móvil, esta misma orquestación sirve al cliente de Capacitor, que solo necesita la API expuesta en el puerto 3000.

