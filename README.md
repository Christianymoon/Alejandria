
# Alejandria

Sistema de gestión de inventario y préstamos para bibliotecas.

## Stack Tecnológico
- **Lenguaje:** Python 3.11
- **Framework:** FastAPI
- **ORM:** SQLAlchemy
- **Base de Datos:** SQLite
- **Validación:** Pydantic v2

## Documentación de la API

### Resumen de Endpoints (rutas reales)

Base URL: `http://127.0.0.1:8000`

- Root:
   - `GET /` — mensaje de bienvenida.

- Autenticación (`/auth`):
   - `POST /auth/signup` — registrar administrador (body según `UserAdminBase`).
   - `POST /auth/token` — obtener token (form-data: `username`, `password`).

- Usuarios (`/users`) — requiere autenticación:
   - `GET /users/` — listar usuarios.
   - `POST /users/` — crear usuario (body: `UserCreate`).
   - `PUT /users/{user_id}` — actualizar usuario (body: `UserUpdate`).
   - `DELETE /users/{user_id}` — eliminar usuario.
   - `GET /users/{user_id}/movements` — listar movimientos del usuario.

- Inventario (`/inventory`) — requiere autenticación:
   - `GET /inventory/` — listar inventario.
   - `GET /inventory/history` — historial completo de inventario.
   - `GET /inventory/{inventory_id}/history` — historial por inventario.
   - `POST /inventory/` — crear inventario (body: `InventoryCreate`).
   - `PUT /inventory/{inventory_id}` — actualizar inventario (body: `InventoryUpdate`).

- Publicaciones (`/publications`) — requiere autenticación:
   - `GET /publications/` — listar publicaciones.
   - `GET /publications/{publication_id}` — obtener publicación.
   - `GET /publications/{publication_id}/history` — historial de inventario de la publicación.
   - `POST /publications/` — crear publicación (body: `PublicationCreate`).
   - `DELETE /publications/{publication_id}` — eliminar publicación.

- Movimientos (`/movements`) — requiere autenticación:
   - `GET /movements/` — listar movimientos.
   - `GET /movements/user/{user_id}` — listar movimientos por usuario.
   - `POST /movements/` — crear movimiento (body: `MovementCreate`).

## ▶️ Guía de Inicio

### 🛠️ Método Manual
1. **Crear entorno virtual:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```
2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configurar variables:** Crear `.env` desde `.env.example`.
4. **Ejecutar:**
   ```bash
   python -m uvicorn backend.main:app --reload
   ```

### ⚡ Método Automático
Tras instalar dependencias
``` bash
pip install -r requirements.txt
```

ejecute:
```bash
python run_server.py
```


