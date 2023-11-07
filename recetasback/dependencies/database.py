"""Módulo de bases de datos"""

# Importaciones necesarias para manejo de contextos, enumeraciones y SQL Alchemy para ORM.
from contextlib import contextmanager
from enum import Enum, auto
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

import logging

# Configuración del sistema de registro de eventos (logging) a nivel de información.
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define una enumeración para representar los posibles estados de la base de datos.
class HealthStatus(Enum):
    CONNECTED = auto()      # Estado cuando la base de datos está conectada.
    DISCONNECTED = auto()   # Estado cuando la base de datos está desconectada.
    UNKNOWN = auto()        # Estado cuando el estado de la base de datos es desconocido.

# Define una clase para manejar la conexión con la base de datos.
class Database:

    def __init__(self, db_url: str) -> None:
        # Al inicializar la clase, crea un motor de base de datos con la URL proporcionada y lo configura para mostrar las consultas en consola.
        self._engine = create_engine(db_url, echo=True)
        # Crea una fábrica de sesiones de base de datos vinculada al motor creado.
        self._db = sessionmaker(autocommit=False, autoflush=False, bind=self._engine)
        
    def get_status(self) -> HealthStatus:
        # Método para obtener el estado actual de la base de datos.
        try:
            # Intenta crear una conexión temporal con la base de datos.
            with self._engine.connect() as conn:
                # Si la conexión es exitosa, devuelve el estado de CONECTADO.
                return HealthStatus.CONNECTED
        except SQLAlchemyError as e:
            # Si hay un error de SQLAlchemy, registra el error y devuelve el estado de DESCONECTADO.
            logger.error(f"Error al conectar a la base de datos: {e}")
            return HealthStatus.DISCONNECTED
        except Exception as e:
            # Para cualquier otro error inesperado, registra el error y devuelve el estado de DESCONOCIDO.
            logger.error(f"Estado desconocido de la base de datos: {e}")
            return HealthStatus.UNKNOWN

    @contextmanager
    # Contextmanager para gestionar la sesión de la base de datos.
    def get_db(self):
        # Inicializa una sesión de base de datos.
        db = self._db()
        try:
            # Cede control al bloque de código que invoca este método con el objeto de sesión.
            yield db
        finally:
            # Asegura que la sesión se cierre después de su uso para evitar conexiones abiertas.
            db.close()
