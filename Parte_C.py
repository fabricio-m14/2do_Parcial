# Fragmento 1

libro = ("9789501234567", "Python", "Guido", 2025)

libro[1] = "Python avanzado"

# El código no va a funcionar ya que libro es una tupla, y estas son inmutables. Luego de crearse NO pueden ser modificadas, reasignarlas o eliminarlas.
# Se produce debido a la inmutabilidad, la característica principal de las tuplas que nos sirve para guardar información que no debe ser modificada.

# Fragmento 2

socios = {"Juan", "Ana", "Pedro", "Ana"}

print(socios)

# La estructura contendrá tres elementos, ya que socios es un conjunto y este NO permite duplicados por lo que Python nos imprime solo la primera vez que se nombra un elemento.
# Nos aporta unicidad por diseño, sin necesidad de escribir más código para que no imprima duplicados.

# Fragmento 3

libros = {
    "9789501234567": {
        "titulo": "Python",
        "autor": "Guido"
    }
}

# La estructura es un diccionario de diccionarios, el diccionario externo usa el ISBN como clave, y el valor asociado es otro diccionario con los datos del libro.
# Cada clave representa un elemento del diccionario correspondiente. El externo es el ISBN, un identificador único como usaremos en el programa de Aprobación directa.
# Las claves del diccionario interno son "titulo", "autor", que representan los datos del libro.
# La ventaja es que tenemos un acceso inmediato a los datos que nos entrega la variable, esto es muy útil en un entorno de biblioteca ya que existen muchísimos libros.

# Un desarrollador afirma:

# "Podría resolver todos los problemas utilizando únicamente listas."

# 1. ¿Está de acuerdo con esta afirmación?

# 2. Justifique su respuesta indicando ventajas y desventajas de esa decisión.

# Parcialmente, no es lo adecuado pero tenemos la ventaja que las listas son sencillas y versátiles. Pero también hay que tener en cuenta que para programa o necesidad
# existe una estructura que tal vez tenga mejores cualidades que la lista en sí. Por ejemplo, para buscar un libro habría que recorrer toda la lista con un bucle
# comparando elemento por elemento, lo cual consume más recursos que un diccionario. No tiene ningún tipo de ventaja por sobre los conjuntos a la hora de lidiar con duplicados,
# por lo que debe utilizar más recursos y lógica para verificarlo. No es inmutable como las tuplas, por lo que son más volátiles. Y es engorroso a la hora de escribirlo por sobre otras
# estructuras en sí. Cada estructura tiene su entorno específico, y pese a ser versátil podemos ver que flaquea en bastantes aspectos que otras no. Por lo que mi respuesta es sí, pero
# utilizada en entornos ideales donde sea la opción más acertada.