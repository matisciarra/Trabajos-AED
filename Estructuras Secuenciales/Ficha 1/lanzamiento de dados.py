import random

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)

if (dado1 == dado2) or (dado1 + dado2)% 2 != 0:
    print(dado1,dado2,"has ganado")
else:
    print(dado1,dado2,"has perdido, ha ganado la maquina")



