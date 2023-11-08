"""Módulo de contenedores"""


from dependency_injector import containers, providers
from .database import Database
import os


class Container(containers.DeclarativeContainer):
    """Define la clase Container contendrá los contenedores de la aplicación."""

    db = providers.Singleton(Database, db_url=os.environ.get("DATABASE_URL", None))
