# Leer dos valores de punto flotante de doble precisión A y B, correspondiente a dos
# notas de estudiantes. Luego de esto, calcular el promedio de los estudiantes,
# considerando que el peso de la nota A es 3.5 y el peso de la nota B es 7.5.
# Cada nota puede ser de cero a diez, siempre con un dígito después del punto decimal.
# No se olvide de imprimir el final de línea luego del resultado, de lo contrario recibirá
# “Presentation Error”. No se olvide del espacio antes y despues del signo igual.

# Entrada
# El archivo de entrada contiene dos valores de punto flotantes con un dígito después del punto decimal.

# Salida
# Imprimir el mensaje "MEDIA"(Promedio en Portugués) y el promedio de los estudiantes de acuerdo
# con los siguientes ejemplos, con 5 dígitos después del punto decimal y con el espacio en
# blanco antes y después del signo igual.

a = float(input())*3.5; b = float(input())*7.5
media = (a + b) / 11
print(f"MEDIA = {media:.5f}")
