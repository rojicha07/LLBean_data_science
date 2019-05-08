lista = [44,11,15,29,53,12,30]
t = 0
max = 0
for i in lista:
    if t > i:
        max = t
    t = i
print("El numero mayor de la lista es:",max)

## otra forma

for i in lista:
    if i > max:
        max = i
print("El numero mayor de la lista es:",max)

