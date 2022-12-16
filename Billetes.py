# En este problema tienes que leer un valor entero
# y calcular el menor número posible de billetes en que puede ser descompuesto.
# Los billetes posibles son 100, 50, 20, 10, 5, 2 y 1.
# Imprimir el valor leído y la lista de billetes.

# Entrada
# La entrada contiene un valor entero N (0 < N < 1000000).

# Salida
# Imprimir el número leído y la cantidad mínima necesaria de billetes en lenguaje portugués,
# como muestra el ejemplo. No olvides imprimir el final de línea luego de cada línea,
# de otra forma recibirás “Presentation Error”.

billetes = [100, 50, 20, 10, 5, 2, 1]
cambio = [0, 0, 0, 0, 0, 0, 0]

cantidad = int(input())
print(cantidad)

for i in range(len(billetes)):
    while cantidad >= billetes[i]:
        cantidad -= billetes[i]
        cambio[i] += 1

for i in range(len(billetes)):
    print(cambio[i], 'nota(s) de R$', billetes[i], end=',00\n')



