ventas = [
    [50000, 60000, 65000, 62000, 78000, 95000],
    [89000, 90000, 98000, 80000, 85000, 90000],
    [65000, 72000, 85000, 72000, 83000, 98000],
    [92000, 88000, 90000, 76000, 82000, 93000]
]

total_ventas = sum(sum(fila) for fila in ventas)

ventas_por_tienda = [sum(fila) for fila in ventas]

tienda_mas_ventas = ventas_por_tienda.index(max(ventas_por_tienda)) + 1

tienda_menos_ventas = ventas_por_tienda.index(min(ventas_por_tienda)) + 1

print(f"Venta total: {total_ventas}")
print(f"Ventas por tienda: {ventas_por_tienda}")
print(f"Tienda que más vendió: ABSA {tienda_mas_ventas}")
print(f"Tienda que menos vendió: ABSA {tienda_menos_ventas}")