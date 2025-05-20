"""Encontrar el máximo y el mínimo
A partir de una lista de números reales, encuentra el mayor y el menor
valor."""

numeros = []

cantidad = int(input("¿Cuántos números desea ingresar? "))

for i in range(cantidad):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

maximo = max(numeros)
minimo = min(numeros)

print(f"El valor máximo es: {maximo}")
print(f"El valor mínimo es: {minimo}")
