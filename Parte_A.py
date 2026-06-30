# Situación 1 

# Representar la ubicación de los libros en estanterías organizadas en filas y columnas.

# Estructura: Matriz

estanteria = [
    ["Libro A", "Libro B", "Libro C"],
    ["Libro D", "Libro E", "Libro F"],
    ["Libro G", "Libro H", "Libro I"]
]

print(estanteria[1][2])

# # Una matriz muestra de forma natural una organización en filas y columnas, donde cada lugar [fila][columna] se refiere a un estante real. 
# # Es la única estructura que representa directamente esa organización en dos dimensiones — una lista sencilla no es suficiente porque solo tiene una dimensión.



# Situación 2 

# Guardar información fija de un libro que no debería modificarse accidentalmente. 

# Estructura: Tupla

libro = ("978-3-16-148410-0", "Cien años de soledad", "Gabriel García Márquez", 1967)

# # Las tuplas no se pueden cambiar — una vez que se crean, sus elementos permanecen igual. 
# # Esto asegura que información como el ISBN, el título, el autor y el año en que se publicó no se cambie por error mientras el programa está en marcha. 
# # Una lista permitiría modificaciones no deseadas.



# Situación 3 

# Evitar que un mismo socio aparezca registrado varias veces.

# Estructura: Conjunto (set)}

socios = {"12345678", "87654321", "11223344"}
socios.add("12345678")

# # Los conjuntos no permiten elementos duplicados por definición. 
# # Si se intenta agregar un socio que ya existe, el conjunto lo ignora automáticamente, sin necesidad de verificar manualmente. 
# # Una lista requeriría una búsqueda previa para detectar el duplicado.



# Situación 4 

# Relacionar un ISBN con toda la información de un libro. 

#Estructura: Diccionario

catalogo = {
    "978-3-16-148410-0": {
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "año": 1967
    }
}

print(catalogo["978-3-16-148410-0"]["autor"])  # nos da "Gabriel García Márquez"


# El diccionario permite relacionar una clave única (el ISBN) con todos los datos asociados al libro. 
# El acceso es directo — no hace falta recorrer toda la estructura para encontrar un libro, simplemente se usa su ISBN como clave.




# Situación 5

# Conservar la información del sistema luego de cerrar el programa.

# Estructura: Archivo (JSON)

import json

# Guardar
f = open("socios.json", "w")
json.dump(socios, f)
f.close()

# Cargar
f = open("socios.json", "r")
socios = json.load(f)
f.close()

# Los datos en memoria se pierden al cerrar el programa. 
# Un archivo JSON permite persistir la información en el disco y recuperarla en la próxima ejecución.
# Es la única alternativa que garantiza que los datos sobrevivan al cierre del sistema.