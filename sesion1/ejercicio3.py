"""Promedio de calificaciones
Solicita al usuario 8 calificaciones, guárdalas en una lista y calcula el
promedio."""

calificaciones = []

# Solicitar 8 calificaciones al usuario
for i in range(8):
    calificacion = float(input(f"Ingrese la calificación {i + 1}: "))
    calificaciones.append(calificacion)

promedio = sum(calificaciones) / len(calificaciones)

print(f"El promedio de las calificaciones es: {promedio}")