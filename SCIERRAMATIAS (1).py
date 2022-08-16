#OK
def es_vocal(c):
    vocales = "aeiouAEIOU"
    if c in vocales:
        return True
#FOR FALSO DEVUELVE NONE, TENGA CUIDADO

#OK
def es_letra(c):
    if "a" <= c <= "z":
        return True
    
#OK
def es_letra_mayuscula(c):
    mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if c in mayusculas:
        return True

#OK
def es_digito(c):
    digitos = "0123456789"
    if c in digitos:
        return True


def main():
#OK
    texto = input("Ingrese un texto: \n")
#OK
    cont_car = cont_pal = may_c = cons = voc = palsinmoa = pen = ult = cont_se = cont_pal_sin_se = cont_s = 0
    cont_pal_emp_dig = cont_e = 0
    tiene_c = tiene_moa = tiene_e = tiene_mayus = emp_dig = False
    band = True
#OK
    for c in texto:
#OK
        if c == " " or c == ".": #Analizar palabra
#OK
            cont_pal += 1
#OK
            if tiene_c and band: #Guardo la cantidad de consonantes de la primera palabra con c
                may_c = cont_car
                band = False
#OK
            if tiene_c and cont_car > may_c: #Comparo y reemplazo
                may_c = cont_car
#OK
            if cons > voc and not tiene_moa: #Comparo si hay mas consonantes que vocales y que no tenga ni m o a
                palsinmoa += 1

#OK
            if cont_se == 1 and cont_s == 1 and cont_e == 1: #Verifico que el se este una sola vez
                cont_pal_sin_se += 1

#OK
            if emp_dig and not tiene_mayus: #Si empiza con digito y no tiene mayusculas cuento la palabra
                cont_pal_emp_dig += 1
                #Reseteo las variables variables
#OK
            cont_car = voc = cons = cont_se = cont_s = cont_e = 0
            tiene_c = tiene_moa = emp_dig = tiene_mayus = False
        else: #Analizar cada letra de la palabra
#OK
            cont_car += 1
#HACER LA ASIGNACION ACA SIGNIFICA QUE ULT VA A SER IGUAL A C, HASTA LA PROXIMA VUELTA
            pen,ult = ult,c #Para saber la letra anterior a la ultima
#OK
            if c == "c": #Verifico si hay una c en la palabra
                tiene_c = True
#OK
            if cont_car == 1 and es_digito(c):
                emp_dig = True #Si empieza con digito

#OK
            if (es_letra(c) or es_letra_mayuscula(c)) and not es_vocal(c):
                cons += 1 #Si es consonante
#OK
            if es_vocal(c):
                voc += 1
#OK
            if es_letra_mayuscula(c):
                tiene_mayus = True

#OK
            if c == "m" or c == "M" or c == "a" or c == "A":
                tiene_moa = True #Si tiene alguna "m" o "a"

#OK
            if (pen == "s" or pen == "S") and (ult == "e" or ult == "E"):
                cont_se += 1 #Contador de se
#OK
            if c == "S" or c == "s":
                cont_s += 1
#OK
            if c == "e" or c == "E":
                cont_e += 1

#OK
    print("Cantidad de palabras que comienzan con un dígito, pero tales que el resto de sus caracteres son letras en minúsculas",cont_pal_emp_dig)
    print("Longitud de la palabra mas larga entre aquellas que tengan (c): ", may_c)
    print("Palabras con mas consonantes que vocales y que no tienen o m o a: ",palsinmoa)
    print("Palabras que contienen (se) solo una vez: ",cont_pal_sin_se)

#OK
if __name__ == "__main__":
    main()

