import random

def crear_vector_random():
    n = int(input("Ingrese la cantidad de elementos del vector: \n"))
    vector = []
    for i in range(n):
        num = random.randint(10000,99999)
        vector.append(num)
    return vector

def ordenar(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1,n):
            if v[i] > v[j]:
                v[i],v[j] = v[j],v[i]
                
def busqueda_binaria(x,v):
    izq,der = 0,len(v)-1
    while izq <= der:
        c = (izq + der)//2
        if x == v[c]:
            return c
        if x < v[c]:
            der = c - 1
        else:
            izq = c + 1 
    return -1

legajos = crear_vector_random()
ordenar(legajos)
print(legajos)
x = int(input("Ingrese el legajo que necesita: \n"))
pos_legajo = busqueda_binaria(x, legajos)
if pos_legajo < 0:
    print("Error, no hemos podido encontrar tu elemento")
else:
    print("La posicion del legajo que necesitas es: ", pos_legajo+1)
    

