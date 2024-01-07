# Ejercicio 1: Calculando PI con Monte Carlo
import random
import matplotlib.pyplot as plt
import math

n_puntos = 5000


def dibujar_puntos(puntos):
    """
    Dibuja los puntos en un plano.
    Args:
        puntos: lista de tuplas con las coordenadas x e y de los puntos.
    """
    x = []
    y = []
    for punto in puntos:
        x.append(punto[0])
        y.append(punto[1])
    plt.scatter(x, y)
    plt.show()


def dibujar_aproximaciones_pi(aproximaciones_pi):
    """
    Dibuja las aproximaciones de PI en función del número de puntos generados.
    Args:
        aproximaciones_pi: lista con las aproximaciones de PI.
    """
    plt.plot(aproximaciones_pi)
    plt.axhline(y=math.pi, color='C1', linestyle='--')
    plt.show()
    # Crear una barra horizontal con el valor real de pi


def main():
    # Paso 1: Generar puntos aleatorios y dibujarlos
    n_puntos_circulo = 0
    n_puntos_cuadrado = 0
    r_circulo = 1
    puntos_generados = []
    aproximaciones_pi = []
    for i in range(n_puntos):
        x = random.random() * 2 * r_circulo - r_circulo
        y = random.random() * 2 * r_circulo - r_circulo
        puntos_generados.append((x, y))
        if x**2 + y**2 <= r_circulo**2:
            n_puntos_circulo += 1
            n_puntos_cuadrado += 1
        else:
            n_puntos_cuadrado += 1
        if i % 1 == 0:
            aproximaxion_actual = 4 * n_puntos_circulo / n_puntos_cuadrado
            print(f'Aproximación actual de PI después de {i} iteraciones: ', aproximaxion_actual)
            aproximaciones_pi.append(aproximaxion_actual)
    with open('aproximaciones_pi.txt', 'w') as f:
        for aproximacion in aproximaciones_pi:
            f.write(f'{aproximacion}\n')

    # Paso 2: Calcular PI
    pi = 4 * n_puntos_circulo / n_puntos_cuadrado
    print('Aproximacion final de PI = ', pi)
    # dibujar_puntos(puntos_generados)
    dibujar_aproximaciones_pi(aproximaciones_pi)


if __name__ == '__main__':
    main()