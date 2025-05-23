estudiantes = []

for i in range(5):
    nombre = input(f"Nombre del estudiante {i+1}: ")
    notas = [float(input(f"Nota {j+1}: ")) for j in range(3)]
    promedio = sum(notas) / 3
    estudiantes.append((nombre, promedio))

for nombre, promedio in estudiantes:
    print(f"{nombre} - Promedio: {promedio:.2f}")