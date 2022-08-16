import random
def crear_vector_random():
    n = int(input("Ingrese la cantidad de elementos del vector: \n"))
    vector = []
    for i in range(n):
        num = random.randint(1,10)
        vector.append(num)
    return vector
def verificar_rango_vectores(vector1,vector2):
    if len(vector1) == len(vector2):
        return True
    return False
def may_comp_hom(vector1,vector2):
    vector_mayor = []
    for i in range(len(vector1)):
        if vector1[i] > vector2[i]:
            vector_mayor.append(vector1[i])
        else:
            vector_mayor.append(vector2[i])
    return vector_mayor

def main():
    vector1 = crear_vector_random()
    vector2 = crear_vector_random()
    verifican = verificar_rango_vectores(vector1, vector2)
    if verifican:
        print(vector1)
        print(vector2)
        vector_mayor = may_comp_hom(vector1, vector2)
        print(vector_mayor)
    else:
        print("Los vectores no poseen mismo rango")
main()