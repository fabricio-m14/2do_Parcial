# Sistema de Gestión de Alumnos

Sistema de consola en Python para administrar alumnos de una institución educativa, con persistencia de datos en un archivo JSON.

## Funcionalidades

- Cargar alumnos (sin permitir DNI duplicados, edades negativas ni notas fuera del rango 0-10)
- Listar alumnos
- Buscar alumno por DNI
- Modificar datos de un alumno
- Eliminar alumno
- Estadísticas: cantidad total, promedio de notas, alumno con mayor nota, aprobados y desaprobados

## Estructura del proyecto

```
proyecto/
├── main.py           # Punto de entrada del sistema
├── menu.py           # Menú interactivo
├── alumnos.py        # Funciones CRUD de alumnos
├── estadisticas.py   # Cálculo de estadísticas
└── archivo.py        # Lectura y escritura del archivo JSON
```

## Cómo ejecutarlo

```bash
python3 main.py
```

Los datos se guardan automáticamente en `alumnos.json` en la misma carpeta.

## Requisitos

- Python 3