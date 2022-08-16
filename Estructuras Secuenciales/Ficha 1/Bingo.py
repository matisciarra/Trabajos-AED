import random
lista = []
for i in range(5):
    rand_num = random.randint(1,100)
    lista.append(rand_num)

a = int(input("Numero a:\n"))
b = int(input("Numero b:\n"))
c = int(input("Numero c:\n"))

if a in lista or b in lista or c in lista:
    print("El muchacho tiene suerte")
else:
    print("El muchacho no tiene suerte")

