"""This is the database init Service"""

#importamos módulos requeridos
import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
#sirve para manipular todas las tablas de la base de datos
from sqlalchemy.ext.declarative import declarative_base


def get_db_name():
    return os.environ.get('DB_NAME', '')
# database_url = os.environ.get('DB_NAME', 'sqlite:///')

def get_db_password():
   return os.environ.get('DB-PASS', '') 

def get_db_host():
    return f"{os.environ.get('DB_HOST', '') }:\
        {os.environ.get('DB_PORT', )}"

def get_db_user():
    return os.environ.get('DB_USER', '') 

def database_url():
    return f"postgresql://{get_db_user()}:{get_db_password()}@{get_db_host()}/{get_db_name()}"


#epresenta el motor de la base de datos, 
# con el comando "echo=True" para que al momento de realizar la base de datos,
# muestre por consola lo que esta realizando, que seria el codigo
engine = create_engine(database_url, echo = True)

# Se crea session para conectarse a la base de datos, 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Sirve para manipular todas las tablas de la base de datos
Base = declarative_base()


