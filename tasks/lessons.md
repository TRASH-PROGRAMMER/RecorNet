# Lessons Learned

## 2026-08-22 — Orquestación obligatoria

La guía `docs/orquestacion/orquestacion-del-flujo-de-trabajo.md` es el estándar operativo del proyecto. Para cada tarea no trivial se debe crear un plan verificable, revisar primero la documentación de contexto y arquitectura que corresponda al componente afectado, mantener el avance en `tasks/todo.md` y no marcar la tarea como completada sin evidencia de validación.

No se deben eliminar, mover, renombrar ni modificar archivos dentro de `docs/` o `.agents/` durante el desarrollo ordinario. Las correcciones del usuario deben registrarse aquí como reglas que prevengan su repetición. Antes de presentar cambios se deben revisar pruebas, errores, advertencias y logs relevantes; los cambios deben ser mínimos, explícitos y trazables.

## 2026-08-26 — Alineación de documentos de reglas y orquestación

- Se actualizó `docs/orquestacion/orquestacion-del-flujo-de-trabajo.md` para eliminar rutas hardcodeadas de Windows y normalizar las referencias a rutas relativas con backticks.
- Se unificaron las reglas de restricción de `docs/` y `.agents/` en una sola línea clara, eliminando redundancias.
- Se corrigieron errores de escritura (`rvisar`, `elinar`, `frotend`, `GENRAL`, `nesecia`, `elimiar`, `archvio`).
- Ambas referencias (`docs/reglas/reglas_del_negocio.md` y `docs/orquestacion/orquestacion-del-flujo-de-trabajo.md`) ahora son consistentes y no se contradicen.

## 2026-09-01 — G3: autorización por relación de cuidado

Una relación cuidador–adulto mayor no debe representarse con listas mutuas en memoria. `CareRelationship` es la fuente única de verdad y toda operación de tratamiento o medicación debe recibir `actor_id`, el paciente y el permiso requerido. Los puertos de repositorio deben impedir consultas sin contexto de autorización; las implementaciones concretas deben aplicar ese contrato mediante un join a relaciones activas.

## 2026-10-17 — Persistencia y autorización en dos niveles

Los adaptadores de persistencia no deben confiar en una autorización previa del caso de uso. Las consultas sensibles deben incorporar el contexto del actor y un `JOIN` a `care_relationships` activa y a `care_permissions` no revocada; el propietario puede acceder a sus propios datos mediante una rama explícita. Cuando el dominio y el DDL usan tipos de identificador distintos, la conversión debe quedar encapsulada en infraestructura y no filtrarse a los puertos.

## 2026-10-17 — Contexto obligatorio de docs y skills

Antes de cada cambio de RecorNet se debe consultar el contexto general, la arquitectura correspondiente al componente, el modelo de base de datos cuando haya persistencia, las reglas del negocio y la guía de orquestación. Para frontend y móvil también son obligatorias las skills de pruebas/auditoría y Capacitor, junto con sus referencias internas. La accesibilidad no es opcional: contraste mínimo 4.5:1/3:1, tipografía escalable, áreas táctiles de al menos 44×44, `alt`/labels, foco visible, alertas redundantes y pruebas trazables por escenario.

El backend mantiene Flask + SQLAlchemy + PostgreSQL + Flask-Migrate, Clean/Hexagonal Architecture, JWT, Redis/Celery, FCM y Cloudinary. La autorización efectiva siempre vive en backend; `CareRelationship` y `care_permissions` son la fuente de acceso cuidador-paciente; el paciente/cuidador solo ve el alcance autorizado; las contraseñas son hashes y los secretos provienen del entorno. El móvil de producción de referencia es Ionic Vue + Capacitor, con notificaciones locales y push, almacenamiento seguro, cola offline idempotente y servidor como fuente de verdad.

El proceso es obligatorio: plan verificable antes de tareas no triviales, cambios mínimos en el módulo responsable, pruebas y revisión de logs/diff antes de cerrar, sección de revisión en `tasks/todo.md` y lección ante cada corrección. No se deben modificar, mover, renombrar ni eliminar archivos de `docs/` o `.agents/` durante el desarrollo ordinario.
