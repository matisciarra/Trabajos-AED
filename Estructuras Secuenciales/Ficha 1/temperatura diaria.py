t1 = float(input("Ingrese la primera temperatura:\n"))
t2 = float(input("Ingrese la segunda temperatura:\n"))
t3 = float(input("Ingrese la tercera temperatura:\n"))

promedio = (t1 + t2 + t3)/2
msg_v = "Existe una temperatura mayor al promedio"
msg_f = "No existe"
x = None
a = None
if t1>promedio or t2>promedio or t3>promedio:
    x = msg_v
    if t1>promedio:
        a = t1
    elif t2>promedio:
        a = t2
    elif t3>promedio:
        a = t3
else:
    x = msg_f
print(x,"y es:",a,"°C")
