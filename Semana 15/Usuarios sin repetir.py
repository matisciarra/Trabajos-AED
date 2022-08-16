def esta(x,vector):
    for i in range(len(vector)):
        if x == vector[i]:
            return True
    return False
        

def cargar_datos():
    n = int(input("Cuantos usuarios va a ingresar? \n"))
    usuarios = []
    for i in range(n):
        user = input("Ingrese un nombre de usuario: \n")
        while esta(user,usuarios):
            user = input("Lo siento, pero el nombre ya ha sido ingresado, ingrese un nombre de usuario nuevo: \n")
        usuarios.append(user)
    return usuarios

usuarios = cargar_datos()
print(usuarios)
    


