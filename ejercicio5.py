# Matriz de ventas: cada fila representa un vendedor y cada columna una zona
ventas = [
    [20, 30, 25, 35],  # Ventas del vendedor 1 por zona
    [40, 22, 33, 28],  # Ventas del vendedor 2 por zona
    [27, 34, 29, 31]   # Ventas del vendedor 3 por zona
]

# Calcula las ventas totales por zona (suma por columnas)
# Usa list comprehension para sumar las ventas de los 3 vendedores (filas) por cada zona (columna)
zonas = [sum([ventas[v][z] for v in range(3)]) for z in range(4)]
# Encuentra la zona con más ventas (índice + 1 porque las zonas empiezan en 1)
zona_max = zonas.index(max(zonas)) + 1

# Calcula las ventas totales por vendedor (suma por filas)
# Usa list comprehension para sumar las ventas de cada vendedor (filas)
vendedor_ventas = [sum(ventas[v]) for v in range(3)]
# Encuentra el vendedor con menos ventas (índice + 1 porque los vendedores empiezan en 1)
vendedor_min = vendedor_ventas.index(min(vendedor_ventas)) + 1

# Calcula el total general de ventas (suma de todas las celdas de la matriz)
total = sum(sum(fila) for fila in ventas)

# Muestra los resultados
print(f"Zona con más ventas: {zona_max}")
print(f"Vendedor con menos ventas: {vendedor_min}")
print(f"Total de computadores vendidos: {total}")
