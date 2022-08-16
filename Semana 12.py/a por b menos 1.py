a = 1
b = 2
for i in range(2023):
    c = (a * b) - 1
    a = b
    b = c
print(a,b,c)