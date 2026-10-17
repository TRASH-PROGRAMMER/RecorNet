# GEMINI.md — RecorNet: Enrutador Global y Guardián de Restricciones Inmutables

> **PROPÓSITO:**  
> Este documento rige como la **directiva maestra inmutable** para cualquier agente de inteligencia artificial en el entorno de desarrollo de **RecorNet**.  
> Centraliza el **enrutamiento de conocimiento técnico** y custodia las **restricciones arquitectónicas, de seguridad y de gobernanza** no negociables del proyecto.

---

## 1. Guardián de Restricciones Inmutables (Reglas Inviolables)

Cualquier cambio de código, sugerencia o planificación debe acatar estrictamente las siguientes restricciones:

### 🛡️ R1: Inmutabilidad de Documentación y Configuración (`docs/` y `.agents/`)
- **PROHIBICIÓN ABSOLUTA:** Queda terminantemente prohibido eliminar, renombrar, mover o sobreescribir archivos dentro de los directorios `docs/` y `.agents/` durante el desarrollo ordinario.
- Los archivos en `docs/` constituyen la especificación aprobada de arquitectura, datos y negocio.
- Los archivos en `.agents/` son los skills y herramientas operativas del agente.

### 🛡️ R2: Autorización Explícita para Eliminación de Código
- Ningún archivo ni carpeta de código en `backend/`, `frontend/`, `multiplataforma/` o raíz del proyecto puede ser eliminado sin:
  1. Explicar previamente al usuario la justificación técnica de la eliminación.
  2. Obtener la **aprobación explícita** del usuario antes de proceder.

### 🛡️ R3: Pureza de Capas en Clean Architecture (Backend)
- **Núcleo de Dominio Aislado (`backend/src/domain/`):**
  - Cero dependencias de frameworks externos (`Flask`, `SQLAlchemy`, `FastAPI`, `Pydantic`, librerías móviles o de UI). Únicamente Python estándar (`dataclasses`, `datetime`, `uuid`, `abc`, `typing`).
  - Los repositorios en la capa de dominio son interfaces abstractas puras (`abc.ABC`).
  - Los Value Objects son inmutables (`frozen=True`).
- **Contratos de Repositorio Seguros:**
  - Toda operación de consulta o mutación sobre recursos clínicos (tratamientos, horarios, dosis) debe exigir obligatoriamente el contexto de autorización: `actor_id`, `patient_id` y el permiso requerido. Prohibidas consultas abiertas sin aislamiento de paciente.

### 🛡️ R4: Modelo de Vinculación y Autorización Cuidador–Adulto Mayor
- **Fuente Única de Verdad:** `CareRelationship` y `CarePermission` son las únicas fuentes de verdad de vinculación.
  - **PROHIBIDO:** Usar listas mutuas en memoria en entidades `User`, `Caregiver` o `Elderly`.
  - **PROHIBIDO:** Usar columnas embebidas tipo `permissions: JSONB` en `care_relationships`.
- **Autoridad de Concesión:**
  - El Adulto Mayor (`elderly_id`) es la **única autoridad** que puede otorgar o revocar permisos (`granted_by_user_id == elderly_id`). El backend debe validar esto en servidor y nunca confiar en el payload del cliente.
- **Vinculación Asistida:**
  - Códigos temporales alfanuméricos de un solo uso generados por el adulto mayor.
  - Almacenamiento seguro exclusivo de `code_hash` (nunca texto plano).
  - Límite estricto de 5 intentos fallidos de validación.

### 🛡️ R5: Doble Máquina de Estados e Idempotencia en Dosis
- **Separación de Estados:**
  - **Estado Clínico (`status`):** `Programada` → `Alertada` → `Tomada` / `Omitida`.
  - **Estado de Sincronización (`sync_status`):** `Pendiente` → `Sincronizada` / `Fallida`.
  - Ambos estados conviven en columnas independientes para garantizar funcionamiento *offline-first*.
- **Idempotencia Transaccional:**
  - El endpoint de confirmación de dosis debe validar: (1) clave de idempotencia transaccional, (2) transiciones válidas de estado clínico (rechazando confirmaciones duplicadas o regresivas), y (3) atomicidad en base de datos.

