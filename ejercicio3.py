# Matriz de ejemplo 3x3 (3 filas x 3 columnas)
matriz = [
    [1, 2, 3],  # Primera fila
    [4, 5, 6],  # Segunda fila
    [7, 8, 9]   # Tercera fila
]

# Lista vacía para almacenar la matriz linealizada por columnas
linealizado = []

# Recorrer cada columna de la matriz (índices 0, 1, 2)
for col in range(len(matriz[0])):
    # Recorrer cada fila de la matriz (índices 0, 1, 2)
    for fila in range(len(matriz)):
        # Agregar elemento actual (fila, columna) a la lista linealizada
        linealizado.append(matriz[fila][col])

# Mostrar resultado final
print("Matriz linealizada por columnas:", linealizado)
