from archivo import cargar_archivo
from alumnos import mostrar_alumno


def cantidad_alumnos() -> None:
    """Muestra por pantalla la cantidad total de alumnos registrados.

    Args:
        Ninguno.

    Returns:
        None
    """

    alumnos = cargar_archivo()
    print(f"Cantidad total de alumnos: {len(alumnos)}")


def promedio_notas() -> None:
    """Calcula y muestra por pantalla el promedio de notas de todos los alumnos.

    Args:
        Ninguno.

    Returns:
        None
    """

    alumnos = cargar_archivo()

    if len(alumnos) == 0:
        print("No hay alumnos registrados.")
        return

    suma = 0
    for alumno in alumnos:
        suma += alumno["nota"]

    promedio = suma / len(alumnos)
    print(f"Promedio de notas: {promedio:.2f}")


def alumno_mayor_nota() -> None:
    """Busca y muestra por pantalla el alumno con la nota más alta.

    Args:
        Ninguno.

    Returns:
        None
    """

    alumnos = cargar_archivo()

    if len(alumnos) == 0:
        print("No hay alumnos registrados.")
        return

    mejor = alumnos[0]
    for alumno in alumnos:
        if alumno["nota"] > mejor["nota"]:
            mejor = alumno

    print("Alumno con mayor nota:")
    mostrar_alumno(mejor)


def cantidad_aprobados() -> None:
    """Calcula y muestra por pantalla la cantidad de alumnos aprobados (nota >= 6).

    Args:
        Ninguno.

    Returns:
        None
    """

    alumnos = cargar_archivo()

    contador = 0
    for alumno in alumnos:
        if alumno["nota"] >= 6:
            contador += 1

    print(f"Cantidad de aprobados: {contador}")


def cantidad_desaprobados() -> None:
    """Calcula y muestra por pantalla la cantidad de alumnos desaprobados (nota < 6).

    Args:
        Ninguno.

    Returns:
        None
    """

    alumnos = cargar_archivo()

    contador = 0
    for alumno in alumnos:
        if alumno["nota"] < 6:
            contador += 1

    print(f"Cantidad de desaprobados: {contador}")