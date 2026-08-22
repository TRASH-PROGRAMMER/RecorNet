# Lecciones de desarrollo

## 2026-08-22 — Orquestación obligatoria

La guía `docs/orquestacion/orquestacion-del-flujo-de-trabajo.md` es el estándar operativo del proyecto. Para cada tarea no trivial se debe crear un plan verificable, revisar primero la documentación de contexto y arquitectura que corresponda al componente afectado, mantener el avance en `tasks/todo.md` y no marcar la tarea como completada sin evidencia de validación.

No se deben eliminar, mover, renombrar ni modificar archivos dentro de `docs/` o `.agents/` durante el desarrollo ordinario. Las correcciones del usuario deben registrarse aquí como reglas que prevengan su repetición. Antes de presentar cambios se deben revisar pruebas, errores, advertencias y logs relevantes; los cambios deben ser mínimos, explícitos y trazables.
