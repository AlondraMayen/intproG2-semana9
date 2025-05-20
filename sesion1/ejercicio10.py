"""Sumar elementos en posiciones pares
Suma los elementos que se encuentran en posiciones pares de la lista."""

lista = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]

suma_pares = 0
for i in range(0, len(lista), 2): 
    suma_pares += lista[i]

print(f"La suma de los elementos en posiciones pares es: {suma_pares}")
