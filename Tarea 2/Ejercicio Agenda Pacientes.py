lista = []

# Data inicial para pruebas:

lista = [["304700376", "Roger", "Jimenez", "60504892", "Tibas", "Enfermedad: Dolor", "Enfermedad: Mareos",
          "Medicamento: Acetaminofen", "Medicamento: Gravol"],
         ["114910761", "Alejandra", "Torres", "837226121", "Heredia", "Enfermedad: Sangrado", "Enfermedad: Mareos",
          "Medicamento: Cortisol", "Medicamento: Gravol"],
         ["234226781", "Luis", "Hernandez", "85679001", "Santa Ana", "Enfermedad: Inflamacion", "Enfermedad: Sangrado",
          "Medicamento: Acetaminofen", "Medicamento: Pronol"],
         ["178901427", "Marta", "Rivera", "65484032", "Curridabat", "Enfermedad: Cancer", "Enfermedad: Dolor",
          "Medicamento: Quimio", "Medicamento: Panadol"]]

print("Bienvenido al sistema de la clínica!")

while True:
    paciente = []
    print("1 - Agregar un paciente nuevo")
    print("2 - Eliminar un paciente")
    print("3 - Agregar enfermedad a un paciente")
    print("4 - Agregar medicamento a un paciente")
    print("5 - Consultar la lista actual de la clínica")
    print("6 - Generar reporte de pacientes con su contacto")
    print("7 - Generar reporte de enfermedades en la clínica")
    print("8 - Generar reporte de medicamentos entregados")
    print("9 - Comparar 2 pacientes")
    print("10 - Salir")
    x = input("Seleccione una opción con los numeros del menu:")
    x = int(x)
    if x == 1:
        id = input("Ingrese la identificación del paciente: ")
        paciente.append(id)
        nombre = input("Ingrese el nombre del paciente: ")
        paciente.append(nombre)
        apellido = input("Ingrese el apellido del paciente: ")
        paciente.append(apellido)
        phone = input("Ingrese el teléfono del paciente: ")
        paciente.append(phone)
        address = input("Ingrese la dirección del paciente: ")
        paciente.append(address)

        lista.append(paciente)
        print("Paciente agregado!")
        print(lista)
    if x == 2:
        id_del = input("Ingrese la identificación del paciente que desea eliminar: ")
        lista = [i for i in lista if i[0] != id_del]
        print("Paciente borrado!")
        print("La nueva lista es: ", lista)
    if x == 3:
        id_enf = input("Ingrese la identificación del paciente que desea actualizar: ")
        enf = input("Ingrese la enfermedad del paciente: ")
        for i in lista:
            if i[0] == id_enf:
                i.append("Enfermedad: " + enf)
        print("Enfermedad agregada!")
        print("La nueva lista es: ", lista)
    if x == 4:
        id_enf = input("Ingrese la identificación del paciente que desea actualizar: ")
        enf = input("Ingrese el medicamento del paciente: ")
        for i in lista:
            if i[0] == id_enf:
                i.append("Medicamento: " + enf)
        print("Medicamento agregado!")
        print("La nueva lista es: ", lista)
    if x == 5:
        for i in lista:
            i[5::] = sorted(i[5::])
        for count, i in enumerate(lista):
            print("Paciente {}".format(count + 1), " - ", "ID:", i[0], "Nombre:", i[1], "Apellido:", i[2], "Telefono:",
                  i[3], "Direccion:", i[4], i[5::])
    if x == 6:
        for count, i in enumerate(lista):
            print("Paciente {}".format(count + 1), " - ", "Nombre:", i[1], i[2], "|", "Telefono:", i[3])
    if x == 7:
        enfermedades = [p for i in lista for p in i if "Enfermedad" in p]
        enfermedades = list(set(enfermedades))
        print("La lista de enfermedades atendidas en la clínica es: ")
        for i in enfermedades:
            print(i)
    if x == 8:
        meds = [p for i in lista for p in i if "Medicamento" in p]
        meds = list(set(meds))
        print("La lista entregadas por la clínica es: ")
        for i in meds:
            print(i)
    if x == 9:
        id_1 = input("Ingrese la identificación del primer paciente de la comparacion: ")
        id_2 = input("Ingrese la identificación del segundo paciente de la comparacion: ")

        enfermedades1 = [p for i in lista for p in i if "Enfermedad" in p and i[0] == id_1]
        enfermedades1 = set(enfermedades1)

        enfermedades2 = [p for i in lista for p in i if "Enfermedad" in p and i[0] == id_2]
        enfermedades2 = set(enfermedades2)

        print("Enfermadades en comun: ", enfermedades1 & enfermedades2)
        print("Enfermadades que no tienen en comun: ", enfermedades1 ^ enfermedades2)
        print("Enfermadades que tiene el primer paciente pero no el segundo: ", enfermedades1 - enfermedades2)
        print("Enfermadades que tiene el segundo paciente pero no el primero: ", enfermedades2 - enfermedades1)

        meds1 = [p for i in lista for p in i if "Medicamento" in p and i[0] == id_1]
        meds1 = set(meds1)

        meds2 = [p for i in lista for p in i if "Medicamento" in p and i[0] == id_2]
        meds2 = set(meds2)

        print("Medicamentos en comun: ", meds1 & meds2)
        print("Medicamentos que no tienen en comun: ", meds1 ^ meds2)
        print("Medicamentos que tiene el primer paciente pero no el segundo: ", meds1 - meds2)
        print("Medicamentos que tiene el segundo paciente pero no el primero: ", meds2 - meds1)
    if x == 10:
        print("Gracias por usar nuestro sistema, chao!")
        break

