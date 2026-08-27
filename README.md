# RecorNet

Software multiplataforma de recordatorios inteligentes de medicamentos para adultos mayores y cuidadores.

## Descripción general

RecorNet es una aplicación web y móvil diseñada para ayudar a los adultos mayores a cumplir correctamente con su tratamiento médico mediante recordatorios accesibles, gestión de medicamentos y seguimiento de adherencia. La plataforma contempla dos roles principales: adulto mayor y cuidador, con permisos y flujos diferenciados.

## Objetivo

Desarrollar una solución multiplataforma accesible que permita:
- Registrar y administrar medicamentos con su información clínica.
- Programar recordatorios inteligentes multisensoriales.
- Confirmar, posponer u omitir tomas con historial trazable.
- Consultar estadísticas de adherencia y seguimiento del tratamiento.
- Apoyar a cuidadores en la supervisión remota del tratamiento.

## Problemas que resuelve

- Olvido en la toma de medicamentos por polimedicación o deterioro cognitivo.
- Confusión entre medicamentos, dosis y horarios.
- Incumplimiento de horarios de medicación.
- Falta de visibilidad sobre la adherencia al tratamiento.
- Dificultad de adultos mayores para usar herramientas tecnológicas.
- Ausencia de canales accesibles de seguimiento para cuidadores.

## Público objetivo

- **Adulto mayor**: usuario principal. Confirma tomas, consulta historial, visualiza estadísticas y recibe recordatorios accesibles.
- **Cuidador**: usuario secundario. Registra y administra medicamentos, programa horarios, supervisa el cumplimiento y recibe alertas de dosis pendientes.

## Características principales

### Rol: Adulto Mayor
- Inicio de sesión seguro.
- Visualización de medicamentos registrados.
- Recordatorios con alarma sonora, mensaje de voz, vibración y alerta visual.
- Confirmación de toma, marcado de pendiente u omisión.
- Consulta de historial de tomas.
- Visualización de estadísticas de adherencia.
- Configuración de accesibilidad (tamaño de fuente, contraste, voz, hapticos).

### Rol: Cuidador
- Inicio de sesión seguro.
- Registro, edición y eliminación de medicamentos.
- Programación de horarios, dosis y duración del tratamiento.
- Carga de fotografías de medicamentos.
- Consulta del historial de tomas del adulto mayor.
- Visualización de estadísticas y adherencia.
- Alertas cuando una dosis queda pendiente.

### Funcionalidades comunes
- Recuperación y cambio de contraseña.
- Cierre de sesión seguro.
- Interfaz accesible e intuitiva.
- Multiplataforma: Web y Android.

## Accesibilidad

RecorNet adopta principios de Diseño Universal y WCAG 2.2:
- Tipografía ampliable y alto contraste.
- Botones grandes y navegación sencilla.
- Compatibilidad con lectores de pantalla.
- Mensajes de voz y vibración en recordatorios.
- Alertas redundantes: visual, sonora, voz y háptica.

## Arquitectura

El proyecto sigue **Clean Architecture + Hexagonal Architecture** con separación estricta de responsabilidades.

### Backend
- **Framework**: Python 3.11 + Flask.
- **API REST**: Flask + Flasgger (Swagger).
- **ORM**: SQLAlchemy 2.0 + Flask-Migrate (Alembic).
- **Auth**: JWT (PyJWT) + bcrypt.
- **Cola/Planificación**: Celery 5.5 + Celery Beat + Redis 7.
- **Push**: Firebase Cloud Messaging.
- **Imágenes**: Cloudinary.
- **Validación**: Pydantic + Marshmallow.
- **WSGI**: Gunicorn.

