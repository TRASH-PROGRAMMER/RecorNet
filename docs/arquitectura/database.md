| Tabla             | Tipo         | Clave           | Comentarios                                                                  |
| ----------------- | ------------ | --------------- | ---------------------------------------------------------------------------- |
| `users`           | Tabla        | `id` (PK)       | Usuario principal (adulto mayor o cuidador).                                 |
| `profiles`        | Tabla        | `user_id` (PK/FK) | Extensión opcional del usuario con datos adicionales.                          |
| `user_roles`      | Tabla        | `(user_id, role_id)` | Tabla puente para N:M entre usuarios y roles.                                |
| `roles`           | Tabla        | `id` (PK)       | Roles: paciente, cuidador, admin, etc.                                       |
| `medications`     | Tabla        | `id` (PK)       |medicamentos.                                |
| `treatments`      | Tabla        | `id` (PK)       | Tratamientos, define dosis y horarios. FK `patient_user_id`, `creator_user_id`. |
| `reminder_schedules` | Tabla | `id` (PK) | Horarios/repetición de dosis. FK `treatment_id`.                           |
| `dose_events`     | Tabla        | `id` (PK)       | Instancias de dosis programadas. FK `schedule_id`, `medication_id`.        |
| `notifications`   | Tabla        | `id` (PK)       | Notificaciones enviadas. FK `dose_event_id`, `recipient_user_id`.           |
| `user_devices`    | Tabla        | `id` (PK)       | Dispositivos registrados (tokens FCM).                                       |
| `statistics_snapshots` | Tabla | `id` (PK) | Snapshot histórico de estadísticas (opcional).                                |
| `reports`         | Tabla        | `id` (PK)       | Reportes generados. FK `subject_user_id`, `created_by_user_id`.            |