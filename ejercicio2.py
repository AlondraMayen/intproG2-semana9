"""2. Encuesta de satisfacción
Un sistema de encuestas almacena las respuestas de 20 personas que valoran un
servicio del 1 al 5.
El programa debe:
• Almacenar las respuestas en una lista.
• Contar cuántas personas eligieron cada puntuación.
• Mostrar el porcentaje de satisfacción (4 y 5)"""
def encuesta_satisfaccion():
    respuestas = []
    conteo_respuestas = [0, 0, 0, 0, 0]  # Índices 0 a 4 para las puntuaciones 1 a 5

    print("Encuesta de satisfacción (20 personas, valoran de 1 a 5):")
    for i in range(20):
        while True:
            try:
                respuesta = int(input(f"Respuesta de la persona {i+1}: "))
                if 1 <= respuesta <= 5:
                    respuestas.append(respuesta)
                    conteo_respuestas[respuesta - 1] += 1
                    break
                else:
                    print("La respuesta debe ser un número entre 1 y 5.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número entero.")

    total_respuestas = len(respuestas)
    satisfechos = conteo_respuestas[3] + conteo_respuestas[4]  # puntuaciones 4 y 5
    porcentaje_satisfaccion = (satisfechos / total_respuestas) * 100

    print("\n--- Resultados de la Encuesta ---")
