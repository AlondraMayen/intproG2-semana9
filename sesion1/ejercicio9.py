"""Separar pares e impares
Llena una lista con 10 números enteros aleatorios entre 1 y 100, y
sepáralos en dos listas: pares e impares."""

import random

# Generar lista con 10 números aleatorios del 1-100
numeros = [random.randint(1, 100) for _ in range(10)]

pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Números generados:", numeros)
print("Pares:", pares)
print("Impares:", impares)