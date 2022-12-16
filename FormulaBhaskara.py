# Leer 3 números de punto flotante.
# Luego, imprimir las raíces de la fórmula de Bhaskara.
# Si es imposible calcular las raíces debido a una división por cero o a la raíz cuadrada de un número negativo,
# presentar el mensaje “Impossivel calcular”.

# Entrada
# Leer 3 números de punto flotante (double) A, B y C.

# Salida
# Mostrar el resultado con 5 dígitos luego del punto decimal o el mensaje si es imposible de calcular.

import math

numeros = input().split(' ')
a = float(numeros[0])
b = float(numeros[1])
c = float(numeros[2])

formula = (b ** 2) - (4.0 * a * c)

if formula < 0 or a == 0:
    print("Impossivel calcular")
else:
    r1 = (-b + math.sqrt(formula)) / (2 * a)
    r2 = (-b - math.sqrt(formula)) / (2 * a)
    print(f'R1 = {r1:.5f}')
    print(f'R2 = {r2:.5f}')
