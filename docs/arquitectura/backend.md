# 🧠  Recornet - Arquitectura y Stack Tecnológico backend

## 📌 Descripción General
**RecorNet** es un software multiplataforma (Android, iOS y Web) diseñado para ayudar a los adultos mayores a cumplir correctamente con el tratamiento de sus medicamentos mediante recordatorios inteligentes, accesibles y fáciles de utilizar.

## 🏗️ Arquitectura General
El backend de **RecorNet** se compone de una API RESTful y un sistema de base de datos relacional (PostgreSQL) siguiendo la arquitectura de  clean architecture + hexagonal architecture.


## Componentes principales
1. 🟢 API / Gateway (Backend principal)

Tecnología: Python + Flask + Swagger + Uvicorn

**Funciones:**

API REST

Punto de entrada (API Gateway ligero)

Autenticación

Gestión de usuarios (adultos mayores y cuidadores)

Gestión de familias

Gestión de medicamentos y tratamientos

Gestión de recordatorios inteligentes

Gestión de notificaciones push

Gestión de estadísticas

Gestión de reportes

2. 🟢 Workers (Backend secundario)
Tecnología: Python + Celery
Funciones:

Planificador

Notificaciones Push

Almacenamiento de imágenes

Estadísticas

Reportes

Arquitectura: Clean Architecture + Hexagonal

### 📁 Estructura del proyecto arquitectura backend: Clean Architecture + Hexagonal
```text
backend/
├── api/                # Flask API REST (Clean Architecture + Hexagonal)      
├── shared/             # (Opcional) utilidades compartidas
├── docker/             # Docker files
├── docker-compose.yml      # Orquestación de servicios
│
├── requirements.txt     # Dependencias de la aplicación
│
├── .env.example         # Ejemplo de archivo de variables de entorno
│
├── .gitignore           # Archivo de ignorados
│
└── README.md            # Descripción del proyecto
```

## 📁 Estructura interna

```text
backend/ (python + flask + swagger + uvicorn)       
│
├── src/
│
│   ├── domain/                              # Núcleo del dominio
│   │
│   │   ├── entities/
│   │   │   ├── user.py
│   │   │   ├── caregiver.py
│   │   │   ├── elderly.py
│   │   │   ├── medication.py
│   │   │   ├── treatment.py
│   │   │   ├── reminder.py
│   │   │   ├── medication_history.py
│   │   │   ├── notification.py
│   │   │   └── statistics.py
│   │   │
│   │   ├── value_objects/
│   │   │   ├── dosage.py
│   │   │   ├── schedule.py
│   │   │   ├── medication_image.py
│   │   │   └── reminder_time.py
│   │   │
│   │   ├── services/
│   │   │   ├── adherence_service.py
│   │   │   ├── reminder_service.py
│   │   │   ├── statistics_service.py
│   │   │   └── notification_service.py
│   │   │
│   │   ├── repositories/
│   │   │   ├── user_repository.py
│   │   │   ├── medication_repository.py
│   │   │   ├── treatment_repository.py
│   │   │   ├── reminder_repository.py
│   │   │   ├── history_repository.py
│   │   │   └── statistics_repository.py
│   │   │
│   │   ├── ports/
│   │   │   ├── cloudinary_port.py
│   │   │   ├── firebase_port.py
│   │   │   ├── redis_port.py
│   │   │   ├── jwt_port.py
│   │   │   └── email_port.py
│   │   │
│   │   └── exceptions/
│   │
│   ├── application/
│   │
│   │   ├── use_cases/
│   │   │
│   │   ├── auth/
│   │   ├── users/
│   │   ├── caregivers/
│   │   ├── elderly/
│   │   ├── medications/
│   │   ├── treatments/
│   │   ├── reminders/
│   │   ├── notifications/
│   │   ├── statistics/
│   │   ├── dashboard/
│   │   └── reports/
│   │
│   │   ├── dto/
│   │   │
│   │   ├── commands/
│   │   │
│   │   ├── queries/
│   │   │
│   │   └── mappers/
│   │
│   ├── infrastructure/
│   │
│   │   ├── api/
│   │   │
│   │   ├── controllers/
│   │   ├── routes/
│   │   ├── middlewares/
│   │   ├── validators/
│   │   ├── serializers/
│   │   └── schemas/
│   │
│   │   ├── persistence/
│   │   │
│   │   ├── models/
│   │   ├── repositories/
│   │   ├── migrations/
│   │   ├── database.py
│   │   └── seed.py
│   │
│   │   ├── cache/
│   │   │
│   │   └── redis.py
│   │
│   │   ├── cloud/
│   │   │
│   │   ├── firebase/
│   │   │   └── firebase_service.py
│   │   │
│   │   ├── cloudinary/
│   │   │   └── cloudinary_service.py
│   │   │
│   │   └── jwt/
│   │       └── jwt_service.py
│   │
│   │   ├── workers/
│   │   │
│   │   ├── celery.py
│   │   ├── reminder_worker.py
│   │   ├── notification_worker.py
│   │   ├── report_worker.py
│   │   └── statistics_worker.py
│   │
│   │   ├── scheduler/
│   │   │
│   │   └── celery_beat.py
│   │
│   │   └── logging/
│   │
│   ├── config/
│   │
│   │   ├── settings.py
│   │   ├── dependencies.py
│   │   ├── swagger.py
│   │   ├── celery_config.py
│   │   └── security.py
│   │
│   ├── docs/
│   │
│   │   └── openapi/
│   │
│   ├── shared/
│   │
│   │   ├── constants/
│   │   ├── enums/
│   │   ├── helpers/
│   │   ├── utils/
│   │   ├── decorators/
│   │   ├── exceptions/
│   │   └── responses/
│   │
│   └── main.py
│
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── e2e/
│   └── fixtures/
│
├── .env
├── .env.example
├── requirements.txt
├── Docker/
│   ├── postgres/
│   ├── redis/
│   ├── celery-worker/
│   └── celery-beat/
│
├── docker-compose.yml
├── README.md
└── .gitignore
```

## Tecnologías asociadas

| Componente                 | Tecnología                                              |
| -------------------------- | ------------------------------------------------------- |
| Framework Backend          | Flask                                                   |
| Servidor WSGI              | Gunicorn                                                |
| Base de datos              | PostgreSQL                                              |
| ORM                        | SQLAlchemy                                              |
| Migraciones                | Flask-Migrate                                           |
| Arquitectura               | Clean Architecture + Hexagonal                          |
| Autenticación              | JWT                                                     |
| Caché / Broker             | Redis                                                   |
| Procesamiento asíncrono    | Celery                                                  |
| Planificador               | Celery Beat                                             |
| Notificaciones Push        | Firebase Cloud Messaging                                |
| Almacenamiento de imágenes | Cloudinary                                              |
| Documentación API          | Swagger                                                 |
| Validación                 | Pydantic                                                |
| Pruebas                    | Pytest                                                  |
| Contenedores               | Docker (PostgreSQL, Redis, Celery Worker y Celery Beat) |


## Funciones:
- Gestión de usuarios (adultos mayores y cuidadores).
- Gestión de medicamentos y tratamientos.
- Gestión de recordatorios inteligentes.
- Gestión de notificaciones push.
- Gestión de estadísticas.
- Gestión de reportes.


