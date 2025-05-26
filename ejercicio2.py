# Lista vacía para almacenar los datos de los estudiantes
estudiantes = []

# Bucle para ingresar datos de 5 estudiantes
for i in range(5):
    # Solicitar nombre del estudiante (i+1 para mostrar número correcto al usuario)
    nombre = input(f"Nombre del estudiante {i+1}: ")
    
    # Ingresar 3 notas usando list comprehension (j+1 para mostrar número correcto)
    notas = [float(input(f"Nota {j+1}: ")) for j in range(3)]
    
    # Calcular promedio (suma de notas dividido entre 3)
    promedio = sum(notas) / 3
    
    # Agregar tupla con nombre y promedio a la lista estudiantes
    estudiantes.append((nombre, promedio))

# Bucle para mostrar los resultados de todos los estudiantes
for nombre, promedio in estudiantes:
    # Imprimir nombre y promedio con 2 decimales
    print(f"{nombre} - Promedio: {promedio:.2f}")
