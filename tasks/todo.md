# RecorNet Backend — Tareas Fase 1

## Componente 1: Configuración del Proyecto
- [x] `requirements.txt` — dependencias Python
- [x] `.env.example` — plantilla de variables de entorno
- [x] `Dockerfile` — actualizado para instalar deps y exponer puerto
- [x] Estructura de carpetas `src/` con `__init__.py` (30 paquetes creados)
- [x] Estructura de carpetas `tests/` (unit, integration)

## Componente 2: Capa de Dominio
- [x] Entidades del dominio
- [x] Value objects
- [x] Repositorios abstractos
- [x] Puertos abstractos
- [x] Excepciones de dominio

## Componente 3: Infraestructura — Persistencia
- [ ] Modelos SQLAlchemy
- [ ] Repositorios concretos
- [ ] Configuración de database.py

## Componente 4: Capa de Aplicación — Use Cases
- [ ] Auth use cases (register, login, refresh)
- [ ] Medications use cases (CRUD)
- [ ] DTOs

## Componente 5: Infraestructura — API
- [ ] Rutas (auth, medications)
- [ ] Middlewares (JWT, roles)
- [ ] Validadores Pydantic
- [ ] Serializadores

## Componente 6: Configuración
- [ ] settings.py
- [ ] dependencies.py
- [ ] security.py

## Componente 7: Entrada Principal
- [ ] main.py (create_app factory)
- [ ] Shared (responses, enums)
- [ ] Verificación final

## Gobierno de desarrollo y orquestación
- [x] Adoptar `docs/orquestacion/orquestacion-del-flujo-de-trabajo.md` como guía obligatoria
- [x] Registrar las lecciones de proceso en `tasks/lessons.md`
- [ ] Añadir una sección de revisión verificable a cada tarea no trivial completada

## Revisión de entidades de dominio
- [x] Inspeccionar entidades, pruebas y documentación del dominio
- [x] Verificar el cumplimiento con contexto, arquitectura backend, reglas de negocio y orquestación
- [x] Corregir inconsistencias de estado, roles, idempotencia y tipos temporales
- [x] Resolver la dependencia faltante `value_objects.interval` detectada por las pruebas
- [x] Corregir imports incompletos del objeto de valor `Frequency`
- [x] Ampliar las pruebas unitarias de las entidades corregidas
- [x] Documentar resultados, evidencias y acciones pendientes de la revisión

### Revisión verificable — entidades de dominio (2026-08-22)

| Criterio | Evidencia | Resultado |
| --- | --- | --- |
| Contexto y reglas | Revisión de `docs/contexto/CONTEXTO GENERAL.md`, `docs/arquitectura/backend.md`, `docs/reglas/reglas_del_negocio.md` y la guía de orquestación. | Cumplido. |
| Estados y sincronización de dosis | `DoseEvent` separa estado clínico, sincronización e idempotencia; se añadió `Interval` para restaurar `Frequency`. | Corregido y probado. |
| Usuarios, roles y notificaciones | `User` elimina el rol duplicado y usa borrado lógico; `Notification` actualiza su campo de estado documentado. | Corregido y probado. |
| Pruebas y compilación | `pytest -q` ejecutó 11 pruebas correctas; `compileall -q src` terminó sin errores; `git diff --check` no reportó errores. | Cumplido. |

**Acciones pendientes no bloqueantes:** normalizar `CareRelationship.permissions` hacia `CarePermission`; reconciliar `UserDevices.notifications_consent` con `Consent`; unificar `ReminderSchedule.scheduled_time` con `ReminderTimes`; consolidar las dos representaciones de estadísticas; y actualizar el inventario histórico de entidades en `docs/arquitectura/backend.md` únicamente con autorización explícita, porque la guía prohíbe modificar `docs/` durante el desarrollo ordinario.

## Informe de cambios publicados
- [x] Delimitar los commits y archivos incluidos en el informe
- [x] Documentar alcance, validaciones, incidencias y pendientes
- [x] Entregar un informe verificable al usuario

### Revisión verificable — informe de cambios (2026-08-26)

El informe cubre los commits `9978e9f`, `f32e9a9`, `4bf856a`, `79f76de` y `b432c5e`; documenta archivos, alcance, validaciones, conflictos de integración y pendientes. El archivo entregable se conserva fuera del repositorio para respetar la restricción de no modificar `docs/` sin autorización explícita.

## Corrección del gap G3 — relación cuidador–adulto mayor
- [x] Revisar listas mutuas en `Caregiver`/`Elderly` y establecer `CareRelationship` como fuente única
- [x] Aplicar permisos y estado de `CareRelationship` en los accesos del cuidador
- [x] Filtrar repositorios de tratamientos y medicación por relación de cuidado autorizada
- [x] Añadir pruebas de aislamiento entre adultos mayores vinculados y no vinculados
- [x] Registrar evidencia de validación y publicar la corrección

