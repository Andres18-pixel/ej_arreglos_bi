matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

linealizado = []
for col in range(len(matriz[0])):
    for fila in range(len(matriz)):
        linealizado.append(matriz[fila][col])

print("Matriz linealizada por columnas:", linealizado)