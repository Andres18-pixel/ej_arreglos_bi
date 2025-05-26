# Definición de la matriz de ventas: cada fila representa una tienda y cada columna un mes
ventas = [
    [50000, 60000, 65000, 62000, 78000, 95000],   # Ventas tienda 1 por mes
    [89000, 90000, 98000, 80000, 85000, 90000],   # Ventas tienda 2 por mes
    [65000, 72000, 85000, 72000, 83000, 98000],   # Ventas tienda 3 por mes
    [92000, 88000, 90000, 76000, 82000, 93000]    # Ventas tienda 4 por mes
]

# Calcula el total de ventas sumando todos los elementos de la matriz
total_ventas = sum(sum(fila) for fila in ventas)  # Suma anidada: por fila y luego total

# Calcula las ventas por tienda (suma de cada fila individual)
ventas_por_tienda = [sum(fila) for fila in ventas]  # Lista con el total por cada tienda

# Encuentra la tienda con mayores ventas (índice + 1 porque Python indexa desde 0)
tienda_mas_ventas = ventas_por_tienda.index(max(ventas_por_tienda)) + 1

# Encuentra la tienda con menores ventas (índice + 1 por la misma razón)
tienda_menos_ventas = ventas_por_tienda.index(min(ventas_por_tienda)) + 1

# Resultados impresos en formato claro
print(f"Venta total: {total_ventas}")  # Muestra el total global de ventas
print(f"Ventas por tienda: {ventas_por_tienda}")  # Muestra el array con totales por tienda
print(f"Tienda que más vendió: ABSA {tienda_mas_ventas}")  # Tienda con máximo volumen
print(f"Tienda que menos vendió: ABSA {tienda_menos_ventas}")  # Tienda con mínimo volumen
