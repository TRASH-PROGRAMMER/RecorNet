# Informe de Pruebas Frontend — RecorNet

**Fecha:** [AAAA-MM-DD] | **Alcance:** [versión/rama/cambio] | **Autor:** [nombre]

## Resumen ejecutivo

[2–4 frases con el veredicto general: aprobado / aprobado con condiciones / no aprobado, y los hallazgos más relevantes de UI/UX y código.]

## 1. Pruebas de código

| Área | Resultado | Evidencia |
|------|-----------|-----------|
| Lint + vue-a11y | ✅ / ❌ | Log de `npm run lint` y `lint_vue_a11y.sh` |
| Tipado TypeScript | ✅ / ❌ | `vue-tsc --noEmit` |
| Tests unitarios (Vitest) | ✅ / ❌ | X/Y pasaron, cobertura Z% |
| Tests E2E (Playwright) | ✅ / ❌ | X/Y escenarios pasaron |
| Seguridad/auth (JWT, roles, rutas) | ✅ / ❌ | Hallazgos |

## 2. Auditoría UI/UX y accesibilidad

| Bloque | Cumplimiento | Hallazgos |
|--------|--------------|-----------|
| WCAG 2.2 — discapacidad visual | ✅ / ❌ | Contrastes, alt, foco, rem |
| Discapacidad motriz (≥44×44 px) | ✅ / ❌ | Áreas táctiles |
| Discapacidad auditiva/cognitiva | ✅ / ❌ | Alertas visuales, lenguaje, confirmaciones |
| Usabilidad (heurísticas) | ✅ / ❌ | Hick, Fitts, estados vacíos/carga |
| Lighthouse | P: _ A: _ | Scores |
| Fidelidad vs prototipos | ✅ / ❌ | Pantallas comparadas |

## 3. Hallazgos priorizados

| # | Severidad | Hallazgo | Módulo | Recomendación |
|---|-----------|----------|--------|---------------|
| 1 | Alta/Media/Baja | | | |

## 4. Veredicto y próximos pasos

[Recomendación final: fusionar, fusionar con condiciones, o rehacer; y los 2–3 siguientes pasos inmediatos.]
