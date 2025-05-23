# Matriz nombres
matriz = [["Jime", "Ana", "Sofia"], ["Juan", "Jose", "Fer"]]
print("-"*25)
for fila in matriz:
    for columna in fila:
        print(f"|{columna:>6}", end = " ")
    print("|")
    print("-"*25)