#### Estructura del backend
```
backend/
├── src/
│   ├── domain/
│   │   ├── entities/           # Entidades del dominio (User, Medication, Treatment, DoseEvent, Notification, CareRelationship, etc.)
│   │   ├── value_objects/      # Value objects (Frequency, Interval, Dosage, ReminderTime, IdempotencyKey)
│   │   ├── repositories/       # Repositorios abstractos
│   │   ├── ports/              # Puertos abstractos (JWT, Cloudinary)
│   │   ├── services/           # Servicios de dominio
│   │   └── exceptions/         # Excepciones de dominio
│   ├── application/
│   │   ├── use_cases/          # Casos de uso (auth, medications)
│   │   └── dto/                # Objetos de transferencia
│   ├── infrastructure/
│   │   ├── api/                # Rutas, middlewares, validadores, serializers
│   │   ├── persistence/        # Modelos SQLAlchemy y repositorios concretos
│   │   ├── cache/              # Integración con Redis
│   │   ├── cloud/              # Integración con Cloudinary
│   │   └── workers/            # Tareas asíncronas Celery
│   ├── config/                 # Configuración de la aplicación
│   └── shared/                 # Enums, excepciones compartidas, respuestas
├── tests/
│   ├── unit/                   # Pruebas unitarias
│   └── integration/            # Pruebas de integración
├── requirements.txt
├── Dockerfile
└── .env.example
```

### Frontend Web
- **Framework**: Vue 3 + TypeScript.
- **Router**: Vue Router.
- **Estado**: Pinia.
- **HTTP**: Axios.
- **CSS**: Tailwind CSS.
- **Push**: Firebase Cloud Messaging.

#### Estructura del frontend web
```
frontend/
└── web/
    ├── src/
    │   ├── assets/             # Imágenes, íconos, fuentes
    │   ├── components/         # Componentes reutilizables
    │   │   ├── common/
    │   │   ├── forms/
    │   │   ├── charts/
    │   │   ├── notifications/
    │   │   └── accessibility/
    │   ├── views/              # Páginas
    │   │   ├── auth/
    │   │   ├── dashboard/
    │   │   ├── medications/
    │   │   ├── reminders/
    │   │   ├── statistics/
    │   │   ├── caregivers/
    │   │   ├── elderly/
    │   │   └── profile/
    │   ├── layouts/            # Layouts generales
    │   ├── router/
    │   ├── store/              # Pinia stores
    │   ├── services/           # Comunicación con backend
    │   ├── composables/        # Lógica reutilizable
    │   ├── types/              # Interfaces TypeScript
    │   ├── utils/              # Funciones auxiliares
    │   ├── constants/          # Constantes
    │   ├── plugins/            # Axios, VueUse, etc.
    │   ├── styles/             # CSS global
    │   ├── App.vue
    │   └── main.ts
    ├── tests/
    ├── package.json
    ├── vite.config.ts
    ├── tsconfig.json
    └── .env
```

### Móvil
- **Stack referencia**: Ionic Vue + Capacitor (coherencia con la web).
- **Notificaciones locales**: `@capacitor/local-notifications`.
- **Push**: `@capacitor/push-notifications`.
- **Nativo**: Haptics, TTS, Cámara.
- **Operación offline**: Cola local con idempotencia y sincronización al recuperar conectividad.

### Base de datos

- **Motor**: PostgreSQL 16.
- **ORM**: SQLAlchemy + Flask-Migrate.
- **Modelo**: Entidades relacionales con soft delete, versionado de tratamientos, idempotencia en confirmaciones y auditoría.

Principales tablas:
- `users`, `profiles`, `accessibility_preferences`, `roles`, `user_roles`
- `auth_sessions`, `password_reset_tokens`
- `medications`, `treatments`, `treatment_revisions`
- `reminder_schedules`, `reminder_times`, `notification_policies`
- `dose_events`, `dose_status_transitions`
- `notifications`, `notification_deliveries`
- `user_devices`, `consents`
- `reports`, `statistics_snapshots`
- `sync_operations`, `audit_events`
- `care_relationships`, `care_permissions`

## Docker

Servicios orquestados con Docker Compose:

| Servicio | Imagen | Función | Puerto |
|----------|--------|---------|--------|
| `postgres` | `postgres:16-alpine` | Base de datos principal | 5432 |
| `redis` | `redis:7-alpine` | Caché y broker de Celery | 6379 |
| `api` | Build desde `./backend` | API REST Flask | 3000 |
| `worker` | Build desde `./backend` | Celery worker | — |
| `beat` | Build desde `./backend` | Celery beat (planificador) | — |

