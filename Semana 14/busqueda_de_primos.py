import math
def es_primo(n):
  for i in range(2,int(math.sqrt(n))+1):
    if (n%i) == 0:
      return False
  return True

def crear_vector():
    n = int(input("Ingrese la cantidad de elementos del vector: \n"))
    vector = []
    for i in range(n):
        num = int(input("Ingrese un numero: "))
        vector.append(num)
    return vector

def filtrar_primos(vector):
    primos = []
    for i in range(len(vector)):
        if es_primo(vector[i]):
            primos.append(vector[i])
    return primos

def promediar(vector):
    n = len(vector)
    sumatoria = 0
    for elem in vector:
        sumatoria += elem
    if n != 0:
        promedio = round(sumatoria/n,2)
        return promedio
def main():
    numeros = crear_vector()
    primos = filtrar_primos(numeros)
    print(primos)
    promedio_primos = promediar(primos)
    print(promedio_primos)
main()

            
