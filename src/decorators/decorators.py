import time
import logging

#configuración Logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time() # Registramos el tiempo de inicio.
        result = func(*args, **kwargs) # Ejecutamos la funcion decoradora.
        end_time = time.time() # Registramos el tiempo de finalizacion.
        elapsed_time= end_time - start_time # Calculamos el tiempo transcurrido.
        logging.info(f"{func.__name__} ejecutada en {elapsed_time:.4f} seconds")
        return result # Retornamos el resultado de la funcion
    return wrapper # Devolvemos el decorador.


def logit(func):
    def wrapper (*args, **kwargs):
        logging.info(f"Corriendo {func.__name__}") # Registramos el inicio de la ejecucion.
        result= func(*args, **kwargs) # Ejecutamos la funcion decoradora.
        logging.info(f"Completado {func.__name__}") 
        return result # Devolvemos el resultado de la funcion.
    return wrapper