## Corrección del repositorio de recordatorios — ReminderRepository
- [x] Corregir `ReminderRepository`: importar `ReminderSchedule` y exigir `actor_id` con autorización de relación de cuidado.
- [x] Añadir pruebas de contrato y aislamiento para `ReminderRepository`.
- [x] Validar con `pytest -q` (14 pruebas), `compileall -q src` y `git diff --check`.
- [x] Publicar la corrección del repositorio de recordatorios en GitHub.

### Revisión verificable — ReminderRepository

| Criterio | Evidencia | Resultado |
| --- | --- | --- |
| Entidad correcta | `backend/src/domain/repositories/reminder_repository.py` importa y utiliza `ReminderSchedule`; no importa `Reminder`. | Cumplido. |
| Contexto de autorización | `save`, `get_by_id`, `get_for_patient` y `delete` exigen `actor_id`; las operaciones por registro también exigen `patient_id` y `permission`. | Cumplido en el contrato de dominio. |
| Pruebas | `backend/tests/unit/test_operational_domain_entities.py` verifica tipos, parámetros keyword-only y permisos; `pytest -q` terminó con 14 pruebas correctas. | Cumplido. |
| Persistencia concreta | No existe todavía un adaptador SQLAlchemy de recordatorios en el árbol actual. | Pendiente para la capa de infraestructura. |

## Implementación de persistencia autorizada — Componente 3
- [x] Crear modelos SQLAlchemy mínimos para relaciones, permisos, medicamentos, tratamientos y horarios.
- [x] Implementar adaptadores concretos de `MedicationRepository`, `TreatmentRepository` y `ReminderRepository`.
- [x] Aplicar joins a `care_relationships` y `care_permissions`, permitiendo también al paciente actuar sobre sus propios datos.
- [x] Añadir pruebas de integración SQLite para aislamiento de cuidadores no vinculados y permisos revocados.
- [x] Ejecutar pruebas unitarias/integración, compilación y revisión del diff.

### Plan verificable — persistencia autorizada (2026-10-17)

**Alcance:** solo `backend/src/infrastructure/persistence` y `backend/tests/integration`; no se modifican `docs/` ni `.agents/`.

**Riesgos:** diferencias de tipos de identificador entre entidades (`str`/`int`), divergencia entre `CareRelationship.permissions` y el esquema normalizado `care_permissions`, y ausencia de PostgreSQL en el sandbox.

**Criterios de aceptación:** (1) los tres adaptadores implementan sus puertos; (2) las lecturas de cuidador usan joins con relación activa y permiso no revocado; (3) un cuidador no vinculado no obtiene filas ni puede borrar; (4) el paciente puede consultar sus propios datos; (5) las pruebas SQLite pasan y el código compila.

### Revisión verificable — persistencia autorizada (2026-10-17)

| Criterio | Evidencia | Resultado |
| --- | --- | --- |
| Adaptadores | `sqlalchemy_medication_repository.py`, `sqlalchemy_treatment_repository.py` y `sqlalchemy_reminder_repository.py` implementan los puertos de dominio. | Cumplido. |
| Aislamiento | Consultas con joins/outer joins a `care_relationships` y `care_permissions`, estado activo y permiso no revocado. | Cumplido. |
| Pruebas | `tests/integration/test_authorized_sqlalchemy_repositories.py` cubre cuidador vinculado, no vinculado, permiso revocado y propietario. | Cumplido. |
| Verificación técnica | `PYTHONPATH=src pytest -q`: 23 correctas; `compileall -q src tests`: correcto; `git diff --check`: correcto. | Cumplido, con una advertencia preexistente de `datetime.utcnow()`. |
| Alcance protegido | No se modificaron `docs/` ni `.agents/`. | Cumplido. |

## Contexto obligatorio cargado — documentación y skills (2026-10-17)
- [x] Leer los 9 documentos Markdown de `docs/` y sus secciones completas.
- [x] Leer `SKILL.md`, referencias, plantilla y script de `frontend-skill`.
- [x] Leer `SKILL.md` y el paquete `recornet-capacitor-dev.skill` de `mobile-skill`.
- [x] Registrar las reglas consolidadas en `tasks/lessons.md` sin modificar `docs/` ni `.agents/`.
- [x] Leer y registrar `GEMINI.md` como directiva maestra global del agente.

## Corrección de bugs en servicios de dominio — reminder_service.py y notification_service.py
- [x] `reminder_service.py`: corregir `NameError` por `Reminder = Reminder` sin import (línea 8 original).
- [x] `reminder_service.py`: importar `ReminderSchedule` y crear alias `Reminder = ReminderSchedule`.
- [x] `reminder_service.py`: inyectar `ReminderRepository` en `__init__`.
- [x] `reminder_service.py`: corregir firma de `update` (usaba `ReminderRepository` como tipo en vez de `Reminder`).
- [x] `notification_service.py`: eliminar import inexistente `notification_delivery_repository`.
- [x] `notification_service.py`: heredar de `ABC` para que los `@abstractmethod` sean efectivos.
- [x] Verificar con `python -m pytest -v`: 23/23 tests pasaron.

### Revisión verificable — bugs servicios de dominio (2026-10-17)

