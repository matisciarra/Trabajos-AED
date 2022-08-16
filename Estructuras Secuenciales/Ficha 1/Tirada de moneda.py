from random import choice
moneda = [1,2]
apuesta = int(input("A que lado apostas? \n1-Cara \n2-Cruz \n"))
lado = choice(moneda)
if apuesta == 1 or apuesta == 2:
    if apuesta == lado:
        print("Ustes ha ganado")
    else:
        print("Usted ha perdido")
else:
    print("No ha elegido una opcion dada")



