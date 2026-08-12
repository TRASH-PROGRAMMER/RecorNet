# 🧠  Recornet - Arquitectura y Stack Tecnológico backend

## 📌 Descripción General
**RecorNet** es un software multiplataforma (Android y Web) diseñado para ayudar a los adultos mayores a cumplir correctamente con el tratamiento de sus medicamentos mediante recordatorios inteligentes, accesibles y fáciles de utilizar.

## 🏗️ Arquitectura General
El backend de **RecorNet** se compone de una API RESTful y un sistema de base de datos relacional (PostgreSQL) siguiendo la arquitectura de  clean architecture + hexagonal architecture.


## Componentes principales

1. 🟢 API / Gateway (Backend principal)

Tecnología: Python + Flask + Swagger + Uvicorn

**Funciones:**

- API REST

- Punto de entrada (API Gateway ligero)

- Autenticación

- Gestión de usuarios (adultos mayores y cuidadores)

- Gestión de familias

- Gestión de medicamentos y tratamientos

- Gestión de recordatorios inteligentes

- Gestión de notificaciones push

- Gestión de estadísticas

- Gestión de reportes

2. 🟢 Workers (Backend secundario)

Tecnología: Python + Celery

**Funciones:**

- Planificador

- Notificaciones Push

- Almacenamiento de imágenes

- Estadísticas

- Reportes

3. 🔔 Sistema de Notificaciones (Backend secundario)
Tecnología: Python + Firebase Cloud Messaging
**Funciones:**

- Notificaciones Push   

4. 💽 Sistema de Almacenamiento de Imágenes (Backend secundario)
Tecnología: Python + Cloudinary
**Funciones:**

- Almacenamiento de imágenes

5. 📈📊 Sistema de Estadísticas (Backend secundario)
Tecnología: Python + Redis
**Funciones:**

- Estadísticas

6. 🗒️ Sistema de Reportes (Backend secundario)
Tecnología: Python + PostgreSQL
**Funciones:**

- Reportes

7.🐳 Contenerización (Backend secundario)
Tecnología: Docker

**Funciones:**

- Contenerización de servicios (PostgreSQL, Redis, Celery Worker y Celery Beat)


Arquitectura: Clean Architecture + Hexagonal

## 📁 Estructura del proyecto arquitectura backend: Clean Architecture + Hexagonal:

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

## 📁 Estructura interna:

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

## Tecnologías asociadas:

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

 ## Base de Datos:

Motor: PostgreSQL
Contenerización: Docker
ORM: SQLAlchemy
Migraciones: Flask-Migrate
Funciones:
- Gestión de usuarios (adultos mayores y cuidadores).
- Gestión de medicamentos y tratamientos.
- Gestión de recordatorios inteligentes.
- Gestión de notificaciones push.
- Gestión de estadísticas.
- Gestión de reportes.
- diagrama entidad relacion:

```mermaid
erDiagram
    USERS ||--o| PROFILES : tiene
    USERS }o--o{ ROLES : asigna_via_USER_ROLES
    USERS ||--o{ CARE_RELATIONSHIPS : cuidador
    USERS ||--o{ CARE_RELATIONSHIPS : adulto_mayor
    USERS ||--o{ TREATMENTS : paciente
    USERS ||--o{ TREATMENTS : creado_por
    MEDICATIONS ||--o{ TREATMENTS : define
    TREATMENTS ||--o{ REMINDER_SCHEDULES : programa
    TREATMENTS ||--o{ DOSE_EVENTS : genera
    REMINDER_SCHEDULES ||--o{ DOSE_EVENTS : instancia
    USERS ||--o{ NOTIFICATIONS : recibe
    DOSE_EVENTS ||--o{ NOTIFICATIONS : origina
    USERS ||--o{ USER_DEVICES : posee
    USERS ||--o{ REPORTS : sujeto_o_autor

```

| Relación               | Tipo |
| ---------------------- | ---- |
| User → Profile         | 1:1  |
| User → Role            | N:M  |
| User → Service         | 1:N  |
| user → medicamnets     | 1:N  |
| user → treatments      | 1:N  |
| user → reminders       | 1:N  |
| User → Notification    | 1:N  |
| User → Statistics      | 1:N  |
| User → Report          | 1:N  |
| Profile → User         | 1:1  |
| Profile → Role         | 1:1  |
| Profile → Service      | 1:1  |
| Profile → Notification | 1:1  |
| Profile → Statistics   | 1:1  |
| Profile → Report       | 1:1  |
| Role → User            | 1:1  |
| Role → Profile         | 1:1  |
| Role → Service         | 1:1  |
| Role → Notification    | 1:1  |
| Role → Statistics      | 1:1  |
| Role → Report          | 1:1  |
| Service → User         | 1:1  |
| Service → Profile      | 1:1  |
| Service → Role         | 1:1  |
| Service → Notification | 1:1  |
| Service → Statistics   | 1:1  |
| Service → Report       | 1:1  |
| Notification → User    | 1:1  |
| Notification → Profile | 1:1  |
| Notification → Role    | 1:1  |
| Notification → Service | 1:1  |
| Statistics → User      | 1:1  |
| Statistics → Profile   | 1:1  |
| Statistics → Role      | 1:1  |
| Statistics → Service   | 1:1  |
| Report → User          | 1:1  |
| Report → Profile       | 1:1  |
| Report → Role          | 1:1  |
| Report → Service       | 1:1  |   

## Caché / Broker:

Motor: Redis, Celery Beat y Celery Worker 
Funciones:
- Planificador
- Estadísticas
- Reportes      
 

## Notificaciones Push:

Motor: Firebase Cloud Messaging
Funciones:
- Notificaciones Push   
 
## Almacenamiento de imágenes:

Motor: Cloudinary
Funciones:
- Almacenamiento de imágenes
 
## Estadísticas:

Motor: Redis
Funciones:
- Estadísticas
 
## Reportes:

Motor: PostgreSQL
Funciones:
- Reportes

## Docker:

Motor: Docker
Se utiliza Docker para facilitar despliegue y desarrollo:
Funciones:
- Contenerización de servicios (PostgreSQL, Redis, Celery Worker y Celery Beat)

## Comunicación entre servicios:

![alt text](https://github.com/RUDYPIO/Recornet/blob/main/docs/arquitectura/backend/diagrama-comunicacion-entre-servicios.png)

## Comunicación entre componentes:
![alt text](https://github.com/RUDYPIO/Recornet/blob/main/docs/arquitectura/backend/diagrama-comunicacion-entre-componentes.png)


✅ Conclusión

La arquitectura de  RecorNet se basa en la arquitectura de Clean Architecture + Hexagonal, que es una arquitectura que se enfoca en separar el código de negocio del código de infraestructura, lo que permite una mejor organización y mantenimiento del código.

Ser escalable
Mantener separación clara de responsabilidades
Permitir evolución hacia sistemas más complejos
Facilitar la comunicación entre componentes
Facilitar la comunicación entre servicios
Mantenimiento de la arquitectura
Mejora continua
Migración de la base de datos
Gestión de la caché
Gestión de la planificación
Gestión de las notificaciones push
Gestión de las estadísticas
Gestión de los reportes
Mejora de la seguridad y rendimiento
Seguridad de la aplicación y usuarios


