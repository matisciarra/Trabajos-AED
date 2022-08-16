horario = int(input("Ingrese el jornal del operario \n1-Diurno \n2-Nocturno \n"))
horas = int(input("Ingrese las horas trabajadas \n"))
msg_error = "Lo siento pero el valor ingresado no corresponde a ninguna opcion solicitada"
x = None
if horario==1 or horario==2:
    if horario == 1:
        x = round(horas*35.50,2)
    elif horario == 2:
        x = round(horas*40.60,2)
    print("El jornal total del operario es igual a",x)
else:
    print(msg_error)


