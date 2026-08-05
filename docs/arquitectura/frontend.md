# 🧠  Recornet - Arquitectura y Stack Tecnológico frontend web

## 📝 Descripción general
*RecorNet** es un software multiplataforma (Android, iOS y Web) diseñado para ayudar a los adultos mayores a cumplir correctamente con el tratamiento de sus medicamentos mediante recordatorios inteligentes, accesibles y fáciles de utilizar.
El frontend es el componente que se encarga de mostrar la interfaz de usuario de la aplicación. El frontend se compone de una aplicación web que se ejecuta en el navegador del usuario, y se utiliza para mostrar la interfaz de usuario de la aplicación.

## 🏗️ Arquitectura General
El frontend de **RecorNet** se compone de una aplicación web que se ejecuta en el navegador del usuario, y se utiliza para mostrar la interfaz de usuario de la aplicación.

### 🏗️ Estructura del proyecto
 ````
 frontend/
│
├── public/
│
├── src/
│   │
│   ├── assets/                  # Imágenes, íconos, fuentes y estilos
│   │
│   ├── components/              # Componentes reutilizables
│   │   ├── common/
│   │   ├── forms/
│   │   ├── charts/
│   │   ├── notifications/
│   │   └── accessibility/
│   │
│   ├── views/                   # Páginas
│   │   ├── auth/
│   │   ├── dashboard/
│   │   ├── medications/
│   │   ├── reminders/
│   │   ├── statistics/
│   │   ├── caregivers/
│   │   ├── elderly/
│   │   └── profile/
│   │
│   ├── layouts/                 # Layouts generales
│   │   ├── AdminLayout.vue
│   │   ├── AuthLayout.vue
│   │   └── EmptyLayout.vue
│   │
│   ├── router/
│   │
│   ├── store/                   # Pinia
│   │   ├── auth.store.ts
│   │   ├── medication.store.ts
│   │   ├── reminder.store.ts
│   │   ├── statistics.store.ts
│   │   └── user.store.ts
│   │
│   ├── services/                # Comunicación con el backend
│   │   ├── api.ts
│   │   ├── auth.service.ts
│   │   ├── medication.service.ts
│   │   ├── reminder.service.ts
│   │   ├── statistics.service.ts
│   │   └── upload.service.ts
│   │
│   ├── composables/             # Lógica reutilizable
│   │   ├── useAuth.ts
│   │   ├── useNotification.ts
│   │   ├── useAccessibility.ts
│   │   └── useStatistics.ts
│   │
│   ├── types/                   # Interfaces y tipos TypeScript
│   │
│   ├── utils/                   # Funciones auxiliares
│   │
│   ├── constants/               # Constantes
│   │
│   ├── plugins/                 # Axios, VueUse, etc.
│   │
│   ├── styles/                  # CSS global
│   │
│   ├── App.vue
│   └── main.ts
│
├── tests/
│
├── package.json
├── vite.config.ts
├── tsconfig.json
├── .env
└── README.md
````
