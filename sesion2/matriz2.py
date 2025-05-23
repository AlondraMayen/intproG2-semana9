print("Precios")
descuento = float(input("Ingrese el descuento en decimales: (0-1): "))
matriz = [[50, 60, 70, 25], [45, 23, 45, 56], [23, 45, 67, 87]]
matriz_d = []

print("-" * 32)
for fila in matriz:
    for columna in fila:
        print(f"|{columna:>6.2f}", end="|")
    print()
    print("-" * 32)

print("Descuento:")
print("-" * 32)

for fila in matriz:
    new_row = []
    for columna in fila:
        new_row.append(columna * (1 + descuento))
    matriz_d.append(new_row)

for fila in matriz_d:
    for columna in fila:
        print(f"|{columna:>6.2f}", end="|")
    print()
    print("-" * 32)
    
