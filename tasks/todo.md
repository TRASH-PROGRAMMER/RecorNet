# RecorNet Backend — Tareas Fase 1

## Componente 1: Configuración del Proyecto
- [x] `requirements.txt` — dependencias Python
- [x] `.env.example` — plantilla de variables de entorno
- [x] `Dockerfile` — actualizado para instalar deps y exponer puerto
- [x] Estructura de carpetas `src/` con `__init__.py` (30 paquetes creados)
- [x] Estructura de carpetas `tests/` (unit, integration)

## Componente 2: Capa de Dominio
- [x] Entidades del dominio
- [x] Value objects
- [x] Repositorios abstractos
- [x] Puertos abstractos
- [x] Excepciones de dominio

## Componente 3: Infraestructura — Persistencia
- [ ] Modelos SQLAlchemy
- [ ] Repositorios concretos
- [ ] Configuración de database.py

## Componente 4: Capa de Aplicación — Use Cases
- [ ] Auth use cases (register, login, refresh)
- [ ] Medications use cases (CRUD)
- [ ] DTOs

## Componente 5: Infraestructura — API
- [ ] Rutas (auth, medications)
- [ ] Middlewares (JWT, roles)
- [ ] Validadores Pydantic
- [ ] Serializadores

## Componente 6: Configuración
- [ ] settings.py
- [ ] dependencies.py
- [ ] security.py

## Componente 7: Entrada Principal
- [ ] main.py (create_app factory)
- [ ] Shared (responses, enums)
- [ ] Verificación final
