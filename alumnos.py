from archivo import cargar_archivo, guardar_archivo


def mostrar_alumno(alumno: dict) -> None:
    """Muestra por pantalla los datos de un alumno.


    Args:
        alumno (dict): Diccionario con los datos del alumno.

    Returns:
        None
    """

    print(f"DNI: {alumno['dni']}")
    print(f"Nombre: {alumno['nombre']}")
    print(f"Apellido: {alumno['apellido']}")
    print(f"Edad: {alumno['edad']}")
    print(f"Nota: {alumno['nota']}")


def cargar_alumno() -> None:
    """Registra un nuevo alumno solicitando sus datos por teclado.

    No permite DNI duplicados, edades negativas ni notas fuera
    del rango 0-10.

    Args:
        Ninguno.

    Returns:
        None
    """

    alumnos = cargar_archivo()

    dni = input("Ingrese DNI: ")

    for alumno in alumnos:
        if alumno["dni"] == dni:
            print("Ya existe un alumno con ese DNI.")
            return

    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")

    edad = int(input("Ingrese edad: "))
    if edad < 0:
        print("La edad no puede ser negativa.")
        return

    nota = float(input("Ingrese nota final: "))
    if nota < 0 or nota > 10:
        print("La nota debe estar entre 0 y 10.")
        return

    alumno = {
        "dni": dni,
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "nota": nota
    }

    alumnos.append(alumno)
    guardar_archivo(alumnos)
    print("Alumno registrado correctamente.")


def listar_alumnos() -> None:
    """Muestra por pantalla todos los alumnos registrados.

    Args:
        Ninguno.

    Returns:
        None
    """

    alumnos = cargar_archivo()

    if len(alumnos) == 0:
        print("No hay alumnos registrados.")
        return

    for alumno in alumnos:
        mostrar_alumno(alumno)
        print("---")


def buscar_alumno() -> None:
    """Busca y muestra un alumno a partir del DNI ingresado.

    Args:
        Ninguno.

    Returns:
        None
    """

    alumnos = cargar_archivo()

    dni = input("Ingrese DNI a buscar: ")

    for alumno in alumnos:
        if alumno["dni"] == dni:
            mostrar_alumno(alumno)
            return

    print("No se encontró un alumno con ese DNI.")


def modificar_alumno() -> None:
    """Modifica los datos de un alumno existente a partir del DNI ingresado.

    No permite edades negativas ni notas fuera del rango 0-10.

    Args:
        Ninguno.

    Returns:
        None
    """

    alumnos = cargar_archivo()

    dni = input("Ingrese DNI del alumno a modificar: ")

    for alumno in alumnos:
        if alumno["dni"] == dni:
            alumno["nombre"] = input("Nuevo nombre: ")
            alumno["apellido"] = input("Nuevo apellido: ")

            edad = int(input("Nueva edad: "))
            if edad < 0:
                print("La edad no puede ser negativa.")
                return
            alumno["edad"] = edad

            nota = float(input("Nueva nota: "))
            if nota < 0 or nota > 10:
                print("La nota debe estar entre 0 y 10.")
                return
            alumno["nota"] = nota

            guardar_archivo(alumnos)
            print("Alumno modificado correctamente.")
            return

    print("No se encontró un alumno con ese DNI.")


def eliminar_alumno() -> None:
    """Elimina un alumno a partir del DNI ingresado.

    Args:
        Ninguno.

    Returns:
        None
    """

    alumnos = cargar_archivo()

    dni = input("Ingrese DNI del alumno a eliminar: ")

    for alumno in alumnos:
        if alumno["dni"] == dni:
            alumnos.remove(alumno)
            guardar_archivo(alumnos)
            print("Alumno eliminado correctamente.")
            return

    print("No se encontró un alumno con ese DNI.")