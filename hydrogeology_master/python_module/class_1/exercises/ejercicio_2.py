# Ejercicio 2: Calculando el error de la aproximación de PI


# Paso 1: importa las librería matplotlib.pyplot as plt y math

"""
Paso 2: Genera el método main() y llama a la función main() desde el bloque if __name__ == '__main__'
Paso 3: Crea una función main() que haga lo siguiente:
Paso 3.1: Lee el fichero aproximaciones_pi.txt y guarda las aproximaciones de PI en una lista.
Paso 3.2: Crea un método que calcule diferentes tipos de error dada una lista de valores y el valor real.
Paso 3.3: Haz un plot del error en función del número de puntos generados.
"""

with open('nombre_del_archivo.txt', 'r') as archivo:
    lineas = archivo.readlines()
    print(lineas)


import numpy as np

# Crear un array simple
# Aquí estamos creando un array de una dimensión con números del 1 al 5
array_simple = np.array([1, 2, 3, 4, 5])
print("Array Simple:", array_simple)

array_simple.shape