n = int(input("Número de filas (menor a 10): "))
m = int(input("Número de columnas (menor a 10): "))

matriz = []
for i in range(n):
    fila = [int(input(f"M[{i}][{j}]: ")) for j in range(m)]
    matriz.append(fila)

for i in range(n):
    print(f"Suma fila {i}: {sum(matriz[i])}")

for j in range(m):
    suma_col = sum(matriz[i][j] for i in range(n))
    print(f"Promedio columna {j}: {suma_col / n:.2f}")

mayor = matriz[0][0]
pos = (0, 0)
for i in range(n):
    for j in range(m):
        if matriz[i][j] > mayor:
            mayor = matriz[i][j]
            pos = (i, j)
print(f"Mayor valor: {mayor}, posición: fila {pos[0]}, columna {pos[1]}")