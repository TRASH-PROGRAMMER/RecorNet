## Orquestación del flujo de trabajo

### 1. modo plan por defecto
- El flujo de trabajo se ejecuta en modo plan por defecto.
- Entra en modo plan para CUALQUIER tarea no trivial (3+ pasos o decisiones de arquitectura)
- Si algo se tuerce, detente y vuelve a planificar de inmediato; no sigas empujando
- Usa el modo plan tambien para los pasos de verificacion, no solo para construir
- Escribe especificaciones detalladas desde el principio para reducir la ambiguedad
### 2. Estrategia de Subagentes
- Usa subagentes sin problema para mantener limpia la ventana de contexto principal
- Delega investigación, exploración y análisis en paralelo a subagentes
Para problemas complejos, asigna mas capacidad de computo mediante subagentes
Una tarea por subagente para una ejecucion enfocada
### 3. Bucle de Auto-mejora
Despues de CUALQUIER correccion del usuario: actualiza tasks/lessons.md con el patron
- Escribe reglas para ti mismo que eviten repetir el mismo error
- Itera sin piedad sobre estas lecciones hasta que baje la tasa de errores
- Revisa las lecciones al inicio de la sesion para el proyecto relevante
### 4. Verificacion Antes de Darlo por Hecho
- Nunca marques una tarea como completada sin demostrar que funciona
- Compara el comportamiento entre main y tus cambios cuando sea relevante
- Pregúntate: "¿Lo aprobaría un staff engineer?"
- Ejecuta pruebas, revisa logs y demuestra que es correcto
### 5. Exige Elegancia (Equilibrada)
- Para cambios no triviales: haz una pausa y preguntate "hay una forma mas elegante?"
- Si una solucion se siente chapucera: "Sabiendo todo lo que se ahora, implementa la solucion elegante"
- Saltate esto en arreglos simples y obvios; no sobre-ingenierices
- Cuestiona tu propio trabajo antes de presentarlo
### 6. Corrección Autónoma de Bugs
- Cuando te den un reporte de bug: simplemente arreglalo. No pidas que te lleven de la mano
- Señala logs, errores y tests que fallan; luego resuelvelos
- Cero cambios de contexto requeridos por parte del usuario
- Ve y arregla los tests fallidos del CI sin que te digan como
## Gestión de Tareas
1. ** Planifica Primero **: Escribe el plan en "tasks/todo.md con elementos verificables
2. ** Verifica el Plan **: Haz un check-in antes de empezar la implementacion
3. ** Haz Seguimiento del Progress **: Marca los elementos como completados a medida que avanzas
4. *+Explica los Cambios **: Resumen de alto nivel en cada paso
5. ** Documenta los Resultados **: Anade una sección de revisión a tasks/todo.md
6. ** Captura Lecciones **: Actualiza 'tasks/lessons.md' despues de las correcciones
## Principios Fundamentales
- ** La Simplicidad Primero **: Haz cada cambio tan simple como sea posible. Impacta el minimo código posible.
- ** Nada de Pereza **: Encuentra las causas raiz. Nada de arreglos temporales. Estandares de un desarrollador senior.
- ** Impacto Minimo **: Los cambios solo deben tocar lo necesario. Evita introducir bugs.
- ** Documenta Todo **: Cada cambio debe tener un resumen de alto nivel. Los cambios complejos requieren una sección de revisión.
- ** Reglas de Oro **: No ignores los errores. No ignores los tests fallidos. No ignores los logs. No ignores las advertencias del compilador. No ignores las advertencias de seguridad.
- Para tener contexto general del proyecto web debes rvisar y analizar el archivo de  contexto general del proyecto  en docs\contexto.
- No puedes elinar esta carpetas  ni su subcarpetas y archivos C:\Users\RUDY PICO\Desktop\Recornet\docs  y .agents.
- No puedes eliminar ni renombrar ni mover estos archivos y carpetas  ni su subcarpetas y archivos C:\Users\RUDY PICO\Desktop\Recornet\docs  y .agents.
- Para  el frotend del proyecto web debes revisar y analizar los archivos C:\Users\RUDY PICO\Desktop\Recornet\docs\arquitectura\frontend.md y C:\Users\RUDY PICO\Desktop\Recornet\docs\contexto\CONTEXTO GENRAL.md para asi cumplir con estos.
- Para  el backend del proyecto web debes revisar y analizar los archivos C:\Users\RUDY PICO\Desktop\Recornet\docs\arquitectura\backend.md y C:\Users\RUDY PICO\Desktop\Recornet\docs\contexto\CONTEXTO GENRAL.md para asi cumplir con estos.
- Para la aplicación de Android debes revisar y analizar los archivos C:\Users\RUDY PICO\Desktop\Recornet\docs\arquitectura\arquitectura_movil.md y C:\Users\RUDY PICO\Desktop\Recornet\docs\contexto\CONTEXTO GENRAL.md para asi cumplir con estos.
- Puedes eliminar carpetas y archivos de codigo  de backend , frontend, multiplataforma siempre cuando me preguntes y yo apruebe elimiar ese archivo y explica el por que ese archvio de codigo  nesecia  ser eliminado.