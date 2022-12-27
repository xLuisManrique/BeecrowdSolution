# Leer cuatro números (N1, N2, N3, N4), con 1 dígito después del punto decimal,
# correspondiente a 4 resultados obtenidos por un estudiante.
# Calcular el promedio con pesos 2, 3, 4 e 1 respectivamente,
# para estos 4 resultados e imprimir el mensaje "Media: " (Promedio), segudio por el cálculo obtenido.
# Si el promedio es de 7.0 o más, imprimir el mensaje "Aluno aprovado." (Estudiante Aprobado).
# Si el promedio es menor que 5.0, imprimir el mensaje: "Aluno reprovado." (Estudiante Reprobado).
# Si el promedio es entre 5.0 and 6.9, incluyendo este, el programa deberá imprimir el mensaje "Aluno em exame." (Estudiante en examén).

# En caso de examen, lea una puntuación más. Imprimir el mensaje "Nota do exame: " (Nota de examen) seguido por la puntuación mostrada.
# Vuelva a calcular el promedio (suma la puntuación del examen con el promedio calculado anteriormente y divida por 2)
# e imprima el siguiente mensaje “Aluno aprovado.” (Estudiante Aprobado)
# en caso de que el promedio sea 5.0 o más o "Aluno reprovado." (Estudiante Reprobado) en caso de que el promedio sea 4.9 o menor.
# Para estos 2 casos (Aprobado o reprobado después del examen) imprimir el mensaje "Media final: " (Promedio Final)
# Seguido por el promedio final para este estudiante en la última línea.

# Entrada:
# La entrada contiene cuatro números flotante que representan las calificaciones de los estudiantes.
# Salida:
# Imprimir todas las respuestas con un dígito después del punto decimal.

numeros = input().split()
N1 = float(numeros[0])
N2 = float(numeros[1])
N3 = float(numeros[2])
N4 = float(numeros[3])

P = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1) ) / 10
print(f'Media: {P:.1f}')

if P >= 7.0:
    print("Aluno aprovado.")
elif P < 5.0:
    print("Aluno reprovado")
elif 5.0 <= P < 7.0:
    print("Aluno em exame.")
    N = float(input())
    print(f'Nota do exame: {N:.1f}')
    N = (P + N) / 2
    if N >= 5.0:
        print("Aluno aprovado.")
        print(f'Media final: {N:.1f}')
    else:
        print("Aluno reprovado.")
        print(f'Media final: {N:.1f}')