| Criterio | Evidencia | Resultado |
| --- | --- | --- |
| Import exitoso | `python -c "import src.domain.services.reminder_service"` y `"...notification_service"` sin errores. | Cumplido. |
| Tipado correcto | `reminder_service.update` usa `Reminder` (alias de `ReminderSchedule`), no `ReminderRepository`. | Cumplido. |
| ABC efectivo | `NotificationService(ABC)` hace que `@abstractmethod` sea vinculante. | Cumplido. |
| Suite completa | `python -m pytest -v`: 23 passed, 0 failed. | Cumplido. |

## Verificación del endpoint de salud — `GET /health` (2026-10-20)
- [x] Verificar que `create_app()` registra `GET /health` y devuelve JSON `200`.
- [x] Verificar que Swagger expone `/health` en `/apispec_1.json`.
- [x] Ejecutar compilación del backend y revisión de diff.
- [ ] Formalizar el contrato de salud en la documentación aprobada, previa autorización para modificar `docs/`.
- [ ] Separar liveness (`/health`) de readiness con comprobación de dependencias (PostgreSQL/Redis) cuando exista la capa de configuración correspondiente.
- [ ] Resolver la incidencia de integración: `Base.metadata.create_all()` falla porque `care_relationships` referencia `users` y no existe un modelo `UserModel` registrado.

### Revisión verificable — endpoint de salud

| Criterio | Evidencia | Resultado |
| --- | --- | --- |
| Respuesta HTTP | Flask test client: `GET /health` → `200`, `application/json`, `{"status": "200 ok"}`. | Cumplido como liveness básico. |
| Documentación técnica | `/apispec_1.json` → `200` y contiene `/health`. | Cumplido técnicamente; falta contrato canónico en `docs/`. |
| Arquitectura | La ruta está en `backend/main.py`, fuera de `src/application`/adaptadores formales. | Alineación parcial; requiere consolidación con la entrada API prevista. |
| Producción | `main.py` arranca con `debug=True`; el endpoint no comprueba PostgreSQL/Redis. | Pendiente de endurecimiento. |
| Suite global | `23` pruebas de dominio no se ejecutan completamente: `4` errores de setup por FK a `users`; la prueba directa del endpoint sí pasó. | Incidencia independiente pendiente. |

## Movimiento de la factoría Flask a `backend/src/main.py` (2026-10-20)
- [x] Mover la implementación real de `create_app()` a `backend/src/main.py`.
- [x] Mantener `backend/main.py` como shim de compatibilidad, sin duplicar la factoría.
- [x] Verificar el contrato `FLASK_APP=src.main:create_app` y los imports desde `src.main` y `main`.
- [x] Probar `/health`, Swagger, compilación y las pruebas específicas de la factoría.
- [x] Registrar evidencia y publicar el cambio sin modificar `docs/` ni `.agents/`.

### Revisión verificable — factoría Flask en `src.main`

| Criterio | Evidencia | Resultado |
| --- | --- | --- |
| Ubicación canónica | `backend/src/main.py` contiene la única implementación de `create_app()`. | Cumplido. |
| Compatibilidad | `backend/main.py` reexporta `create_app` desde `src.main`, sin duplicar la factoría. | Cumplido. |
| Descubrimiento Flask | `FLASK_APP=src.main:create_app flask routes` registra `/health` y Swagger. | Cumplido. |
| Prueba específica | `tests/integration/test_app_factory.py`: 1 pasada. | Cumplido. |
| Compilación | `python3 -m compileall -q backend/src backend/main.py backend/tests`: correcto. | Cumplido. |
| Suite global | 20 pruebas pasan; 4 errores de setup persisten por FK a `users` sin `UserModel` en `Base`. | Pendiente independiente. |

## Auditoría de imports y módulos heredados (2026-10-20)
- [x] Auditar imports internos y símbolos heredados en `backend/src` y `backend/tests`.
- [x] Importar los 106 módulos Python del backend para detectar referencias rotas.
- [x] Eliminar el alias heredado `Reminder` del servicio y usar `ReminderSchedule` de forma canónica.
- [x] Mantener `backend/main.py` únicamente como shim compatible hacia `src.main`.
- [x] Validar imports, pruebas dirigidas, compilación y `git diff --check`.
- [ ] Normalizar el nombre de archivo `Frequency.py` a `frequency.py` mediante una tarea separada con plan de migración; actualmente todos los imports son consistentes.

### Revisión verificable — imports heredados

| Hallazgo | Estado |
| --- | --- |
| `Reminder` como alias de `ReminderSchedule` | Corregido en `domain/services/reminder_service.py`; no quedan referencias al símbolo aislado. |
| `notification_delivery_repository` | No se encontraron referencias; el repositorio canónico es `notification_delivery.py`. |
| `backend/main.py` | Se conserva intencionalmente como shim; la implementación canónica está en `src/main.py`. |
| Importación de módulos | 106 módulos importados, 0 fallos. |
| Pruebas dirigidas | 15 pasadas (`test_app_factory.py` y `test_operational_domain_entities.py`). |
| Compilación y diff | Correctos; no se modificaron `docs/` ni `.agents/`. |
