"""Buscar un elemento
Dada una lista de palabras, solicita al usuario una palabra y muestra si está
o no en la lista."""

palabras = ["manzana", "banana", "pera", "uva", "naranja", "sandía"]

# Solicitar una palabra al usuario
buscar = input("Ingrese una palabra para buscar en la lista: ").lower()

# Verificar si la palabra está en la lista 
if buscar in palabras:
    print(f"La palabra '{buscar}' SÍ está en la lista.")
else:
    print(f"La palabra '{buscar}' NO está en la lista.")