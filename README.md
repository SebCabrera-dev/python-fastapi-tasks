# API REST & Aplicación Web de Gestión de Tareas (FastAPI + SQLite)

Aplicación web completa y API RESTful desarrollada en Python utilizando FastAPI y SQLAlchemy para la gestión de tareas en tiempo real con persistencia en base de datos SQLite.

## 🚀 Características
- **API RESTful Completa:** Endpoints para operaciones CRUD (obtención, creación y eliminación de tareas).
- **Persistencia de Datos (ORM):** Integración con SQLAlchemy y SQLite para el almacenamiento permanente de información.
- **Interfaz Web Intuitiva:** Frontend interactivo (HTML/CSS/JS) servido directamente por FastAPI para una experiencia de usuario limpia y fluida.
- **Validación de Datos:** Uso de Pydantic Schemas para la estructura de peticiones e inspección de datos.
- **Documentación Interactiva:** Generada automáticamente por Swagger UI (`/docs`).

## 🛠️ Tecnologías Utilizadas
- **Backend:** Python 3, FastAPI, Uvicorn
- **Base de Datos / ORM:** SQLite, SQLAlchemy
- **Frontend:** HTML5, CSS3, JavaScript (Fetch API)
- **Control de Versiones:** Git & GitHub

⚙️ Instalación y Ejecución Local

1. Clona el repositorio: 
        python-fastapi-tasks
2. Instala las dependencias: 
        pip install fastapi uvicorn sqlalchemy pydantic
3. Inicia el servidor:
        python -m uvicorn main:app --reload
4. Abre en tu navegador la direccion el enlace dado
        Aplicación Web: http://xxx.x.x.x:xxxx
        Documentación Swagger UI: http://xxx.x.x.x:xxxx/docs