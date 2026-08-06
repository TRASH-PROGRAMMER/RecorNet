# 🧠  Recornet - Arquitectura y Stack Tecnológico frontend web

## 📝 Descripción general
**RecorNet** es un software multiplataforma (Android, iOS y Web) diseñado para ayudar a los adultos mayores a cumplir correctamente con el tratamiento de sus medicamentos mediante recordatorios inteligentes, accesibles y fáciles de utilizar.
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
### ⚙️ Stack: 


| Componente                 | Tecnología                                              |
| -------------------------- | ------------------------------------------------------- |
| Framework Frontend         | Vue.js                                                  |          
| lenguaje                   | TypeScript                                              |
| Router                     | Vue Router                                              |
| Estado                     | Pinia                                                   |
| HTTP                       | Axios                                                   |
| UI                         | Vuetify                                                 |
| tailwind                   | Css                                                     |


### 📱 Pantallas clave de la aplicación:

#### 1. 🧑 ** auth **
- Pantalla de login
- Pantalla de registro
#### 2. 🏠 ** dashboard **
- Pantalla de inicio
- Pantalla de perfil
- Pantalla de estadísticas
- Pantalla de notificaciones
#### 3. 🧑‍🤝‍🧑 ** medications **
- Pantalla de listado de medicamentos
- Pantalla de detalle de medicamentos
- Pantalla de creación de medicamentos
- Pantalla de edición de medicamentos
#### 4. 📅 ** reminders **
- Pantalla de listado de recordatorios
- Pantalla de detalle de recordatorios
- Pantalla de creación de recordatorios
- Pantalla de edición de recordatorios
#### 5. 👩‍🏫 ** statistics **
- Pantalla de listado de estadísticas
- Pantalla de detalle de estadísticas
- Pantalla de creación de estadísticas
- Pantalla de edición de estadísticas
#### 6. 👩‍🏫 ** caregivers **
- Pantalla de listado de cuidadores
- Pantalla de detalle de cuidadores
- Pantalla de creación de cuidadores
- Pantalla de edición de cuidadores
#### 7. 👩‍🏫 ** elderly **
- Pantalla de listado de adultos mayores
- Pantalla de detalle de adultos mayores
- Pantalla de creación de adultos mayores
- Pantalla de edición de adultos mayores
#### 8. 👩‍🏫 ** profile **
- Pantalla de perfil  

### 🔗 **Conexión con el backend**

La aplicación se conecta a un backend RESTful que proporciona una API para la gestión de usuarios, medicamentos, tratamientos, recordatorios inteligentes, notificaciones push, estadísticas y reportes.

El backend se encarga de gestionar la autenticación, autorización y autorización de acceso a las funciones de la aplicación. También se encarga de almacenar y gestionar los datos de usuarios, medicamentos, tratamientos, recordatorios inteligentes, notificaciones push, estadísticas y reportes.

La conexión entre el frontend y el backend se realiza mediante una API RESTful que proporciona una interfaz para la comunicación entre los dos sistemas. La API RESTful se encarga de proporcionar una API para la gestión de usuarios, medicamentos, tratamientos, recordatorios inteligentes, notificaciones push, estadísticas y reportes.


En services/api.ts:

import axios from "axios";

export const api = axios.create({ baseURL: "http://localhost:3000/api"});

