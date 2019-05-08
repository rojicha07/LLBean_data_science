edad = 25
print('La persona es: ')

if edad < 18:
    print("menor")
else:
    print("mayor")

pixel = [0.6, 0.3, 0.4]
intensidad = sum(pixel[:])/len(pixel)
print ("La intensidad es :", intensidad)

suma=0
#mediante ciclos
for i in pixel:
    suma+=i
    print("La intensidad es :", suma/len(pixel))

print("La intensidad es :", "{:0.2f}".format(suma/len(pixel)))

#otra forma
print("La intensidad es :", "{:0.2f}".format(sum(pixel)/len(pixel)))

if intensidad > 0.5:
    color = "Blanco"
else:
    color = "Negro"

print("El pixel es de color :", color,"!")
