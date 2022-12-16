# Leer un valor entero, que es la duración en segundos de un evento realizado en una fábrica,
# e informarlo expresado en horas:minutos:segundos.

# Entrada
# El archivo de entrada contiene al entero N.

# Output
# Imprimir el tiempo leído del archivo de entrada (segundos)
# convertido en horas:minutos:segundos como el ejemplo siguiente.


entero = int(input())
hora = int(entero / 3600 )
minutos = int((entero % 3600) / 60)
segundos = entero % 3600 % 60
print(f'{hora:.0f}:{minutos:.0f}:{segundos}')
