a,b,c = int(input("Digame un numero: ")), int(input("Digame un numero: ")), int(input("Digame un numero: "))
x = None

caso_1 = (a+b+c)/2
caso_2 = (a+b+c)**3

if a + b + c > 10:
    x = caso_1
else:
    x = caso_2

print(x)