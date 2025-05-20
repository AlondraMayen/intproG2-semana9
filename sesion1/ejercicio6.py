"""Invertir una lista
Pide 10 números al usuario, guárdalos en una lista e imprímelos en orden
inverso."""

numeros = []

# Solicitar 10 números al usuario
for i in range(10):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

# Mostrar la lista en orden inverso
print("Lista en orden inverso:")
for numero in reversed(numeros):
    print(numero)