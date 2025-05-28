
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

# Solicitar al usuario el número de filas y columnas para la matriz (ambas < 10)
n = int(input("Número de filas (menor a 10): "))  # n = número de filas
m = int(input("Número de columnas (menor a 10): "))  # m = número de columnas

# Inicializar una lista vacía para almacenar la matriz
matriz = []

# Construir la matriz fila por fila
for i in range(n):  # Iterar sobre cada fila (de 0 a n-1)
    # Usar list comprehension para ingresar los valores de cada fila
    fila = [int(input(f"M[{i}][{j}]: ")) for j in range(m)]  # j = columnas (0 a m-1)
    matriz.append(fila)  # Añadir la fila completa a la matriz

# Calcular y mostrar la suma de cada fila
for i in range(n):  # Iterar sobre cada fila
    # Sumar todos los elementos de la fila i
    print(f"Suma fila {i}: {sum(matriz[i])}")  # sum() suma los elementos de la lista

# Calcular y mostrar el promedio de cada columna
for j in range(m):  # Iterar sobre cada columna
    # Sumar los elementos de la columna j (accediendo a matriz[i][j] para cada fila i)
    suma_col = sum(matriz[i][j] for i in range(n))
    # Mostrar el promedio con 2 decimales
    print(f"Promedio columna {j}: {suma_col / n:.2f}")  # :.2f = formato con 2 decimales

# Encontrar el valor mayor en la matriz y su posición
mayor = matriz[0][0]  # Inicializar con el primer elemento de la matriz
pos = (0, 0)  # Tupla para almacenar posición (fila, columna)

# Recorrer toda la matriz para buscar el mayor valor
for i in range(n):  # Iterar sobre cada fila
    for j in range(m):  # Iterar sobre cada columna
        if matriz[i][j] > mayor:  # Si encontramos un valor mayor
            mayor = matriz[i][j]  # Actualizar el valor mayor
            pos = (i, j)  # Actualizar la posición

# Mostrar el resultado final
print(f"Mayor valor: {mayor}, posición: fila {pos[0]}, columna {pos[1]}")

