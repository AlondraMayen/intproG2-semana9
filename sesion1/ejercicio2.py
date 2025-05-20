"""Sumar los elementos de una lista
Solicita 10 números al usuario, guárdalos en una lista y muestra la suma
total."""

numeros = []

# Solicitar 10 números al usuario
for i in range(10):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

suma_total = sum(numeros)

print(f"La suma total de los números ingresados es: {suma_total}")