import json
import os

RUTA = "alumnos.json"

def cargar_archivo() -> list:
    """Carga la lista de alumnos almacenada en el archivo JSON.

    Args:
        Ninguno.

    Returns:
        list: Lista de alumnos. Lista vacía si el archivo no existe.
    """

    if os.path.exists(RUTA):
        f = open(RUTA, "r")
        alumnos = json.load(f)
        f.close()
        return alumnos
    return []
 
def guardar_archivo(alumnos: list) -> None:
    """Guarda la lista de alumnos en el archivo JSON.

    Args:
        alumnos (list): Lista de alumnos a guardar.

    Returns:
        None
    """

    f = open(RUTA, "w")
    json.dump(alumnos, f, indent=4)
    f.close()