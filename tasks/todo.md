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
