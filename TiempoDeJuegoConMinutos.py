

numeros = input().split(' ')
hora_inicial = int(numeros[0])
minuto_inicial = int(numeros[1])
hora_final = int(numeros[2])
minuto_final = int(numeros[3])
hora = (24 - hora_inicial) + hora_final
minutos = (60 - minuto_inicial) + minuto_final
if hora > 24:
    hora = hora - 24
if minuto_inicial > minuto_final:
    hora = hora - 1
if hora == 24 and minutos > 0 and minuto_inicial != minuto_final:
    hora = 0
if minutos >= minutos - 60:
    minutos = minutos % 60
print(f'O JOGO DUROU {hora} HORA(S) E {minutos} MINUTO(S)')
