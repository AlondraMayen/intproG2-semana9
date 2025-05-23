"""3. Total de ventas diarias
Una tienda registra sus ventas durante los 7 días de la semana.
En el programa se debe:
• Ingresar los montos de venta diaria.
• Calcular el total y el promedio semanal.
• Mostrar qué día tuvo mayor y menor venta"""

def ventas_semanales():
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    ventas = []

    print("Ingrese los montos de ventas para cada día de la semana:")

    for i in range(7):
        while True:
            try:
                monto = float(input(f"{dias[i]}: $"))
                if monto >= 0:
                    ventas.append(monto)
                    break
                else:
                    print("El monto no puede ser negativo. Intente de nuevo.")
            except ValueError:
                print("Entrada no válida. Ingrese un número válido.")

    total = sum(ventas)
    promedio = total / 7
    mayor_venta = max(ventas)
    menor_venta = min(ventas)
    dia_mayor_venta = dias[ventas.index(mayor_venta)]
    dia_menor_venta = dias[ventas.index(menor_venta)]

    print("\n--- Resumen de Ventas ---")
    print(f"Total semanal: ${total:.2f}")
    print(f"Promedio diario: ${promedio:.2f}")
    print(f"Mayor venta: ${mayor_venta:.2f} el día {dia_mayor_venta}")
    print(f"Menor venta: ${menor_venta:.2f} el día {dia_menor_venta}")

# Ejecutar la función
ventas_semanales()
