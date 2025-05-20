array_str = ["uno","dos","tres","cuatro","cinco"]
print("Array de cadenas:", array_str)

# Insertar un elemento al inicio
array_str.insert(3, "cero")
print("Array de cadenas despues de insertar 'cero' al inicio", array_str)

# Contar elementos gay arreglo
cantidad = len(array_str)
print("Cantidad de elementos en el arreglo:", cantidad)

# Eliminar un elemento del arreglo
array_str.remove("tres")
print("Array de cadenas despues de eliminar 'tres': ", array_str)

# Otra forma de eliminar elemento del arreglo
array_str.pop(2)
print("Array de cadenas despues de elinimar el elemento en la posicion 2: ", array_str)