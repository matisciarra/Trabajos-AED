def es_vocal(c):
    vocales = "aeiou"
    if c in vocales:
        return True

def es_letra(c):
    if "a" <= c <= "z":
        return True

def es_consonante(c):
    if es_letra(c) and not es_vocal(c):
        return True
        
def es_digito(c):
    digitos = "0123456789"
    if c in digitos:
        return True

def porcentaje(cantidad,total):
    if total != 0:
        porcentaje = round((cantidad*100)/total,2)
        return porcentaje

def promedio(sumatoria,cantidad):
    if cantidad != 0:
        promedio = round(sumatoria/cantidad,2)
        return promedio
    return None