### 🛡️ R6: Accesibilidad Universal (WCAG 2.1 AA)
- Toda interfaz desarrollada para el adulto mayor debe cumplir:
  - Áreas interactivas mínimas de **44x44 pt/px**.
  - Relación de contraste mínima de **4.5:1** (3:1 para textos grandes).
  - Tipografía dinámica relativa (`rem`/`em`).
  - Redundancia multimodal (visual, vibración háptica y lectura Text-To-Speech).

---

## 2. Enrutador Global de Conocimiento

Antes de responder, planificar o modificar código, el agente debe enrutar su contexto hacia las fuentes documentales y skills correspondientes según el ámbito de la tarea:

```
                                  [ TAREA RECIBIDA ]
                                           │
         ┌───────────────────┬─────────────┴─────────────┬────────────────────┐
         ▼                   ▼                           ▼                    ▼
   [ REGLAS / NEGOCIO ]  [ BACKEND / BD ]        [ FRONTEND / WEB ]    [ MÓVIL / CAPACITOR ]
         │                   │                           │                    │
  • CONTEXTO GENERAL  • backend.md                • frontend.md        • arquitectura_movil.md
  • reglas_del_negocio• base_de_datos.md          • frontend-skill/    • mobile-skill/
                      • Clean Architecture        • Vue 3 + Tailwind   • Plugins nativos
                      • Repositorios abstractos   • WCAG / a11y tests  • Offline sync
```

### Tabla de Enrutamiento Obligatorio

| Ámbito de la Tarea | Documentos Principales a Consultar | Skills y Herramientas a Activar |
| :--- | :--- | :--- |
| **Gobernanza y Orquestación** | • `docs/orquestacion/orquestacion-del-flujo-de-trabajo.md`<br>• `tasks/lessons.md`<br>• `tasks/todo.md` | • Modo Plan por defecto<br>• Ciclo de auto-mejora continua |
| **Reglas del Negocio y Dominio** | • `docs/reglas/reglas_del_negocio.md`<br>• `docs/contexto/CONTEXTO GENERAL.md` | • Validación de roles (`patient`, `caregiver`)<br>• Protocolo de vinculación asistida (17 pasos) |
| **Backend & Base de Datos** | • `docs/arquitectura/backend.md`<br>• `docs/arquitectura/base_de_datos.md` | • Python / Flask / SQLAlchemy (capa de infra)<br>• Interfaces puras en dominio (`src/domain/`) |
| **Frontend Web** | • `docs/arquitectura/frontend.md`<br>• `docs/contexto/CONTEXTO GENERAL.md` | • `.agents/skills/frontend-skill/SKILL.md`<br>• Checklist de revisión y pruebas E2E<br>• Script de auditoría de accesibilidad |
| **Aplicación Móvil (Android)** | • `docs/arquitectura/arquitectura_movil.md`<br>• `docs/contexto/CONTEXTO GENERAL.md` | • `.agents/skills/mobile-skill/SKILL.md`<br>• Plugins nativos Capacitor (Local Notifications, Haptics, TTS, Camera) |

---

## 3. Protocolo Operativo del Agente

1. **Modo Planificación Obligatorio:**
   - Activar el análisis estructurado para cualquier tarea no trivial (≥ 3 pasos o con impacto en arquitectura).
   - Registrar y dar seguimiento a los pasos en `tasks/todo.md`.
2. **Ciclo de Auto-Mejora (Lessons Learned):**
   - Ante **CUALQUIER** corrección recibida del usuario o falla de diseño, actualizar de inmediato `tasks/lessons.md` documentando el patrón y la regla para evitar reincidencia.
3. **Verificación Empírica Antes de Concluir:**
   - Prohibido asumir que una tarea funciona sin evidencia verificable (ejecución de pruebas unitarias `pytest`, linters, compilación o logs limpios).
4. **Respuestas Precisas y Enlaces Clicables:**
   - Mantener explicaciones concisas y directas.
   - Todo archivo, clase o función mencionada debe incluir un enlace clicable con el formato `[nombre](file:///ruta/absoluta)`.
