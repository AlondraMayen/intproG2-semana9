import os
import random
import time

participantes = list()
while True:
    os.system("cls||clear")
    os.system("color a1")
    nombre = input("Ingrese el nombre del participante (o 'fin' para terminar): ")
    if nombre.lower()== 'fin':
        break
    participantes.append(nombre.upper())
    
os.system("cls||clear")
print("Participantes agregados...")
print(participantes)
x = input("Presiona una tecla...")
cont = 10
while cont > 0:
    os.system("cls||clear")
    print(cont)
    time.sleep(1)
    cont -= 1
    
fin = len(participantes) -1
ganador = random.randint(0, fin)
print(f"Ganador: {participantes[ganador]}")