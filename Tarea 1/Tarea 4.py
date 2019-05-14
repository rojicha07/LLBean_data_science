hoja_calculo = [
    ['carlos', 54.54, 6.57, 3.64],
    ['juan', 5.54, 9.57, 4.64],
    ['luis', 9.54, 7.57, 1.64],
]


def transpuesta(hoja_calculo):
    return [list(i) for i in zip(*hoja_calculo)]


b = transpuesta(hoja_calculo)
b  # sea b la tabla resultante luego de aplicar transpuesta


# parte1

def avg(list):
    return sum(list) / len(list)


def mult(list):
    x = 1
    for i in list:
        x *= i
    return x


def suma(list):
    r = 0
    for n in list:
        r += n
    return r


def tax(list, rate):
    new = []
    for b in list:
        new.append(b * (1 + (rate / 100)))
    return new


functions = {
    "avg": avg,
    "mult": mult,
    "suma": suma,
    "tax": tax
}

# parte2

print("El promedio de miles de colones en débito es:", functions['avg'](b[1]))
print("La suma de todas las deudas es:", functions['suma'](b[3]))
print("La multiplicación de todos los créditos entre sí es:", functions['mult'](b[2]))


# parte3

def un_transpuesta(hoja_calculo):
    return [list(i) for i in zip(*hoja_calculo)]


b[2] = functions['tax'](b[2], 20)
c = un_transpuesta(b)
print("La nueva tabla general es:", c)


