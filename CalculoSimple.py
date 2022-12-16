# En este problema, la tarea consiste en leer un código de un producto 1,
# el número de unidades del producto 1,
# el precio de una unidad de producto 1,
# el código de un producto 2,
# el número de unidades del producto 2
# y el precio de una unidad de producto 2.
# Después de esto, calcular y mostrar la cantidad a pagar.

# Entrada
# El archivo de entrada contiene dos líneas de datos.
# En cada línea habrá 3 valores: Dos enteros y un valor flotante con 2 dígitos después del punto decimal.

# Salida
# El archivo de salida debe ser un mensaje como en el siguiente ejemplo.
# Recuerde el espacio antes de ":" y antes del símbolo "R$".
# El valor debe ser presentado con 2 dígitos después del punto.

producto_uno = input().split(' ')
codigo_uno = int(producto_uno[0])
numero_unds = int(producto_uno[1])
precio_und = float(producto_uno[2])
producto_dos = input().split(' ')
codigo_dos = int(producto_dos[0])
num_unds = int(producto_dos[1])
precio_unidad = float(producto_dos[2])
precio_final = (precio_und * numero_unds) + (precio_unidad * num_unds)
print(f'VALOR A PAGAR: R$ {precio_final:.2f}')
