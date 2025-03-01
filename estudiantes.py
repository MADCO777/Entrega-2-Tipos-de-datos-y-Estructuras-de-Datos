# Listado ene l cual se guardan a los estudiantes
estudiantes = []

# se agregan a los estudiantes junto a sus notas
estudiantes.append({"nombre": "Ana", "nota": 85})
estudiantes.append({"nombre": "Juan", "nota": 92})
estudiantes.append({"nombre": "María", "nota": 78})

# Creador del promedio de los estudiantes
total = sum(est["nota"] for est in estudiantes)
promedio = total / len(estudiantes)

# El print para moostrarle al usuario lo devuelto
print("Estudiantes:")
for est in estudiantes:
    print(f"Nombre: {est['nombre']}, Nota: {est['nota']}")
print(f"Promedio: {promedio:.2f}")
