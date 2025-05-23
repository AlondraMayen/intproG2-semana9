matriz = [["Jime", "Ana", "Ale"], ["Juan", "Jose", "Fer"], ["Felix", "Andre","Sofi"]]
matriz_contador = [[len(nombre) for nombre in fila] for fila in matriz]

print("Matriz original:")
print("-" * 25)
for fila in matriz:
    for columna in fila:
        print(f"|{columna:>6}", end=" ")
    print("|")
    print("-" * 25)

print("\nMatriz de cantidad de letras:")
print("-" * 25)
for fila in matriz_contador:
    for columna in fila:
        print(f"|{columna:>6}", end=" ")
    print("|")
    print("-" * 25)
