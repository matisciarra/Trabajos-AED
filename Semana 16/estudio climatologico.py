import random

def cargar_datos(v,v2,v3):
    n = int(input("Ingrese cantidad de datos de los vectores \n"))
    for i in range(n):
        temp = random.randint(15,47)
        region = random.randint(1,20)
        dia = random.randint(1,365)
        v.append(temp)
        v2.append(region)
        v3.append(dia)

def promediar(vector):
    n = len(vector)
    sumatoria = 0
    for elem in vector:
        sumatoria += elem
    if n != 0:
        promedio = round(sumatoria/n,2)
        return promedio

def sort(regiones,temps,dias):
    n = len(regiones)
    for i in range(n-1):
        for j in range(i+1,n):
            if temps[i] > temps[j]:
                regiones[i],regiones[j] = regiones[j], regiones[i]
                temps[i],temps[j] = temps[j], temps[i]
                dias[i],dias[j] = dias[j], dias[i]

def esta_region(x,regiones):
    while x < 0 or x > 20:
        x = int(input("Error, (solo entre 1 y 20), cual region desea seleccionar? \n"))
    for i in range(len(regiones)):
        if x == regiones[i]:
            return True
    return False

def mostrar_region(x,regiones,temps,dias):
    n = len(regiones)
    for i in range(n-1):
        if x == regiones[i]:
            print("Region: ",regiones[i],"\nTemperatura: ",temps[i],"\ndia: ",dias[i])
            print("*"*60)

def supera(muestra,region,regiones,temps):
    n = len(regiones)
    for i in range(n-1):
        if region == regiones[i] and muestra > temps[i]:
            return True
    return False

def contar_muestras(regiones):
    vec_contador = [0]*20
    for i in range(len(regiones)):
        vec_contador[(regiones[i]-1)] += 1
    return vec_contador

def main():
    temps = []
    regiones = []
    dias = []
    cargar_datos(temps, regiones, dias)
    #print("Temperaturas: ",temps,"\nRegiones: ",regiones,"\nDias: ",dias)
    prom_temps = promediar(temps)
    print("El promedio de temperaturas fue de: ",prom_temps)
    sort(regiones,temps,dias)
    region = int(input("Cual region desea seleccionar? \n"))
    while not esta_region(region, regiones):
        region = int(input("No hemos podido encontrar esa region, seleccione otra: \n"))
    mostrar_region(region, regiones, temps, dias)
    muestra = int(input("Ingrese la muestra que realizo: \n"))
    if supera(muestra,region,regiones,temps):
        print("Hubo una muestra en la region que la supero")
    else:
        print("No hubo muestra que la haya superado")
    contador_muestras = contar_muestras(regiones)
    print(contador_muestras)
    
if __name__ == "__main__":
    main()