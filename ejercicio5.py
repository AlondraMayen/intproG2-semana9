"""5. Análisis de números aleatorios
Se desea analizar una muestra de 30 números aleatorios entre 1 y 100.
En el programa se debe:
• Generar los números y almacenarlos.
• Separar los pares e impares en listas distintas.
• Mostrar la suma total de cada grupo y cuántos elementos contiene cada uno."""

import random

def analisis_numeros():
    nums = [random.randint(1, 100) for _ in range(30)]
    pares = []
    impares = []

    for n in nums:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)

    suma_par = sum(pares)
    suma_imp = sum(impares)
    cant_par = len(pares)
    cant_imp = len(impares)

    print("--- Análisis ---")
    print(f"Números: {nums}")
    print(f"\nPares ({cant_par}): {pares}")
    print(f"Suma de pares: {suma_par}")
    print(f"\nImpares ({cant_imp}): {impares}")
    print(f"Suma de impares: {suma_imp}")

analisis_numeros()
