# Checklist de Revisión de Código Frontend (RecorNet)

Checklist de código para Vue 3 + TypeScript + Pinia + Vue Router + Axios + Tailwind, alineado con la estructura de `docs/arquitectura/frontend.md` y el skill existente `recornet-capacitor-dev`. Ejecutar tras cada cambio significativo en `frontend/` y antes de fusionar a la rama principal.

## 1. Estructura y convenciones

1. Los nuevos archivos siguen la estructura acordada: `components/`, `views/`, `composables/`, `services/`, `store/` (Pinia), `types/`, `utils/`, `constants/`.
2. Los componentes usan `<script setup lang="ts">` con tipado completo (sin `any`).
3. Cada vista pública del router tiene meta `requiresAuth` y guard de rol.
4. Las cadenas con API usan el cliente central de `services/api.ts` (baseURL `http://localhost:3000/api` en dev), nunca `fetch`/`axios` directos en componentes.
5. Los stores Pinia se limitan a estado global (auth, medication, reminder, statistics, user); la lógica derivada va en composables (`useAuth.ts`, `useAccessibility.ts`, `useStatistics.ts`).
6. No hay credenciales hardcodeadas; la base de la API va de `.env`/`import.meta.env`.

## 2. Seguridad y autenticación

1. El JWT se persiste en `@capacitor/preferences` (móvil) o `localStorage` (web) y se inyecta vía interceptor de Axios (`Authorization: Bearer <token>`).
2. Manejo amigable de 401/403: interceptor redirige a login con mensaje, sin errores crudos al usuario.
3. Las rutas protegidas verifican rol: adulto mayor no puede acceder a gestión de cuidador y viceversa (validar en router y en backend).
4. Las fotos de medicamentos se envían como `multipart/form-data` hacia el endpoint de Cloudinary del backend.

## 3. Accesibilidad en código

1. Tipografía exclusivamente en `rem`/`em` (prohibido `px` fijos en `font-size`).
2. Botones y áreas táctiles ≥ 44×44 px (CSS o utility `min-h-11 min-w-11`).
3. Colores con contraste ≥ 4.5:1 normal / 3:1 grande; revisar el tema en `styles/`.
4. Todo `<img>` con `:alt` dinámico (foto de medicamento → nombre del medicamento).
5. Formularios con `<label>` asociado, `aria-describedby` para errores y `aria-invalid`.
6. Focus trapping en modales de confirmación (eliminar medicamento, omitir dosis).
7. Composable `useAccessibility` centraliza fuente, contraste, TTS y vibración.

## 4. Calidad general

1. `npm run typecheck` (o `vue-tsc --noEmit`) sin errores.
2. Linter sin warnings nuevos; reglas de accesibilidad activas (eslint-plugin-vue-a11y).
3. Tests unitarios pasan y la cobertura del módulo tocado no baja.
4. Sin `console.log` ni código muerto en componentes.
5. Manejo de errores en toda llamada de servicio (try/catch o `onError` de TanStack Query/`usePromise`).
6. Estado de carga y error renderizados en toda vista que consume API.
7. No mutar props; emits tipados con `defineEmits<{ ... }>()`.
8. Componentes reutilizables de accesibilidad en `components/accessibility/` (FontSizeToggle, ContrastToggle, VoiceReader, LargeButton).

## 5. Comandos de verificación

```bash
cd frontend
npm ci                      # instalar dependencias
npm run lint                # ESLint + vue-a11y
npm run typecheck           # vue-tsc --noEmit
npm run test:unit           # Vitest unitarios
npm run test:e2e            # Playwright E2E (requiere backend/mock)
npm run build               # verificar build de producción
npx lighthouse http://localhost:5173 --quiet \
  --only-categories=accessibility,performance --output=json --output-path=lh.json
```

## 6. Criterios de aceptación de un PR frontend

1. Pasa el pipeline completo: lint → typecheck → unit → e2e (o mocks).
2. Sin degradación de accesibilidad: axe sin violaciones críticas/serias.
3. Screenshots de Playwright si cambió UI (comparar con `frontend/prototipe/`).
4. Documenta cambios de rutas, stores o contratos de servicio en el PR.
5. Cambios de estilo revisados en modo alto contraste y con fuente ampliada (200%).
