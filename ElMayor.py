# Hacer un programa que lea 3 valores enteros y presente el mas grande seguido del mensaje "eh o maior".
# Usando la siguiente fórmula:
# MaiorAB = (a+b+abs(a-b)) / 2

# Entrada
# El archivo de entrada contiene 3 valores enteros.

# Salida
# Imprimir el mas grande de los 3 valores seguido por un espacio y el mensaje "eh o maior".

valores = input().split(' ')
a = int(valores[0])
b = int(valores[1])
c = int(valores[2])
maiorab = a,b,c
print(max(maiorab), "eh o maior")
