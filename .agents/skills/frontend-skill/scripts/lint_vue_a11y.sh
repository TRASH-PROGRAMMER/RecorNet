#!/usr/bin/env bash
# lint_vue_a11y.sh — Análisis estático rápido de accesibilidad en componentes Vue de RecorNet.
# Uso: bash lint_vue_a11y.sh <directorio-src>
# Busca patrones de riesgo de accesibilidad sin requerir instalar dependencias.
# No sustituye a axe/Lighthouse; es un primer filtro de bajo costo.

set -u
SRC="${1:?Uso: bash lint_vue_a11y.sh <directorio-src>}"
EXIT=0

echo "== RecorNet: análisis estático de accesibilidad en $SRC =="

# 1. Imágenes sin alt
echo "--- <img> sin atributo :alt / alt ---"
grep -rn --include="*.vue" -E '<img[^>]*>' "$SRC" | grep -vE '\b(:?alt|aria-label|role="presentation")' && EXIT=1 || true

# 2. Font-size en px (debe ser rem/em para tipografía dinámica)
echo "--- font-size fijo en px ---"
grep -rn --include="*.vue" --include="*.css" --include="*.scss" -E 'font-size:\s*[0-9]+px' "$SRC" && EXIT=1 || true

# 3. Colores inline con posible bajo contraste (indicativo)
echo "--- estilos inline color/background-color ---"
grep -rn --include="*.vue" -E 'style="[^"]*(color|background-color):' "$SRC" && EXIT=1 || true

# 4. Botones sin texto visible ni aria-label
echo "--- <button> sin contenido visible ni aria-label ---"
grep -rn --include="*.vue" -E '<button[^>]*>\s*</button' "$SRC" && EXIT=1 || true

# 5. Inputs sin label asociado
echo "--- <input> sin label/id relacionado ---"
grep -rn --include="*.vue" -E '<input[^>]*>' "$SRC" | grep -vE '\b(aria-label|id|v-model)\b' && EXIT=1 || true

# 6. lang del documento
echo "--- lang de la página ---"
if ! grep -rn --include="index.html" -qE '<html[^>]*lang="es"' "$SRC/.." 2>/dev/null; then
  echo "ADVERTENCIA: index.html sin lang=\"es\""
  EXIT=1
fi

if [ "$EXIT" -eq 0 ]; then
  echo "OK: no se detectaron patrones de riesgo evidentes."
fi
exit "$EXIT"
