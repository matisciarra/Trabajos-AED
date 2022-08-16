import random
def crear_vector_random():
    n = 7
    vector = []
    for i in range(n):
        num = random.randint(-1,10)
        vector.append(num)
    return vector

def ordenar(vec):
    n = len(vec)
    for i in range(n-1):
        for j in range(i+1,n):
            if vec[i] > vec[j]:
                vec[i],vec[j] = vec[j],vec[i]

def tomar_3_primeros(v):
    n = len(v)
    vec = v[n-3:n]
    return vec

def mayores_a(x,v):
    mayores = []
    for i in range(len(v)):
        if v[i] > x:
            mayores.append(v[i])
    return mayores

def diferencia_entre_mayor_y_menor(v):
    n = len(v)
    dif = v[n-1] - v[0]
    return dif

def sumar(vector):
    sumatoria = 0
    for elem in vector:
        sumatoria += elem
    return sumatoria

def main():
    puntajes = crear_vector_random()
    ordenar(puntajes)
    print(puntajes)
    tres_primeros = tomar_3_primeros(puntajes)
    print(tres_primeros)
    x = int(input("Ingrese un puntaje: \n"))
    mayores_a_x = mayores_a(x,puntajes)
    print("Los valores mayores a",x,":",mayores_a_x)
    diferencia = diferencia_entre_mayor_y_menor(puntajes)
    print("La diferencia entre el menor y mayor puntaje es de: ",diferencia)
    puntaje_total = sumar(puntajes)
    if puntaje_total < 20:
        print("Quedan descalificados, el puntaje total fue de: ",puntaje_total)
    else:
        print("Calificaron, tienen mas de 20")
main()
