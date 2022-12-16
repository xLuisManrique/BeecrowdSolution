# Escribir un programa que lea las coordenadas (X, Y) de un número indeterminado de puntos en el sistema Cartesiano.
# Para cada punto escribir el cuadrante al cual pertenece.
# El programa finaliza cuando al menos una de dos coordenadas es NULL (sin escribir ningún mensaje en esta situación).

# Entrada
# La entrada contiene varios casos de pruebas. Cada caso de prueba contiene dos números enteros.

# Salida
# Para cada caso de prueba, imprimir el cuadrante correspondiente al cual pertenecen las coordenadas,
# en portugues, como en el ejemplo.


while (True):
    try:
        a, b = list(map(int, input().split(' ')))
        if ( a == 0 or b == 0):
            break
        elif ( a > 0 and b > 0):
            print("primeiro")
        elif ( a > 0 and b < 0):
            print("quarto")
        elif ( a < 0 and b < 0):
            print("terceiro")
        elif ( a < 0 and b > 0):
            print("segundo")
    except EOFError:
        break
