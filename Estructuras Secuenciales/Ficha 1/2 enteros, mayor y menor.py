#Entradas
a = int(input("Numero a: "))
b = int(input("Numero b: "))
may = None
men = None
#Procesp
if a > b:
    may = a
    men = b
else:
    may = b
    men = a
#Resultado
print(men,may)
