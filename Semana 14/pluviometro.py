import random

def mostrar_menu():
    op = int(input("1.Determinar promedio anual de lluvias \n2.Determinar el promedio de lluvias para un determinado trimestre\n3.Determinar mes mas seco del año\n4.Determinar los meses del año en los que llovió más que el promedios de lluvia de todo el año.\n"))
    return op

def verificar_opcion(desde,hasta):
    op = mostrar_menu()
    while op < desde or op > hasta:
        print("Eliga un numero entre",desde,"y",hasta,",por favor")
        op = mostrar_menu()
    return op

def cargar_datos():
    temp_mensuales = [] #Creo el arreglo de temperaturas mensuales
    n = 12
    for i in range(n):
        temp = random.randint(15,45)
        temp_mensuales.append(temp)
    return temp_mensuales

def promediar(vector):
    n = len(vector)
    sumatoria = 0
    for elem in vector:
        sumatoria += elem
    if n != 0:
        promedio = round(sumatoria/n,2)
        return promedio

def elegir_trimestre(vector):
    op = int(input("Elige un trimestre (1,2,3,4)"))
    while op < 1 or op > 4:
        op = int(input("Elige un trimestre correcto ENTRE 1 Y 4... (1,2,3,4)"))
    trimestre = vector[((op-1)*3):((op-1)*3)+3]
    return trimestre
def buscar_mayor(vector):
    for i in range(len(vector)):
        if i == 0:
            may = vector[i]
            mes = i
        if vector[i] > may:
            may = vector[i]
            mes = i
    return mes,may
def main(): 
    op = verificar_opcion(1, 4)
    temps_mensuales = cargar_datos()
    print(temps_mensuales)
    if op == 1:
        promedio = promediar(temps_mensuales)
        print("Las temperatura anual promedio fue de: ",promedio,"grados centigrados")
    if op == 2:
        trimestre = elegir_trimestre(temps_mensuales)
        promedio_trimestre = promediar(trimestre)
        print(trimestre)
        print("El promedio del trimestre fue:,",promedio_trimestre)
    if op == 3:
        mas_seco = buscar_mayor(temps_mensuales)
        mes_mas_seco = mas_seco[0]+1
        temp_mas_seca = mas_seco[1]
        print("El mes mas seco fue el",mes_mas_seco,"con una temperatura de: ",temp_mas_seca,"grados centigrados")
    if op == 4:
        pass
main()



