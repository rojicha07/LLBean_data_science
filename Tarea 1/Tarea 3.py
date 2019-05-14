#PRIMERA PARTE
print("**PRIMERA PARTE**:")

agenda_hospital = []
persona = ('Juan', 'Mora', 100103111,65 , 81118811, 'dolor')
agenda_hospital.append(persona)
persona = ('Ana', 'Jimenez', 32415116,50 , 46261266, 'consulta')
# agregamos otra persona
agenda_hospital.append(persona)
persona =[('Sofia',   'Alfaro',   32415116,   36 , 51161161, 'consulta'),
          ('Carlos',  'Sanchez',  33411151,   15 , 41655161, 'dolor'),
          ('Felipe',  'Perez',    12243151,   42 , 65151111, 'documento'),
          ('Melissa', 'Alvarado', 734114144,  10 , 87421312, 'dolor'),
          ('Pedro',   'Castro',   4372124141, 2 ,  99313131, 'dolor'),]
agenda_hospital.extend(persona)
for paciente in agenda_hospital:
    print(paciente)

#Primera pregunta:

print("Pregunta 1: Llegaron",len(agenda_hospital),"pacientes")

#Segunda pregunta:
res=0
for paciente in agenda_hospital:
    if (paciente[5]) == 'dolor':
        res = res + 1
print("Pregunta 2:",res,"pacientes llegaron por dolor")

#Tercera pregunta:
print("Tercera pregunta:")
agenda_mayor_menor = sorted(agenda_hospital, key=lambda x: x[3], reverse = True)
for paciente in agenda_mayor_menor:
    print(paciente)

#Cuarta pregunta:

res2=0
res3=0
for paciente in agenda_hospital:
    if (paciente[3]) >= 18:
        res2 = res2 + 1
    else:
        res3 = res3 + 1
print("Cuarta pregunta:",res2,"pacientes son mayor de edad; ",res3, "pacientes son menor de edad")

#Quinta pregunta:
print("Quinta pregunta:")
agenda_sorted = sorted(agenda_hospital, key=lambda x: (x[5]=='dolor', x[3]), reverse = True)
for paciente in agenda_sorted:
    print(paciente)

#Sexta pregunta:
print("Sexta pregunta:")
restart = True
while restart:
    for paciente in agenda_sorted:
        if paciente[5] == 'dolor':
            agenda_sorted.remove(paciente)
            restart = True
            break
        restart = False

agenda_sorted2 = sorted(agenda_sorted, key=lambda x: x[3],)
for paciente in agenda_sorted2:
    print(paciente)

#SEGUNDA PARTE
print("**SEGUNDA PARTE**:")

#3.1
print("3.1:")
input_number = input("Cuantos valores quiere en la lista?")
lista=[]
for i in range(0,int(input_number)):
    input_value = input("Por favor ingrese el valor # {} ".format(i+1))
    lista.append(input_value)
print("La lista creada es:",lista)


#3.2
print("3.2:")
input_number = input("Cuantas palabras tiene la lista?")
lista=[]
for i in range(0,int(input_number)):
    input_value = input("Por favor ingrese la palabra # {} ".format(i+1))
    lista.append(input_value)
print("La lista creada es:",lista)
input_name = input("Digame la palabra a buscar:")
if lista.count(input_name) == 0:
    print("La palabra",input_name,"no aparece en la lista")
else:
    print("La palabra",input_name,"aparece",lista.count(input_name),"veces")
input_number = input("Cuantas palabras tiene la lista?")
lista=[]
for i in range(0,int(input_number)):
    input_value = input("Por favor ingrese la palabra # {} ".format(i+1))
    lista.append(input_value)
print("La lista creada es:",lista)
input_name = input("Digame la palabra a buscar:")
if lista.count(input_name) == 0:
    print("La palabra",input_name,"no aparece en la lista")
else:
    print("La palabra",input_name,"aparece",lista.count(input_name),"veces")
