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
