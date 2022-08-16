ancho = int(input("Ingrese el ancho: "))
largo = int(input("Ingrese el largo: "))
cuadrado = ancho == largo
superficie = str(ancho * largo)
if cuadrado == True:
    print("Es un cuadrado y su superficie es de"+superficie+"metros cuadrados")
else:
    print("Es un rectangulo y la superficie es de "+superficie+" metros cuadrados")



