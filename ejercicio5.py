ventas = [
    [20, 30, 25, 35],
    [40, 22, 33, 28],
    [27, 34, 29, 31]
]

zonas = [sum([ventas[x][y] for x in range(3)]) for y in range(4)]
zona_max = zonas.index(max(zonas)) + 1

vendedor_ventas = [sum(ventas[x]) for x in range(3)]
vendedor_min = vendedor_ventas.index(min(vendedor_ventas)) + 1

total = sum(sum(fila) for fila in ventas)

print(f"Zona con más ventas: {zona_max}")
print(f"Vendedor con menos ventas: {vendedor_min}")
print(f"Total de computadores vendidos: {total}")