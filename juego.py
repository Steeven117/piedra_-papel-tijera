# INPUT

print("--------------------------------")
print("-----PIEDRA, PAPEL O TIJERA-----")
print("--------------------------------")

import random

# processing

while True:
    aleatorio = random.randrange(0,3)
    PC = ""
    print("1. piedra: ")
    print("2. papel: ")
    print("3. tijera: ")
    opcion = int(input("Elige una opcion: "))

    if opcion == 1:
        rta = "PIEDRA"
    elif opcion == 2:
        rta = "PAPEL"
    elif opcion== 3:
        rta = "TIJERA"
    print("ESCOGISTE: ", rta)

    if aleatorio == 0:
        PC = "PIEDRA"
    elif aleatorio == 1:
        PC = "PAPEL"
    elif aleatorio == 2:
        PC = "TIJERA"
    print("PC elijio: ", PC)
    
    if PC == "piedra" and rta == "papel":
        print("GANASTE PAPEL ENVUELVE A PIEDRA")
    elif PC == "papel" and rta == "Tijera":
        print("GANASTE TIJERA CORTA PAPEL")
    elif PC == "tijera" and rta == "piedra":
        print("GANASTE PIEDRA APLASTA TIJERA")
    if PC == "papel" and rta == "piedra":
        print("PERDISTE PAPEL ENVUELVE PIEDRA")
    elif PC == "tijera" and rta == "papel":
        print("PERDISTE TIJERA CORTA PAPEL")
    elif PC == "piedra" and rta == "tijera":
        print("PERDISTE PIEDRA APLASTA TIJERA")
    elif PC == rta:
        print("EMPATE")

