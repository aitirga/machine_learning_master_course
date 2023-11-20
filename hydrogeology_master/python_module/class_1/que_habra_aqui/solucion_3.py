# Ejercicio 2: Calculando el error de la aproximación de PI


# Paso 1: importa las librería matplotlib.pyplot as plt y math
import matplotlib.pyplot as plt
import math

"""
Paso 2: Genera el método main() y llama a la función main() desde el bloque if __name__ == '__main__'
Paso 3: Crea una función main() que haga lo siguiente:
Paso 3.1: Lee el fichero aproximaciones_pi.txt y guarda las aproximaciones de PI en una lista.
Paso 3.2: Crea un método que calcule diferentes tipos de error dada una lista de valores y el valor real.
Paso 3.3: Haz un plot del error en función del número de puntos generados.
"""

def calcular_error_absoluto(valores, valor_real):
    """
    Calcula el error absoluto de una lista de valores respecto a un valor real.
    Args:
        valores: lista de valores.
        valor_real: valor real.

    Returns:
        Lista con los errores absolutos.
    """
    errores = []
    for valor in valores:
        errores.append(abs(valor - valor_real))
    return errores

def calcular_mse(valores, valor_real):
    """
    Calcula el error cuadrático medio de una lista de valores respecto a un valor real.
    Args:
        valores: lista de valores.
        valor_real: valor real.

    Returns:
        Lista con los errores cuadráticos medios.
    """
    errores = []
    for valor in valores:
        errores.append((valor - valor_real)**2)
    return errores

def calcular_error(valores, valor_real, tipo_error='absoluto'):
    """
    Calcula el error de una lista de valores respecto a un valor real.
    Args:
        valores: lista de valores.
        valor_real: valor real.
        tipo_error: tipo de error a calcular.

    Returns:
        Lista con los errores.
    """
    errores = []
    if tipo_error == 'absoluto':
        errores = calcular_error_absoluto(valores, valor_real)
    elif tipo_error == 'mse':
        errores = calcular_mse(valores, valor_real)
    return errores

def main():
    with open('../data/aproximaciones_pi.txt', 'r') as f:
        aproximaciones_pi = f.readlines()
    aproximaciones_pi = [float(aproximacion.strip()) for aproximacion in aproximaciones_pi]
    errores = calcular_error(aproximaciones_pi, math.pi, tipo_error='mse')
    plt.plot(errores)
    plt.semilogy()
    plt.show()

if __name__ == '__main__':
    main()


