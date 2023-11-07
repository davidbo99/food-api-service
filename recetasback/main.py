"""Main del proyecto"""

from fastapi import FastAPI
from recetasback.dependencies.containers import Container
from recetasback.routers import endpoints

# Crea una instancia de la aplicación FastAPI.
app = FastAPI()

# Este bloque solo se ejecuta si el script se ejecuta directamente (es decir, no se importa como un módulo).
if __name__ == '__main__':
    
    # Crea una instancia de la clase Container del módulo recetasback.dependencies.containers.
    container = Container()
    
    """Utiliza la inyección de dependencias para conectar cualquier dependencia necesaria para los módulos especificados.
    En este caso, está conectando dependencias para el módulo actual (__name__ se refiere al nombre del módulo actual)"""
    container.wire(modules=[__name__])

    """Recupera la dependencia de base de datos del contenedor. Se espera que la propiedad 'db' proporcione
    acceso a la sesión/conexión de la base de datos."""
    db = container.db()
    
    # Asigna el contenedor al estado de la aplicación para que sea accesible en toda la aplicación.
    app.container = container
    
    """Incluye el enrutador del módulo 'endpoints' del paquete recetasback.adapters.
    Esto añade todas las rutas de endpoints definidas en ese enrutador a la aplicación FastAPI."""
    app.include_router(endpoints.router)
