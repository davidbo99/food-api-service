# README para el Proyecto de Recetas (BACKEND)

## Descripción
Este proyecto es el backend de una aplicación de recetas, desarrollado utilizando FastAPI, SQLAlchemy y Alembic. Ofrece funcionalidades como búsqueda de recetas, creación de usuarios, autenticación, y manejo de migraciones de base de datos.

## Requisitos Previos
- Python 3.8 o superior
- [Poetry](https://python-poetry.org/docs/#installation)

## Configuración del Entorno
1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
   ```

2. Instala las dependencias:
   ```bash
   poetry install
   ```

3. Crea un archivo de configuración `.env` en la raíz del proyecto y añade las variables de entorno necesarias. Ejemplo:
   ```env
   DATABASE_URL=sqlite:///./test.db
   SECRET_KEY=tu_clave_secreta
   ```

## Inicialización de la Base de Datos
1. Ejecuta las migraciones para inicializar la base de datos:
   ```bash
   poetry run alembic upgrade head
   ```

## Ejecutar el Servidor de Desarrollo
1. Inicia el servidor de desarrollo:
   ```bash
   poetry run uvicorn main:app --reload
   ```
   Aquí, `main` es el nombre del archivo Python que contiene tu aplicación FastAPI, y `app` es el nombre de la instancia de la aplicación FastAPI.

2. Abre tu navegador y visita [http://localhost:8000](http://localhost:8000). Deberías ver la interfaz de usuario de FastAPI.

## Ejecutar Pruebas
1. Para ejecutar las pruebas, usa el siguiente comando:
   ```bash
   poetry run pytest
   ```

## Contribuir
Si deseas contribuir al proyecto, considera seguir las siguientes prácticas:

1. Crea una nueva rama para tu característica o corrección.
2. Escribe código limpio y sigue las guías de estilo.
3. Asegúrate de que todas las pruebas pasen antes de hacer un push.
4. Crea una solicitud de pull y asegúrate de que pasa todas las verificaciones de CI.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT - ve el archivo [LICENSE](LICENSE) para más detalles.

## Contacto
Si tienes alguna pregunta o necesitas ayuda, no dudes en contactar al equipo de desarrollo.

---

Este README proporciona una guía básica para comenzar con el proyecto, instalar dependencias, ejecutar el servidor de desarrollo, y contribuir al proyecto. Puedes expandirlo según las necesidades específicas de tu proyecto.