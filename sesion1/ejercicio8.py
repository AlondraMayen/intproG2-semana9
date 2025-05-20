"""Eliminar duplicados
Dada una lista con valores repetidos, crea una nueva lista sin duplicados."""

lista = [1, 2, 2, 3, 4, 4, 5, 1, 6]
sin_duplicados = []

# Recorrer la lista original
for elemento in lista:
    if elemento not in sin_duplicados:
        sin_duplicados.append(elemento)

print("Lista sin duplicados:", sin_duplicados)