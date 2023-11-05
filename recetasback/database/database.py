"""Conexion de base de datos postgresQL"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/dbname" #reemplazar "user", "password", "localhost", y "dbname" con los valores correctos según tu configuración de base de datos.

engine = create_engine(SQLALCHEMY_DATABASE_URL)#Crear motor de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()