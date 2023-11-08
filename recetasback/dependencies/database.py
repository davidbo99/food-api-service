"""Módulo de bases de datos"""


from contextlib import contextmanager
from enum import Enum, auto
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class HealthStatus(Enum):
    CONNECTED = auto()     
    DISCONNECTED = auto()  
    UNKNOWN = auto()


class Database:
    # Define una clase para manejar la conexión con la base de datos y métodos para obtener un status de esta"""
    
    def __init__(self, db_url: str) -> None:
        self._engine = create_engine(db_url, echo=True)
        self._db = sessionmaker(autocommit=False, autoflush=False, bind=self._engine)
        
    def get_status(self) -> HealthStatus:
        try:
            with self._engine.connect() as conn:
                return HealthStatus.CONNECTED
        except SQLAlchemyError as e:
            logger.error(f"Error al conectar a la base de datos: {e}")
            return HealthStatus.DISCONNECTED
        except Exception as e:
            logger.error(f"Estado desconocido de la base de datos: {e}")
            return HealthStatus.UNKNOWN

    @contextmanager
    def get_db(self):
        db = self._db()
        try:
            yield db
        finally:
            db.close()
