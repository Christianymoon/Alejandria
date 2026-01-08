# 📚 Biblioteca App

Sistema de gestión de inventario y préstamos para bibliotecas.

## 🚀 Stack
- Python 3.11
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic v2

## 📂 Estructura
- backend/
  - api/
  - core/
  - models/
  - schemas/
  - services/
  - repositories/

## ▶️ Cómo correr el proyecto

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Crear archivo .env usando el archivo .env.example

python -m uvicorn backend.main:app --reload
