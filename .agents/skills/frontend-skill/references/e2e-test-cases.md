# Casos de Prueba E2E por Rol y Módulo (RecorNet)

Catálogo de escenarios end-to-end derivados del flujo general del sistema documentado en `docs/contexto/CONTEXTO GENRAL.md` y del flujo de confirmación de dosis. Usar como base para escribir tests con Playwright. Todos los tests deben ejecutarse con el backend en un entorno local (`http://localhost:3000`) o mocks de API.

## 1. Autenticación (`/auth`)

| ID | Escenario | Rol | Verificación |
|----|-----------|-----|--------------|
| AUTH-01 | Login con credenciales válidas | Ambos | Redirige al dashboard según rol |
| AUTH-02 | Login con credenciales inválidas | Ambos | Muestra mensaje de error claro, reintentable |
| AUTH-03 | Registro de usuario con datos válidos | Ambos | Cuenta creada, sesión iniciada |
| AUTH-04 | Registro con email duplicado | Ambos | Alerta de duplicado, no crea cuenta |
| AUTH-05 | Registro con campos obligatorios vacíos | Ambos | Validación de formulario activa, botón deshabilitado |
| AUTH-06 | Recuperación de contraseña | Ambos | Flujo de reset completado |
| AUTH-07 | Logout | Ambos | Sesión cerrada, JWT eliminado, redirige a login |
| AUTH-08 | Token expirado | Ambos | Expulsión amigable a login con mensaje |

## 2. Dashboard (`/dashboard`)

| ID | Escenario | Rol | Verificación |
|----|-----------|-----|--------------|
| DASH-01 | Adulto mayor ve su dashboard simplificado | Adulto mayor | Próxima toma, botón grande "Confirmar toma" visible |
| DASH-02 | Cuidador ve dashboard con gestión | Cuidador | Listado de medicamentos, acceso a CRUD |
| DASH-03 | Notificaciones visibles en dashboard | Ambos | Badge/contador de recordatorios activos |
| DASH-04 | Sin medicamentos registrados | Ambos | Estado vacío con CTA claro |

## 3. Medicamentos (`/medications`)

| ID | Escenario | Rol | Verificación |
|----|-----------|-----|--------------|
| MED-01 | Crear medicamento con datos válidos | Cuidador | Guardado en BD, visible en listado |
| MED-02 | Crear medicamento sin nombre | Cuidador | Error de validación, formulario no se envía |
| MED-03 | Subir fotografía del medicamento | Cuidador | `multipart/form-data` enviado, imagen visible |
| MED-04 | Editar medicamento | Cuidador | Datos actualizados, horarios sincronizados |
| MED-05 | Eliminar medicamento con confirmación | Cuidador | Diálogo de confirmación, registro eliminado |
| MED-06 | Ver detalle de medicamento | Ambos | Foto, dosis, descripción, horario correctos |
| MED-07 | Duplicar medicamento existente | Cuidador | Alerta de duplicado aplicada |

## 4. Recordatorios (`/reminders`)

| ID | Escenario | Rol | Verificación |
|----|-----------|-----|--------------|
| REM-01 | Programar recordatorio al crear medicamento | Cuidador | Notificación programada automáticamente |
| REM-02 | Editar horarios de recordatorio | Cuidador | Horarios actualizados en servidor |
| REM-03 | Recepción de notificación push | Adulto mayor | Contiene nombre, foto, dosis, descripción, hora |
| REM-04 | Recordatorio con imagen accesible | Adulto mayor | `<img alt="...">` presente con nombre del medicamento |
| REM-05 | Dosis pendiente por no confirmar | Adulto mayor | Se marca pendiente, se repite recordatorio |
| REM-06 | Cuidador notificado de dosis pendiente | Cuidador | Recibe alerta si opción habilitada |

## 5. Confirmación de toma (núcleo del producto)

| ID | Escenario | Rol | Verificación |
|----|-----------|-----|--------------|
| TOMA-01 | Confirmar toma dentro del tiempo | Adulto mayor | Se registra fecha/hora de confirmación |
| TOMA-02 | Registrar en historial tras confirmar | Ambos | Entrada visible en historial |
| TOMA-03 | No confirmar y superar tiempo límite | Adulto mayor | Dosis marcada como pendiente/omitida |
| TOMA-04 | Cancelar confirmación | Adulto mayor | Sin registro, dosis sigue pendiente |

## 6. Historial (`/history`)

| ID | Escenario | Rol | Verificación |
|----|-----------|-----|--------------|
| HIS-01 | Consultar historial de tomas | Ambos | Dosis tomadas, pendientes y omitidas listadas |
| HIS-02 | Filtrar por rango de fechas | Ambos | Filtrado correcto por día/semana/mes |

## 7. Estadísticas (`/statistics`)

| ID | Escenario | Rol | Verificación |
|----|-----------|-----|--------------|
| EST-01 | Porcentaje de adherencia visible | Ambos | Indicador numérico correcto |
| EST-02 | Días consecutivos de cumplimiento | Ambos | Contador consistente con historial |
| EST-03 | Dosis tomadas vs pendientes vs omitidas | Ambos | Gráfico coincide con datos reales |
| EST-04 | Número de dosis programadas por día | Ambos | Correcto según tratamiento activo |
| EST-05 | Gráficos con lectores de pantalla | Ambos | `<canvas>` con rol/etiqueta o tabla alternativa |

## 8. Perfil y configuración

| ID | Escenario | Rol | Verificación |
|----|-----------|-----|--------------|
| PROF-01 | Editar perfil | Ambos | Cambios persisten tras recargar |
| PROF-02 | Cambiar tamaño de fuente accesible | Ambos | Tipografía se escala globalmente (rem) |
| PROF-03 | Alternar alto contraste / modo oscuro | Ambos | Tema aplicado y persistente |
| PROF-04 | Activar/desactivar lectura por voz | Adulto mayor | Text-to-speech funciona |
| PROF-05 | Cambiar rol en pruebas | Ambos | UI adaptada al rol tras relogin |

## Reglas para escribir los tests Playwright

1. Un archivo por módulo: `e2e/auth.spec.ts`, `e2e/medications.spec.ts`, etc.
2. Nombrar tests con el ID del escenario (ej. `test('MED-01: crear medicamento con datos válidos')`) para trazabilidad con este catálogo.
3. Usar `test.describe.configure({ mode: 'parallel' })` solo cuando los tests no comparten estado.
4. Mockear la API con `page.route('**/api/**', ...)` o MSW para tests que no requieran backend real.
5. Para notificaciones push (REM-03) y TTS (PROF-04), verificar el comportamiento observable en UI o los mocks de servicio, no la integración nativa (eso pertenece a la app Capacitor).
