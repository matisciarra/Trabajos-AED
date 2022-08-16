import random
def crear_vector_random():
    n = int(input("Ingrese la cantidad de elementos del vector: \n"))
    vector = []
    for i in range(n):
        num = random.randint(1,100)
        vector.append(num)
    return vector

def ordenar_ascendente(vec):
    n = len(vec)
    for i in range(n-1):
        for j in range(i+1,n):
            if vec[i] > vec[j]:
                vec[i],vec[j] = vec[j],vec[i]

def busqueda_binaria(vector,x):
    n = len(vector)
    izq,der = 0,n-1
    while izq <= der:
        c = (izq + der)//2
        if x == vector[c]:
            return True
        if x < vector[c]:
            der = c - 1
        else:
            izq = c + 1
    return False

def contar(x,vector):
    contador = 0
    for i in range(len(vector)):
        if vector[i] > x and vector[i] % 2 != 0:
            contador += 1
    return contador
    
vector = crear_vector_random()
ordenar_ascendente(vector)
print(vector)
x = int(input("Que elemento desea buscar? \n"))
esta_x = busqueda_binaria(vector, x)
if esta_x:
    contador = contar(x, vector)
    print("Contador impares y mayores a",x,":",contador)
else:
    print("No hemos podido encontrar tu elemento")






