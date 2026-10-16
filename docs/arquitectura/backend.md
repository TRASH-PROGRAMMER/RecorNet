# 🧠  Recornet - Arquitectura y Stack Tecnológico backend

## 📌 Descripción General
**RecorNet** es un software multiplataforma (Android y Web) diseñado para ayudar a los adultos mayores a cumplir correctamente con el tratamiento de sus medicamentos mediante recordatorios inteligentes, accesibles y fáciles de utilizar.

## 🏗️ Arquitectura General
El backend de **RecorNet** se compone de una API RESTful y un sistema de base de datos relacional (PostgreSQL) siguiendo la arquitectura de  clean architecture + hexagonal architecture.


## Componentes principales

1. 🟢 API / Gateway (Backend principal)

Tecnología: Python + Flask + Swagger + Gunicorn 

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

``mermaid
erDiagram
    USERS ||--o| PROFILES : tiene
    USERS ||--o{ USER_ROLES : recibe
    ROLES ||--o{ USER_ROLES : asigna
    USERS ||--o{ AUTH_SESSIONS : inicia
    USERS ||--o{ PASSWORD_RESET_TOKENS : recupera
    USERS ||--o| ACCESSIBILITY_PREFERENCES : configura
    USERS ||--o{ CARE_RELATIONSHIPS : cuidador
    USERS ||--o{ CARE_RELATIONSHIPS : adulto_mayor
    CARE_RELATIONSHIPS ||--o{ CARE_PERMISSIONS : delega
    USERS ||--o{ TREATMENTS : paciente
    USERS ||--o{ TREATMENTS : creado_por
    MEDICATIONS ||--o{ TREATMENTS : define
    TREATMENTS ||--o{ REMINDER_SCHEDULES : programa
    REMINDER_SCHEDULES ||--o{ REMINDER_TIMES : contiene
    TREATMENTS ||--o{ DOSE_EVENTS : genera
    TREATMENTS ||--o{ TREATMENT_REVISIONS : versiona
    TREATMENTS ||--o{ NOTIFICATION_POLICIES : regula
    DOSE_EVENTS ||--o{ NOTIFICATIONS : origina
    DOSE_EVENTS ||--o{ DOSE_STATUS_TRANSITIONS : historiza
    NOTIFICATIONS ||--o{ NOTIFICATION_DELIVERIES : intenta
    USERS ||--o{ USER_DEVICES : posee
    USERS ||--o{ CONSENTS : concede
    USERS ||--o{ SYNC_OPERATIONS : encola
    USERS ||--o{ AUDIT_EVENTS : ejecuta
    USERS ||--o{ REPORTS : sujeto
    USERS ||--o{ REPORTS : autor
    USERS ||--o{ STATISTICS_SNAPSHOTS : conserva
    REMINDER_SCHEDULES ||--o{ DOSE_EVENTS : instancia
```


## Tablas, relaciones y descripción

| Tabla | Clave | Descripción |
|-------|-------|-------------|
| `users` | `id` (PK) | Usuario principal: adulto mayor o cuidador. Datos de identidad y credenciales (contraseña como hash). Eliminado con soft delete. No contiene una columna `role`: la asignación se centraliza en `user_roles`. |
| `profiles` | `user_id` (PK/FK) | Extensión opcional del usuario con datos adicionales (preferencias, foto, ubicación). |
| `accessibility_preferences` | `user_id` (PK/FK) | Preferencias accesibles explícitas: escala tipográfica, alto contraste, voz, hápticos y reducción de movimiento. |
| `roles` | `id` (PK) | Catálogo de roles: `patient` (adulto mayor), `caregiver` (cuidador). Un eventual rol `admin` interno debe aprobarse explícitamente por producto antes de habilitarse. |
| `user_roles` | `(user_id, role_id)` (PK compuesta) | Tabla puente N:M entre usuarios y roles; permite evolución futura sin cambiar el modelo. |
| `auth_sessions` | `id` (PK) | Sesiones renovables y revocables; conserva hash del token de renovación, dispositivo y vencimiento. |
| `password_reset_tokens` | `id` (PK) | Token de recuperación de acceso almacenado como hash, con vencimiento y consumo único. |
| `medications` | `id` (PK) | Catálogo del medicamento: nombre, descripción, forma, fabricante, estado y fotografía. No contiene dosis ni frecuencia porque dependen de la prescripción del paciente. |
| `treatments` | `id` (PK) | Prescripción que une un paciente, un cuidador autor y un medicamento con fechas de inicio/fin, dosis e instrucciones. Cada modificación incrementa `version`. |
| `treatment_revisions` | `id` (PK) | Historial de versiones de tratamiento, con autor y cambios; apoya la resolución explícita de conflictos. |
| `reminder_schedules` | `id` (PK) | Regla de recurrencia asociada a un tratamiento. FK `treatment_id`; conserva zona horaria y días de la semana. |
| `reminder_times` | `id` (PK) | Hora(s) del día para cada programación; evita almacenar horarios en JSON y permite validarlos e indexarlos. |
| `notification_policies` | `id` (PK) | Política de reintentos y escalamiento de un tratamiento o usuario: intervalo, máximo de intentos y umbral de pendiente. |
| `dose_events` | `id` (PK) | Instancias de dosis programadas. FK `schedule_id` y `treatment_id`; incluye `idempotency_key` única. El estado clínico de la toma y el estado de sincronización se conservan en columnas separadas. |
| `dose_status_transitions` | `id` (PK) | Transición inmutable entre estados de una dosis, con actor, motivo y marca temporal. |
| `notifications` | `id` (PK) | Registro de avisos locales o push. FK `dose_event_id` y `recipient_user_id`, con canal, estado de entrega y payload. |
| `notification_deliveries` | `id` (PK) | Intento individual de enviar una notificación a un dispositivo; registra reintentos, proveedor, entrega o fallo. |
| `user_devices` | `id` (PK) | Dispositivos registrados con tokens FCM, sistema operativo y preferencias de notificación. FK `user_id`. |
| `consents` | `id` (PK) | Evidencia temporal de consentimiento o revocación para tratamiento de datos, avisos y guía por voz. |
| `reports` | `id` (PK) | Reportes de seguimiento generados por el cuidador o por el sistema. FK explícitas `subject_user_id` y `created_by_user_id`. |
| `statistics_snapshots` | `id` (PK) | Snapshot histórico opcional de estadísticas (adherencia, rachas), complementario a la caché de Redis. |
| `sync_operations` | `id` (PK) | Cola durable de operaciones offline con idempotencia, reintentos y último error conocido. |
| `audit_events` | `id` (PK) | Registro inmutable de acciones relevantes de seguridad, cambios de estado, acceso y entregas. |
| `care_permissions` | `id` (PK) | Permiso individual, revocable y auditable dentro de una relación cuidador-adulto mayor. |


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


