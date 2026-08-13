# Criterios de Auditoría UI/UX y Accesibilidad (RecorNet)

Checklist de verificación para la revisión manual o asistida de UI/UX. Los requisitos provienen de `docs/arquitectura/frontend.md` (WCAG 2.2, Diseño Universal, leyes de usabilidad) y del skill existente `recornet-capacitor-dev` (móvil). La audiencia principal son adultos mayores y personas con discapacidad visual, auditiva, motriz o cognitiva: elevar el listón de accesibilidad por encima de lo habitual.

## 1. Accesibilidad — Discapacidad visual

| # | Criterio | Umbral | Cómo verificar |
|---|----------|--------|----------------|
| 1.1 | Contraste texto normal | ≥ 4.5:1 (WCAG AA) | Herramienta de contraste o axe |
| 1.2 | Contraste texto grande/UI | ≥ 3:1 | Igual |
| 1.3 | Unidades relativas de fuente | `rem`/`em` en todo el texto | Buscar `px` fijos en fuentes con grep |
| 1.4 | Tamaño base ampliable | Escala con preferencia del sistema | Cambiar `font-size` root en devtools |
| 1.5 | Atributo `alt` en fotos de medicamentos | 100% de `<img>` | Lighthouse o axe |
| 1.6 | Compatibilidad con lectores de pantalla | Roles/labels ARIA correctos | Navegar solo con teclado + screen reader |
| 1.7 | Estado de foco visible | Outline ≥ 2px, contraste suficiente | Tabulación completa |
| 1.8 | Lenguaje de página | `lang="es"` en `<html>` | Inspección del DOM |

## 2. Accesibilidad — Discapacidad motriz

| # | Criterio | Umbral | Cómo verificar |
|---|----------|--------|----------------|
| 2.1 | Tamaño mínimo de área táctil | 44×44 px | Medición manual o axe |
| 2.2 | Espaciado entre elementos interactivos | ≥ 8 px | Medición manual |
| 2.3 | Sin gestos complejos (swipes, zoom multi-touch) | 0 en flujos críticos | Revisión de interacciones |
| 2.4 | Tareas completas en ≤ 3 pasos | Flujos: confirmación de toma, añadir medicamento | Conteo de pasos en prototipo/implementación |

## 3. Accesibilidad — Discapacidad auditiva y cognitiva

| # | Criterio | Umbral | Cómo verificar |
|---|----------|--------|----------------|
| 3.1 | Alertas visuales redundantes ante eventos sonoros | Presente en recordatorios | Revisión UI de recordatorio |
| 3.2 | Confirmaciones antes de acciones destructivas | Diálogo en eliminar/omitir | E2E TOMA-04, MED-05 |
| 3.3 | Lenguaje sencillo, sin jerga médica | Revisión de copy | Lectura de textos de UI |
| 3.4 | Un mensaje de error por campo, con solución | Mensajes claros | Validación de formularios |
| 3.5 | Colores consistentes por estado (tomada/pendiente/omitida) | Semántica constante | Revisión de temas |
| 3.6 | Opciones por pantalla limitadas (Ley de Hick) | Máx. 4–6 acciones visibles | Revisión de pantallas clave |

## 4. Principios de usabilidad (revisión heurística)

1. **Interfaz intuitiva y navegación consistente**: mismo layout, misma posición de menú en todas las pantallas.
2. **Retroalimentación inmediata**: spinners/estados de carga en toda acción asíncrona (< 200 ms percepción).
3. **Prevención de errores**: validación inline, campos obligatorios marcados, evitar duplicados.
4. **Recuperación de errores**: mensajes accionables, deshacer posible en ediciones.
5. **Ley de Fitts**: botones de acción principal grandes y cerca del borde/borde inferior en móvil.
6. **Ley de Proximidad**: datos del medicamento (foto, dosis, horario) agrupados en una tarjeta.
7. **Estado vacío**: toda lista sin datos muestra mensaje y CTA, nunca pantalla en blanco.
8. **Estados de carga y error**: skeletons o placeholders mientras cargan datos de API.

## 5. Correspondencia con prototipos

Los prototipos en `frontend/prototipe/web/` y `frontend/prototipe/Mobile/` son la referencia visual. Comparar pantalla por pantalla:

- Login web y móvil → `inicio-de-seccion-rol-cuidador.png`, `mobile*.png`
- Dashboard adulto mayor → `dasboard-rol-adulto-mayor*.png`
- Dashboard cuidador → `dasboard-rol-cuidador*.png`
- CRUD medicamentos cuidador → `añadir-medicamento-rol-cuidador*.png`, `editar-medicamento-rol cuidador.png`, `gestion de inventario-rol cuidador.png`
- Historial → `historial-de-tomas-rol-adulto-mayor*.png`, `historial-de-tomas-rol-cudiador.png`
- Estadísticas → `estadisticas*.png`, `estadistica.png`
- Tema/estilos → `theme.png`

Ejecutar la comparación con capturas automatizadas de Playwright contra los prototipos o con revisión visual asistida por LLM (ver SKILL.md sección 4).

## 6. Pruebas de rendimiento visual

- Lighthouse ≥ 90 en Performance, Accessibility, Best Practices y SEO para la web.
- No bloqueo del hilo principal durante la animación del recordatorio (alarma/voz).
- Imágenes de medicamentos optimizadas (webp/avif, lazy loading fuera de viewport).
- Tiempo hasta interactividad < 3 s en red 4G simulada (`--throttling-profile`).
