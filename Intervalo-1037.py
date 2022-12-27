# Debes hacer un programa que lea un número de punto flotante e imprimir un mensaje diciendo en cuál de los siguientes
# intervalos el número pertenece: [0,25] (25,50], (50,75], (75,100). Número es menor que cero o mayor que 100,
# el programa debe imprimir el mensaje "Fora de intervalo" que significa "Fuera de intervalo".

# El símbolo '(' representa mayor que, por ejemplo:
# [0,25] indica números entre 0 y 25.0000, incluyendo ambos.
# (25,50] indicates numbers greater than 25 (25.00001) up to 50.0000000.

# Entrada:
# El archivo de entrada contiene un número de punto flotante.
# Salida:
# La salida debe ser un mensaje como el siguiente ejemplo.


valor = float(input())

if valor < 0 or valor > 100:
    print("Fora de intervalo")
elif 0 <= valor <= 25.0000:
    print("Intervalo [0,25]")
elif 25.00001 <= valor <= 50.0000000:
    print("Intervalo (25,50]")
elif 50.0000001 <= valor <= 75.0000000:
    print("Intervalo (50,75]")
elif 75.0000001 <= valor <= 100.0000000:
    print("Intervalo (75,100]")
