# Leer los cuatro valores correspondientes a las coordenadas x e y de dos puntos en el plano,
# p1 (x1, y1) y p2 (x2, y2) y calcular la distancia entre ellos,
# mostrando cuatro decimales después del punto, de acuerdo a la fórmula:
# Distancia = √ (x2 - x1) ** 2 + (y2 - y1) **2

# Entrada
# La entrada contiene dos líneas de datos,
# la primera contiene dos valores double: x1 y1,
# la segunda también contiene dos valores double con un dígito después del punto: x2 y2.

# Salida
# Calcular y mostrar el valor de la distancia usando la fórmula provista, con 4 dígitos después del punto.

import math

valores_p1 = input().split(' ')
x1 = float(valores_p1[0])
y1 = float(valores_p1[1])
valores_p2 = input().split(' ')
x2 = float(valores_p2[0])
y2 = float(valores_p2[1])
distancia = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
print(f'{distancia:.4f}')




