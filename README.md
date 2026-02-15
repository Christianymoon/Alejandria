
# Alejandria

Sistema de gestión de inventario y préstamos para bibliotecas.

## Stack Tecnológico
- **Lenguaje:** Python 3.11
- **Framework:** FastAPI
- **ORM:** SQLAlchemy
- **Base de Datos:** SQLite
- **Validación:** Pydantic v2

## Documentación de la API

### Publicaciones (`/publications`)

Manejo del catálogo de libros y publicaciones.

#### `GET /publications/`
Obtiene la lista de todas las publicaciones registradas.

#### `GET /publications/view/{publication_id}`
Obtiene el detalle de una publicación específica.

#### `POST /publications/`
Crea una nueva publicación.
- **Body (JSON):** `name`, `year`, `month`, `type`, `code`.

#### `PUT /publications/{publication_id}`
Actualiza los datos de una publicación existente.

#### `DELETE /publications/{publication_id}`
Elimina una publicación del sistema.

---

### 📦 Inventario (`/inventory`)

Gestión del stock físico de las publicaciones.

#### `GET /inventory/`
Lista el inventario actual de todas las publicaciones.

#### `GET /inventory/{publication_id}`
Consulta el stock disponible de una publicación específica.

#### `POST /inventory/`
Registra inventario inicial para una publicación.
- **Body (JSON):** `publication_id`, `total_quantity`, `available_quantity`.

#### `PUT /inventory/{publication_id}`
Actualiza manualmente las cantidades de stock.

---

### 🔄 Movimientos (`/movements`)

Registro de préstamos y devoluciones.

#### `GET /movements/`
Lista el historial de todos los movimientos realizados.

#### `POST /movements/`
Registra un nuevo movimiento.
- **Body (JSON):** `user_id`, `publication_id`, `quantity`, `movement_type` (`IN`/`OUT`).

---

### 👥 Usuarios (`/users`)

Gestión de usuarios del sistema.

#### `GET /users/`
Obtiene la lista de todos los usuarios registrados.

#### `GET /users/{user_id}`
Obtiene el detalle de un usuario específico.

#### `POST /users/`
Registra un nuevo usuario.
- **Body (JSON):** `username`, `role_id`, `is_active`.

#### `PUT /users/{user_id}`
Actualiza la información o estado de un usuario.

#### `DELETE /users/{user_id}`
Elimina un usuario del sistema.

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


