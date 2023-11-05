"""Módulo de contenedores"""

# Importa el módulo de containers y providers de la librería dependency_injector.
# Estos módulos son utilizados para la inyección de dependencias en la aplicación,
# lo que permite una configuración más flexible y una mejor desacoplación de componentes.
from dependency_injector import containers, providers

# Importa la clase Database del módulo de base de datos local.
# Esta clase se encarga de la gestión de conexiones y operaciones con la base de datos.
from .database import Database
import os  # Importa el módulo os para acceder a las variables de entorno del sistema operativo.

# Define la clase Container que hereda de DeclarativeContainer de dependency_injector.
# Esta clase actúa como un contenedor para la configuración de servicios y recursos,
# lo que permite un manejo centralizado de las dependencias en la aplicación.
class Container(containers.DeclarativeContainer):

    # Crea un proveedor singleton para la base de datos.
    # Un singleton es un patrón de diseño que restringe la instanciación de una clase a un solo objeto.
    # Aquí, se asegura que solo haya una instancia de Database en toda la aplicación.
    # La URL de la base de datos se obtiene de las variables de entorno, usando "DATABASE_URL" como clave.
    # Si "DATABASE_URL" no se encuentra en las variables de entorno, se utiliza None como valor predeterminado.
    db = providers.Singleton(Database, db_url=os.environ.get("DATABASE_URL", None))
