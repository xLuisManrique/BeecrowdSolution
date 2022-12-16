# Leer 4 valores enteros A, B, C y D.
# Luego, si B es mayor que C,
# D es mayor que A,
# la suma de C y D es mayor que la suma de A y B,
# C y D son valores positivos y A es par,
# escribir el mensaje “Valores aceitos” (Valores aceptados).
# De lo contrario, escriba el mensaje “Valores nao aceitos” (Valores no aceptados).

# Entrada
# Cuatro números enteros A, B, C y D.

# Salida
# Mostrar el mensaje correspondiente luego de la validación de los números.

variables = input().split(' ')
a = int(variables[0])
b = int(variables[1])
c = int(variables[2])
d = int(variables[3])
suma_uno = c + d
suma_dos = a + b
if ( b > c and d > a) and suma_uno > suma_dos and (c > 0 and d > 0) and a % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")

