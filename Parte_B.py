# 1. Explique por qué utilizar múltiples listas separadas para almacenar datos relacionados puede generar errores de consistencia. 

# Supongamos que guardamos los datos de socios en dos listas separadas:
nombres = ["Juan", "Carlos", "José"]
apellidos = ["Perez", "Gutierrez", "Messi"]

#  El problema lo tenemos si se elimina "Carlos" de la lista nombres, este está asignado a el índice 1 (es decir, nombres[1]), y se relaciona
#  con el mismo índice de la lista apellidos "Gutierrez"(apellidos[1]). Al eliminarlo lo que va a suceder es que apellidos[1] pertenecerá a
#  "José", ya que pasará a ocupar esa posición en la lista. Lo que corresponde hacer es borrar la variable de la lista con nombres.remove("Carlos").

# 2. Explique qué ventajas aporta utilizar una estructura basada en clave-valor para buscar información. 

# El acceso por clave es directo, no hace falta recorrer toda la estructura para encontrar un elemento. Comparando los dos enfoques:

# Con lista: hay que recorrer hasta encontrar el ISBN

for libro in libros:
    if libro["isbn"] == "978-3-16-148410-0":
        print(libro)

# Con diccionario: acceso inmediato

print(catalogo["978-3-16-148410-0"])

# 3. Explique por qué una estructura que no permite duplicados puede ser útil en sistemas reales.

# En sistemas reales, los duplicados generan inconsistencias y errores difíciles de detectar. En el caso de la biblioteca, si un mismo socio aparece
# dos veces, ocurrirá que:
#  - Se le envíen notificaciones duplicadas.

#  - Se registren dos préstamos distintos para la misma persona pero en registros diferentes.

#  - Al buscar su historial, los resultados aparezcan divididos entre los dos registros.

# Usando un conjunto, estos problemas se evitan automáticamente, sin necesidad de escribir código adicional para detectar y rechazar duplicados.

# 4. Explique las diferencias entre almacenar datos: únicamente en memoria; en archivos. ¿En qué situaciones utilizaría cada alternativa? 


# Almacenar los datos en memoria hace que el acceso sea más rápido pero que no tenga persistencia, es decir, no tenemos la trazabilidad de guardarlo en archivos de guardado(JSON).
# Tiene una capacidad menor ya que la limita la memoria RAM, en el caso de los archivos tiene la capacidad del disco del sistema. Se almacenan en memoria aquellos datos temporales
# de uso típico durante la ejecución de un programa, para que persistan estos datos(como vamos a ver en el programa de aprobación directa) es necesario guardarlos en archivos.

# En el sistema de la biblioteca, lo ideal es combinar ambas: 
# cargar los datos del archivo al iniciar, trabajar en memoria mientras el programa está activo, y guardar en el archivo al cerrar o cada vez que se realiza un cambio importante.