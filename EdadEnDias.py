# Leer un entero,
# que corresponde a la edad de una persona (en días) e imprimirlo en años, meses y días,
# seguido del respectivo mensaje “ano(s)”, “mes(es)”, “dia(s)”.
# Nota: Para facilitar el cálculo,
# considere al año con 365 días y al mes con 30.
# En los casos de prueba nunca habrá una situacion que permita 12 meses y algunos días, como 360, 363 ó 364.
# Este es sólo un ejercicio para plantear un simple razonamiento matemático.

# Entrada
# La entrada consiste en un solo valor entero.

# Salida
# Mostrar el resultado, como se muestra a continuación.


edad_persona = int(input())
edad_anios = int(edad_persona // 365)
edad_persona = edad_persona - (edad_anios * 365)
edad_meses = int(edad_persona // 30)
edad_persona = edad_persona - edad_meses * 30
edad_dias = edad_persona
print(f'{edad_anios} ano(s)\n{edad_meses} mes(es)\n{edad_dias} dia(s)')
