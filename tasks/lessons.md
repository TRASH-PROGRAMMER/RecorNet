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
