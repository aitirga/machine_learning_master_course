# Ejercicio 1

# Crea una función main() que imprima por pantalla "Hello World!".

# Llama a la función main() desde el bloque if __name__ == '__main__'.



def multiplicate_por_cero(numero, multiplicador=0.0):
    """
    Multiplica un número por cero.
    Args:
        numero: número a multiplicar.
        multiplicador: valor por el que se multiplica el número.

    Returns:
        El valor de la multiplicación.
    """
    valor = numero * multiplicador
    return valor

nota = 5

# if nota >= 5:
#     print('Aprobado')
# else:
#     print('Suspenso')
#
#
# if nota > 5:
#     print('Aprobado')
# elif nota == 5:
#     print('Aprobado por los pelos')
# else:
#     print('Suspenso')


nota = 5.05
eps = 0.1
if nota >= 5 + eps:
    print('Aprobado')
elif nota >= 5 and nota < 5 + eps:
    print('Aprobado por los pelos')
else:
    print('Suspenso')

for i in range(10):
    print(i)

notas = {'Juan': 5, 'Pedro': 6, 'Ana': 7}
for alumno in notas:
    print(alumno, notas[alumno])


nota = 3.5
while nota < 5:
    nota += 0.01
print(nota)

alumnos = ['Juan', 'Pedro', 'Ana']
notas = [5, 6, 7]

notas_alumnos = {alumnos[i]: notas[i] for i in range(len(alumnos))}


