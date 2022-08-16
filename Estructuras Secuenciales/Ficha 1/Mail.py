nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
dominio = "@frc.utn.edu.ar"

x = None

a = nombre[0]+apellido+dominio
b = nombre+"."+apellido+dominio

if nombre[0] == apellido[0]:
    x = b
else: 
    x = a

print(x)

    


