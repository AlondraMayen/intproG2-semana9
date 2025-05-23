"""4. Registro de sueldos
Se registra el sueldo de 12 empleados.
El programa debe:
• Almacenar los sueldos.
• Calcular cuántos ganan más de $1,000.
• Hallar el sueldo promedio.
• Identificar si algún sueldo es exactamente $0 (posible error de captura)."""

def registro_sueldos():
    sueldos = []

    print("Ingrese el sueldo de los 12 empleados:")

    for i in range(12):
        while True:
            try:
                sueldo = float(input(f"Sueldo del empleado {i+1}: $"))
                if sueldo >= 0:
                    sueldos.append(sueldo)
                    break
                else:
                    print("El sueldo no puede ser negativo. Intente de nuevo.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")

    cantidad_mas_de_1000 = sum(1 for s in sueldos if s > 1000)
    promedio = sum(sueldos) / len(sueldos)
    sueldos_con_cero = any(s == 0 for s in sueldos)

    print("\n--- Informe de Sueldos ---")
    print(f"Cantidad de empleados que ganan más de $1,000: {cantidad_mas_de_1000}")
    print(f"Sueldo promedio: ${promedio:.2f}")
    if sueldos_con_cero:
        print("Hay al menos un sueldo registrado como $0 (posible error de captura).")
    else:
        print("No se detectaron sueldos en $0.")

# Ejecutar la función
registro_sueldos()
