---
name: recornet-frontend-testing
description: "Pruebas de frontend y auditoria UI/UX para RecorNet (app web Vue 3 + TypeScript + Pinia + Vue Router + Axios + Tailwind para recordatorio de medicamentos a adultos mayores). Usar cuando se vaya a probar, auditar o revisar el frontend de RecorNet; escribir tests unitarios, E2E o de accesibilidad; revisar codigo frontend (lint, tipos, seguridad JWT, roles); comparar UI contra prototipos; o generar informes de calidad de pruebas. Tambien aplica a la app movil Capacitor/Ionic derivada de este frontend."
---

# RecorNet — Pruebas de Frontend y Auditoría UI/UX

Skill para ejecutar pruebas de código y auditorías UI/UX del frontend de **RecorNet**, software multiplataforma de recordatorio inteligente de medicamentos para adultos mayores, con rol de cuidador. Complementa el skill existente `recornet-capacitor-dev` (móvil) cubriendo la vertiente de verificación y calidad.

Antes de empezar, leer el contexto del proyecto: `docs/contexto/CONTEXTO GENRAL.md` (necesidades, público, flujo completo) y `docs/arquitectura/frontend.md` (stack Vue 3 + TS + Pinia + Vue Router + Axios + Tailwind, estructura de carpetas y accesibilidad WCAG 2.2). La web app apunta a `http://localhost:3000/api` en desarrollo y el backend es Flask + PostgreSQL + Celery + FCM + Cloudinary.

## Proceso general

Ejecutar las pruebas en este orden:

1. **Análisis estático de código** (sección 2)
2. **Pruebas automatizadas** (sección 3): unitarias y E2E
3. **Auditoría UI/UX y accesibilidad** (sección 4): heurística, contrastes, prototipos, Lighthouse
4. **Revisión de código de frontend** (sección 5)
5. **Informe de resultados** (sección 6, usar la plantilla de `templates/testing-report-template.md`)

## 1. Regla de oro: la accesibilidad no es negociable

El usuario final son adultos mayores y personas con discapacidad visual, auditiva, motriz o cognitiva. Todo hallazgo de accesibilidad con severidad **Alta** (contraste insuficiente, texto en `px` fijo, `<img>` de medicamento sin `alt`, área táctil < 44×44 px, foco invisible) bloquea la entrega. Ver detalles en `references/ui-ux-audit-criteria.md`.

## 2. Análisis estático de código

Ejecutar el script incluido antes de cualquier prueba dinámica (no requiere instalar dependencias):

```bash
bash scripts/lint_vue_a11y.sh frontend/src
```

Corrige los patrones que detecte: imágenes sin `alt`, `font-size` en `px`, `input` sin label, botones vacíos. Luego:

```bash
cd frontend
npm ci
npm run lint        # ESLint con vue-a11y
npm run typecheck   # vue-tsc --noEmit
```

## 3. Pruebas automatizadas

### 3.1 Unitarias (Vitest)

Tipos de tests a escribir y mantener:

- **Stores Pinia**: mutaciones de `auth`, `medication`, `reminder`, `statistics` y `user` con datos falsos; verificar estado inicial, acciones y getters.
- **Composables**: `useAuth.ts` (inyección de token, manejo de 401), `useAccessibility.ts` (cambio de tema/fuente/TTS), `useNotification.ts` (programación de recordatorios).
- **Servicios**: mockear Axios en `api.ts`; verificar interceptores y `multipart/form-data` para fotos de medicamentos.
- **Utils/validaciones**: dosis, frecuencias, fechas de inicio/fin del tratamiento, registros duplicados.

Mockear siempre la API; no depender del backend en unitarios.

### 3.2 E2E (Playwright)

Configurar `playwright.config.ts` con `baseURL` del frontend y reportes HTML. El catálogo completo de escenarios por módulo e ID (AUTH-01, MED-03, TOMA-01, EST-02, etc.) está en `references/e2e-test-cases.md`: leerlo y usarlo como fuente de verdad. Los escenarios críticos del producto son:

