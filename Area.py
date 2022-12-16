# Escriba un programa que lea tres valores de punto flotante: A, B y C.
# Luego, calcular y mostrar:
# a) El área del triángulo rectángulo de base A y altura C.
# b) El área del círculo de radio C (Pi = 3.14159).
# c) El área del trapecio el cual tiene A y B como bases, y C como altura.
# d) El área del cuadrado de lado B.
# e) El área del rectángulo de lados A y B.

# Entrada
# La entrada contiene tres valores de doble precisión con un dígito luego del punto decimal.

# Salida
# La salida contiene 5 renglones. Cada uno de los renglones corresponde a las áreas descriptas anteriormente,
# siempre con el mensaje correspondiente (en portugués) y un espacio entre los dos puntos y el valor.
# El valor calculado debe ser presentado con 3 dígitos luego del punto decimal.

valores = input().split(' ')
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

triangulo = (a * c) / 2
circulo = 3.14159 * (c ** 2)
trapecio = ((a + b) * c) / 2
cuadrado = b * b
rectangulo = a * b
print(f'TRIANGULO: {triangulo:.3f}\nCIRCULO: {circulo:.3f}\nTRAPEZIO: {trapecio:.3f}\nQUADRADO: {cuadrado:.3f}\n'
      f'RETANGULO: {rectangulo:.3f}')

