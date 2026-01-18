# 📚 Biblioteca App

Sistema de gestión de inventario y préstamos para bibliotecas.

## 🚀 Stack Tecnológico
- **Lenguaje:** Python 3.11
- **Framework:** FastAPI
- **ORM:** SQLAlchemy
- **Base de Datos:** SQLite
- **Validación:** Pydantic v2

## � Documentación de la API

### 📖 Publicaciones (`/publications`)

Manejo del catálogo de libros y publicaciones.

#### `GET /publications/`
Obtiene la lista de todas las publicaciones registradas.
- **Parámetros:** Ninguno.

#### `GET /publications/view/{publication_id}`
Obtiene el detalle de una publicación específica.
- **Parámetros de ruta:**
  - `publication_id` (int): ID único de la publicación.

#### `POST /publications/`
Crea una nueva publicación en el sistema.
- **Body (JSON):**
  - `name` (str): Nombre de la publicación.
  - `year` (int): Año de publicación.
  - `month` (int): Mes de publicación.
  - `type` (str): Tipo de publicación (ej. libro, revista).
  - `code` (str): Código único de identificación (ISBN o interno).

---

### 📦 Inventario (`/inventory`)

Gestión del stock físico de las publicaciones.

#### `GET /inventory/`
Lista el inventario actual de todas las publicaciones.
- **Parámetros:** Ninguno.

#### `POST /inventory/`
Registra inventario inicial para una publicación.
- **Body (JSON):**
  - `publication_id` (int): ID de la publicación.
  - `total_quantity` (int): Cantidad total de ejemplares.
  - `available_quantity` (int): Cantidad disponible inicialmente.

---

### 🔄 Movimientos (`/movements`)

Registro de préstamos y devoluciones.

#### `GET /movements/`
Lista el historial de todos los movimientos realizados.
- **Parámetros:** Ninguno.

#### `POST /movements/`
Registra un nuevo movimiento (préstamo o devolución).
- **Body (JSON):**
  - `user_id` (int): ID del usuario que realiza el movimiento.
  - `publication_id` (int): ID de la publicación involucrada.
  - `quantity` (int): Cantidad de ejemplares.
  - `movement_type` (str): Tipo de movimiento (`IN` para devoluciones, `OUT` para préstamos).
  - `notes` (str, opcional): Notas adicionales.

---

### 👥 Usuarios (`/users`)

Gestión de usuarios del sistema.

#### `GET /users/`
Obtiene la lista de todos los usuarios registrados.
- **Parámetros:** Ninguno.

#### `POST /users/`
Registra un nuevo usuario.
- **Body (JSON):**
  - `username` (str): Nombre de usuario.
  - `role_id` (int): ID del rol asignado.
  - `is_active` (bool): Estado activo/inactivo.

## ▶️ Cómo correr el proyecto (Metodo manual)

1. **Crear entorno virtual:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar variables de entorno:**
   - Crear un archivo `.env` basado en `.env.example`.

4. **Correr el servidor:**
   ```bash
   python -m uvicorn backend.main:app --reload
   ```

## Como correr el proyecto (Metodo automatico)
1. **Simplemente ejecute el siguiente archivo despues de activar el entorno virtual e instalar las dependencias requeridas**

  ```bash
  python run_server.py
  ```

