# Skill: Desarrollo de Aplicación Móvil RecorNet con Capacitor

Esta skill define el flujo de trabajo, las mejores prácticas y la configuración técnica necesaria para desarrollar la aplicación móvil multiplataforma de **RecorNet** utilizando **Capacitor**. Se enfoca en garantizar la accesibilidad para adultos mayores y la integración fluida con el backend de Clean Architecture analizado previamente.

## 1. Configuración del Entorno y Stack Frontend

Para mantener la coherencia con el backend y los requisitos de accesibilidad, se recomienda el siguiente stack tecnológico para el frontend móvil:

| Componente | Tecnología Recomendada | Razón de Elección |
| :--- | :--- | :--- |
| **Framework Base** | React o Vue.js | Alta capacidad de componentes reutilizables y gestión de estado. |
| **Runtime Nativo** | Capacitor | Permite convertir la web app en app nativa para iOS y Android con acceso a APIs de hardware. |
| **UI Framework** | Ionic Framework | Componentes pre-diseñados optimizados para móviles y con soporte nativo de accesibilidad. |
| **Gestión de Estado** | TanStack Query (React Query) | Sincronización eficiente con la API RESTful del backend. |
| **Estilos** | Tailwind CSS | Facilidad para implementar temas de alto contraste y tipografía dinámica. |

## 2. Integración de Funcionalidades Nativas (Capacitor Plugins)

RecorNet requiere acceso a funciones específicas del dispositivo para cumplir con sus objetivos de recordatorios inteligentes:

> **Importante:** La implementación de recordatorios debe ser redundante, utilizando tanto notificaciones push (Firebase) como notificaciones locales para asegurar que el adulto mayor reciba la alerta incluso sin conexión estable.

*   **@capacitor/local-notifications:** Esencial para programar las alarmas de medicamentos que deben sonar puntualmente. Permite configurar sonidos personalizados y vibración.
*   **@capacitor/push-notifications:** Integración con Firebase Cloud Messaging (FCM) para recibir actualizaciones del cuidador en tiempo real.
*   **@capacitor/camera:** Utilizado para que el usuario o cuidador capture la fotografía del medicamento durante el registro (CRUD).
*   **@capacitor/text-to-speech:** Fundamental para la accesibilidad, permitiendo que la aplicación "lea" el nombre del medicamento y la dosis al activar el recordatorio.
*   **@capacitor/haptics:** Proporciona retroalimentación física (vibración) clara al interactuar con botones grandes o recibir alertas.

## 3. Implementación de Accesibilidad (Diseño Universal)

Siguiendo las pautas WCAG mencionadas en el contexto general, el desarrollo debe seguir estas reglas estrictas:

1.  **Tipografía Dinámica:** Utilizar unidades `rem` o `em` para que los textos respeten la configuración de tamaño de fuente del sistema operativo del usuario.
2.  **Áreas de Interacción:** Todos los botones deben tener un tamaño mínimo de 44x44 puntos para facilitar la interacción de personas con dificultades motrices.
3.  **Contraste Elevado:** Implementar un sistema de temas que garantice un contraste mínimo de 4.5:1 para texto normal y 3:1 para texto grande.
4.  **Soporte de Lectores de Pantalla:** Uso correcto de etiquetas ARIA y atributos `alt` en las fotografías de los medicamentos.

## 5. Flujo de Sincronización con el Backend

La comunicación entre la app de Capacitor y el backend de Flask debe estructurarse de la siguiente manera:

*   **Autenticación:** Almacenamiento seguro del JWT utilizando `@capacitor/preferences`.
*   **Interceptores de API:** Implementar lógica para adjuntar el token en cada petición y manejar la expiración de sesión de forma amigable para el usuario.
*   **Manejo de Imágenes:** Las fotos capturadas con la cámara deben enviarse como `multipart/form-data` hacia el endpoint del backend que conecta con Cloudinary.

## 6. Comandos Esenciales de Desarrollo

Para el mantenimiento y despliegue de la aplicación, se utilizarán los siguientes comandos base:

```bash
# Sincronizar cambios de la web app con los proyectos nativos
npx cap copy

# Abrir el proyecto en Android Studio o Xcode
npx cap open android
npx cap open ios

# Instalar nuevos plugins nativos
npm install @capacitor/plugin-name
npx cap sync
```

---
**Autor:** Manus AI
**Versión:** 1.0.0
**Referencia:** Basado en el análisis de arquitectura de RecorNet y CONTEXTOGENRAL.md.
