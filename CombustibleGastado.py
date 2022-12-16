# Juancito quiere calcular y mostrar la cantidad de litros de combustible gastado en un viaje,
# con un auto que hace 12 Km/L.
# Para eso, le gustaría que lo ayudes a través de un programa sencillo.
# Para realizar el cálculo, tienes que leer el tiempo (en horas)
# y la velocidad media (en Km/h) del viaje.
# De esta forma se puede obtener la distancia,
# y luego, calcular la cantidad de litros necesarios.
# Mostrar el valor con tres dígitos luego del punto decimal.

# Entrada
# La entrada contiene dos enteros.
# El primero es el tiempo que duró el viaje (en horas).
# El segundo es la velocidad media del viaje (en Km/h).

# Salida
# Imprimir cuantos litros de combustible fueron necesarios para hacer el viaje,
# con tres dígitos luegos del punto decimal.

auto = 12
tiempo_horas = int(input()); velocidad_viaje = int(input())
litros_gastado = (tiempo_horas * velocidad_viaje ) / 12
print(f'{litros_gastado:.3f}')
