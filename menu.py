from alumnos import cargar_alumno, listar_alumnos, buscar_alumno, modificar_alumno, eliminar_alumno
from estadisticas import cantidad_alumnos, promedio_notas, alumno_mayor_nota, cantidad_aprobados, cantidad_desaprobados


def mostrar_menu() -> None:
    """Muestra por pantalla las opciones del menú principal.

    Args:
        Ninguno.

    Returns:
        None
    """

    print("\n--- Sistema de Gestión de Alumnos ---")
    print("1. Cargar alumno")
    print("2. Listar alumnos")
    print("3. Buscar alumno")
    print("4. Modificar alumno")
    print("5. Eliminar alumno")
    print("6. Cantidad total de alumnos")
    print("7. Promedio de notas")
    print("8. Alumno con mayor nota")
    print("9. Cantidad de aprobados")
    print("10. Cantidad de desaprobados")
    print("0. Salir")


def iniciar_menu() -> None:
    """Ejecuta el bucle principal del menú, leyendo la opción del usuario y derivando la
    ejecución a la función correspondiente hasta que se seleccione la opción de salir.

    Args:
        Ninguno.

    Returns:
        None
    """

    opcion = 99

    while opcion != 0:
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            cargar_alumno()
        elif opcion == 2:
            listar_alumnos()
        elif opcion == 3:
            buscar_alumno()
        elif opcion == 4:
            modificar_alumno()
        elif opcion == 5:
            eliminar_alumno()
        elif opcion == 6:
            cantidad_alumnos()
        elif opcion == 7:
            promedio_notas()
        elif opcion == 8:
            alumno_mayor_nota()
        elif opcion == 9:
            cantidad_aprobados()
        elif opcion == 10:
            cantidad_desaprobados()
        elif opcion == 0:
            print("Saliendo del sistema...")
        else:
            print("Opción inválida.")