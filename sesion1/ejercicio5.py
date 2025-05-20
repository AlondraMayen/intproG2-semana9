"""Contar elementos mayores que un número
Dada una lista de 10 números, contar cuántos son mayores que 50."""

numeros = []

# Solicitar 10 números al usuario
for i in range(10):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

# Contar cuántos números son mayores que 50
mayores_que_50 = 0
for numero in numeros:
    if numero > 50:
        mayores_que_50 += 1

print(f"Hay {mayores_que_50} números mayores que 50.")
