"""1. Registro de calificaciones
Un docente desea registrar las calificaciones de sus 10 estudiantes en un examen.
El programa debe:
• Solicitar las calificaciones (sólo se permiten entre 0 a 100).
• Mostrar el promedio, la calificación más alta, la más baja y cuántos aprobaron (>=
70)."""

def registrar_calificaciones():
    calificaciones = []

    print("Ingrese las calificaciones de los 10 estudiantes (de 0 a 100):")
    for i in range(10):
        while True:
            try:
                nota = float(input(f"Calificación del estudiante {i+1}: "))
                if 0 <= nota <= 100:
                    calificaciones.append(nota)
                    break
                else:
                    print("La calificación debe estar entre 0 y 100. Intente de nuevo.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")

    promedio = sum(calificaciones) / len(calificaciones)
    calificacion_mas_alta = max(calificaciones)
    calificacion_mas_baja = min(calificaciones)
    aprobados = sum(1 for nota in calificaciones if nota >= 70)

    print("\n--- Resultados ---")
    print(f"Promedio: {promedio:.2f}")
    print(f"Calificación más alta: {calificacion_mas_alta}")
    print(f"Calificación más baja: {calificacion_mas_baja}")
    print(f"Cantidad de estudiantes que aprobaron: {aprobados}")

registrar_calificaciones()