1. **Confirmación de toma** (TOMA-01 a TOMA-04): botón grande "Confirmar toma", registro de fecha/hora, historial y gestión de dosis pendientes/omitidas.
2. **Recordatorio completo** (REM-03): notificación con nombre, foto, dosis, descripción y hora programada.
3. **CRUD de medicamentos por el cuidador** (MED-01 a MED-07) con validaciones y confirmación de eliminación.
4. **Roles**: adulto mayor no accede a gestión de cuidador y viceversa.

```bash
npx playwright test              # suite completa
npx playwright test medications  # por módulo
```

Para tests sin backend disponible, interceptar con `page.route('**/api/**', ...)` devolviendo fixtures en `tests/fixtures/`.

## 4. Auditoría UI/UX y accesibilidad

Leer `references/ui-ux-audit-criteria.md` y ejecutar la auditoría en dos frentes:

**Automático:**

```bash
npx lighthouse http://localhost:5173 --quiet \
  --only-categories=accessibility,performance --output=json --output-path=lh.json
```

Y usar `@axe-core/playwright` dentro de los tests E2E para auditoría con axe. Umbral: Lighthouse ≥ 90 en Accessibility y Performance; cero violaciones críticas/serias en axe.

**Manual/heurístico:** navegar cada pantalla con teclado (Tabulación completa), zoom de texto al 200%, modo alto contraste y fuente del sistema ampliada. Verificar los criterios por discapacidad de la referencia (contraste 4.5:1/3:1, unidades `rem`, áreas táctiles ≥ 44×44 px, alertas visuales redundantes, confirmaciones, lenguaje sencillo, estados vacíos y de carga).

**Fidelidad vs prototipos:** comparar la implementación con `frontend/prototipe/web/` y `frontend/prototipe/Mobile/` (mapeo pantalla por pantalla en la referencia). Capturar screenshots con Playwright (`page.screenshot`) y revisar visualmente, o pedir la comparación a un modelo multimodal.

## 5. Revisión de código frontend

Antes de fusionar, aplicar el checklist de `references/code-review-checklist.md`. Puntos innegociables:

- JWT en interceptor de Axios con manejo amigable de 401/403; rutas con `meta.requiresAuth` y guard de rol.
- Fotos como `multipart/form-data` hacia Cloudinary vía backend.
- Sin `px` fijos en fuentes; tema de contraste ≥ 4.5:1; `alt` dinámico en fotos de medicamentos.
- `<script setup lang="ts">`, stores Pinia solo para estado global, lógica en composables.
- Sin degradación de cobertura ni de scores de accesibilidad respecto a la rama principal.

## 6. Informe de resultados

Generar el informe con `templates/testing-report-template.md`. Incluir: resultados por área (lint, tipos, unitarios, E2E, auditoría, Lighthouse), hallazgos priorizados por severidad con módulo afectado y recomendación, y veredicto final (fusionar / fusionar con condiciones / no aprobado). Entregar el informe como archivo Markdown junto con los logs de evidencia.

## Referencias

- `references/e2e-test-cases.md` — catálogo de escenarios E2E por rol y módulo con IDs para trazabilidad. Leer antes de escribir tests Playwright.
- `references/ui-ux-audit-criteria.md` — criterios de auditoría UI/UX y accesibilidad WCAG 2.2 por tipo de discapacidad, más mapeo de prototipos y umbrales de rendimiento. Leer antes de la auditoría.
- `references/code-review-checklist.md` — checklist de revisión de código Vue/TS/Pinia y comandos de verificación. Leer antes de revisar o fusionar código.
- `scripts/lint_vue_a11y.sh` — análisis estático rápido de accesibilidad en componentes Vue.
- `templates/testing-report-template.md` — plantilla del informe de pruebas.