input_number = input("Cuantas palabras tiene la lista?")
lista=[]
for i in range(0,int(input_number)):
    input_value = input("Por favor ingrese la palabra # {} ".format(i+1))
    lista.append(input_value)
print("La lista creada es:",lista)
input_name = input("Digame la palabra a buscar:")
if lista.count(input_name) == 0:
    print("La palabra",input_name,"no aparece en la lista")
else:
    print("La palabra",input_name,"aparece",lista.count(input_name),"veces")



#3.3
print("3.3:")
input_number = input("Cuantas palabras tiene la lista?")
lista=[]
for i in range(0,int(input_number)):
    input_value = input("Por favor ingrese la palabra # {} ".format(i+1))
    lista.append(input_value)
print("La lista creada es:",lista)
input_old = input("Digame la palabra que desea sustituir:")
input_new = input("Digame la nueva palabra que desea:")
for i in lista:
    if i == input_old:
        lista[lista.index(i)] = input_new
print("La lista ahora es:", lista)

#3.4
print("3.4:")
input_number = input("Cuantas palabras tiene la lista?")
lista=[]
for i in range(0,int(input_number)):
    input_value = input("Por favor ingrese la palabra # {} ".format(i+1))
    lista.append(input_value)
print("La lista creada es:",lista)
input_del = input("Digame la palabra que desea borrar:")
for i in lista:
    if i == input_del:
        lista.remove(input_del)
print("La lista ahora es:", lista)


#3.5
print("3.5:")
input_number = input("Cuantas palabras tiene la lista?")
lista=[]
for i in range(0,int(input_number)):
    input_value = input("Por favor ingrese la palabra # {} ".format(i+1))
    lista.append(input_value)
print("La lista creada es:",lista)
input_number2 = input("Cuantas palabras tiene la lista a eliminar?")
lista2=[]
for i in range(0,int(input_number2)):
    input_value2 = input("Por favor ingrese la palabra # {} por eliminar".format(i+1))
    lista2.append(input_value2)
print("La lista de palabras a eliminar es:",lista2)
for i in lista:
    for n in lista2:
        if i == n:
            lista.remove(n)
print("La lista ahora es:",lista)


#3.6
print("3.6:")
input_number = input("Cuantas palabras tiene la lista?")
lista=[]
lista2=[]
for i in range(0,int(input_number)):
    input_value = input("Por favor ingrese la palabra # {} ".format(i+1))
    lista.append(input_value)
    lista2.insert(0,input_value)
print("La lista creada es:",lista)
print("La lista inversa es:",lista2)

#3.7
print("3.7:")
input_number = input("Cuantas palabras tiene la lista?")
lista=[]
for i in range(0,int(input_number)):
    input_value = input("Por favor ingrese la palabra # {} ".format(i+1))
    lista.append(input_value)
print("La lista creada es:",lista)
lista = list(dict.fromkeys(lista))
print("La lista sin duplicados es:",lista)


#3.8
print("3.8:")
input_number = input("Cuantas palabras tiene la primera lista?")
lista=[]
for i in range(0,int(input_number)):
    input_value = input("Por favor ingrese la palabra # {} ".format(i+1))
    lista.append(input_value)
print("La primera lista es:",lista)
input_number2 = input("Cuantas palabras tiene la segunda lista?")
lista2=[]
for i in range(0,int(input_number2)):
    input_value2 = input("Por favor ingrese la palabra # {} ".format(i+1))
    lista2.append(input_value2)
print("La segunda lista es:",lista2)
lista = list(dict.fromkeys(lista))
lista2 = list(dict.fromkeys(lista2))
both=[]
first=[]
second=[]
all = lista + lista2
all = list(dict.fromkeys(all))

for i in lista:
    for n in lista2:
        if n == i:
            both.append(n)

first = list(set(lista)-set(lista2))
second = list(set(lista2)-set(lista))

print("Las palabras que aparecen en ambas listas son:",both)
print("Las palabras que solo aparecen en la primera lista son:",first)
print("Las palabras que solo aparecen en la segunda lista son:",second)
print("Todas las palabras son:",all)

