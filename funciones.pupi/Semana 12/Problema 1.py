def es_vocal(c):
    vocales = "aeiou"
    if c in vocales:
        return True


def main():
    texto = input("Ingrese un texto por favor: (con punto se termina) \n")
    cont_caracteres = cont_palabras = cont_b = cont_d= cont_pi = 0
    ult = prim = pen = None
    b = d = empieza_pi = False
    texto = texto.lower()
    for c in texto:
        if c == " " or c == ".": #Aca estoy procesando la palabra
            cont_palabras += 1
            if es_vocal(ult) and cont_caracteres % 2 != 0:
                b = True
            if b:
                cont_b += 1
                b = False
            cont_caracteres = 0
            if prim == ult:
                d = True
            if d:
                cont_d += 1
            if empieza_pi:
                cont_pi += 1
        else: #Aca proceso cada letra
            ult = c
            cont_caracteres += 1
            if cont_caracteres > 2:
                pen = ult
            if cont_caracteres == 1:
                prim = c
            if cont_caracteres == 2 and c == "i" and prim == "p":
                empieza_pi = True
            
    print(cont_pi)
main()
