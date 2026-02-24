# 🧱 Django Code Generator - Clean Architecture

Este proyecto permite **generar automáticamente archivos CRUD** (Entity, UseCase, Repository, etc.) siguiendo los principios de **Arquitectura Limpia en Django**, usando un modelo existente como fuente.

## 🚀 ¿Qué genera?

A partir de un modelo Django existente, este generador crea:

- `domain/entities/<Model>Entity.py`
- `application/usecases/<model>_usecase.py`
- `application/repositories/<model>_repository.py`
- `infraestructure/repositories/django<model>_repository.py`
- `presentation/views/<model>_view.py` *(si aplica)*

---

## 📦 Instalación

1. Clona este repositorio o instala desde PyPI/Git.
    Ejm: pip install git+https://github.com/ZequerVirus/CleanCrud.git
2. Asegúrate de tener tu modelo dentro de un archivo `models.py`.

Ejemplo de estructura mínima esperada:

app_content/
├── models.py ← aquí debe estar tu modelo original
├── domain/
├── application/
└── infraestructure/


3. Asegúrate de tener en `INSTALLED_APPS` la app que contiene el comando, por ejemplo:

```python
INSTALLED_APPS = [
    ...
    "app_content",
]
```

## Uso del comando 

python manage.py generate_crud \
    --model=NombreDelModelo \
    --basepath=app_content \
    --model_path=app_content/models.py \
    --language=python
