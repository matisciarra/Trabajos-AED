def crear_vector():
    n = int(input("Ingrese la cantidad de elementos del vector: \n"))
    vector = []
    for i in range(n):
        num = int(input("Ingrese un numero: "))
        vector.append(num)
    return vector
def buscar_ultimo(vector):
    ult = vector[len(vector)-1]
    return ult
def buscar_primero(vector):
    prim = vector[0]
    return prim
def contar(vector,elemento):
    contador = 0
    for i in range(len(vector)):
        if vector[i] == elemento:
            contador += 1
    return contador
def filtrar_menores_a(elemento,vector):
    new_vec = []
    for i in range(len(vector)):
        if vector[i] < elemento:
            new_vec.append(vector[i])
    return new_vec

numeros = crear_vector()
print(numeros)
ultimo_numero = buscar_ultimo(numeros)
print(ultimo_numero)
cont_ult = contar(numeros,ultimo_numero)
print(cont_ult)
primer_numero = buscar_primero(numeros)
vec_men_prim =  filtrar_menores_a(primer_numero,numeros)
print(vec_men_prim)

