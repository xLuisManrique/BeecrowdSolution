





billetes = [100, 50, 20, 10, 5, 2]
monedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
cambio = [0, 0, 0, 0, 0, 0]
cantidad = float(input())
print('NOTAS:')
for i in range(len(billetes)):
    while cantidad >= billetes[i]:
        cantidad -= billetes[i]
        cambio[i] += 1
for i in range(len(billetes)):
    print(cambio[i], 'nota(s) de R$', billetes[i], end='.00\n')
print('MOEDAS:')
for i in monedas:
    resultado = int(round(cantidad, 2) / i)
    print(f'{resultado} moeda(s) de R$ {i:.2f}')
    cantidad -= resultado * i
