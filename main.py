"""Punto de entrada del Sistema de Gestión de Alumnos.

Este módulo inicia la ejecución del programa llamando a la función
iniciar_menu(), que despliega el menú interactivo y deriva el control
al resto de los módulos (alumnos, estadisticas, archivo).
"""

from menu import iniciar_menu

iniciar_menu()