### Comandos esenciales

```bash
# Levantar toda la plataforma
docker compose up -d

# Ver estado de contenedores
docker compose ps

# Ver logs de un servicio
docker compose logs -f worker

# Detener la plataforma
docker compose down

# Reconstruir imágenes después de cambios
docker compose build
```

## Variables de entorno

Variables principales definidas en `.env`:
- `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`
- `DATABASE_URL`
- `SECRET_KEY`, `JWT_EXPIRATION_MINUTES`, `JWT_REFRESH_EXPIRATION_DAYS`
- `REDIS_URL`
- `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET`, `CLOUDINARY_URL`
- `FIREBASE_CREDENTIALS_FILE`
- `FLASK_APP`, `FLASK_ENV`, `APP_HOST`, `APP_PORT`

> **Seguridad**: `.env` está en `.gitignore` y nunca se sube al repositorio.

## Pruebas

```bash
# Backend: pruebas unitarias
cd backend
pytest -q

# Verificar compilación del dominio
cd backend
python -m compileall -q src
```

### Pruebas unitarias actuales

- Estados y transiciones de `DoseEvent`.
- Soft delete y estado de `User`.
- Validaciones de `Frequency` e `Interval`.
- Revocación de `AuthSession` y `CarePermission`.
- Ciclo de vida de `NotificationDelivery`.
- Consumo único de `PasswordResetToken`.

## Documentación

La documentación del proyecto se encuentra en `docs/`:

| Documento | Propósito |
|-----------|-----------|
| `contexto/CONTEXTO GENERAL.md` | Contexto, necesidades, públicos, flujos y requisitos funcionales. |
| `arquitectura/backend.md` | Stack, estructura y componentes del backend. |
| `arquitectura/frontend.md` | Stack, estructura y pantallas del frontend web. |
| `arquitectura/arquitectura_movil.md` | Arquitectura, capas, sincronización y accesibilidad móvil. |
| `arquitectura/base_de_datos.md` | Modelo entidad-relación, DDL PostgreSQL y seguridad. |
| `arquitectura/docker.md` | Estrategia de contenedores y comandos Docker Compose. |
| `reglas/reglas_del_negocio.md` | Reglas de negocio, seguridad, integridad y accesibilidad. |
| `orquestacion/orquestacion-del-flujo-de-trabajo.md` | Guía de desarrollo, verificación y gobierno del proyecto. |

## Flujo de trabajo

El proyecto regido por `docs/orquestacion/orquestacion-del-flujo-de-trabajo.md`:
- Modo plan por defecto para tareas no triviales.
- Uso de subagentes para investigación y análisis.
- Verificación antes de dar por hecha una tarea.
- Cambios mínimos, explícitos y trazables.
- Captura de lecciones en `tasks/lessons.md`.
- Seguimiento de avance en `tasks/todo.md`.

## Estado del proyecto

| Componente | Estado |
|------------|--------|
| Configuración (deps, Docker, env) | ✅ |
| Dominio (entidades, VOs, puertos, excepciones) | ✅ |
| Pruebas unitarias de dominio | ✅ |
| Persistencia (modelos SQLAlchemy, migraciones) | ⬜ |
| Aplicación (use cases, DTOs) | ⬜ |
| API REST (rutas, auth, middlewares, CRUD) | ⬜ |
| Configuración (`main.py`, `settings.py`, `security.py`) | ⬜ |
| Frontend web código | ⬜ |
| Móvil código | ⬜ |

## Requisitos

- Python 3.11+
- PostgreSQL 16
- Redis 7
- Docker y Docker Compose
- Node.js 18+ (para frontend)
- npm o pnpm (para frontend)

## Seguridad

- Contraseñas almacenadas como hash (bcrypt), nunca en texto plano.
- Autenticación por JWT con refresh tokens.
- Conexiones TLS entre aplicación y base de datos.
- Principio de mínimo privilegio en base de datos.
- Variables de entorno para credenciales; nunca en código.
- Audit trail en `audit_events` para acciones sensibles.

## Licencia

Proyecto académico/privado. Todos los derechos reservados.
