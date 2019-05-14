#1

mis_valores = [5, 6, 10, 13, 3, 4]
numerator = 0
dividend = len(mis_valores)
for i in mis_valores:
    numerator += i
print("El promedio de la lista es:", numerator/dividend)

#2


todos = [

    [177, 145, 167, 190, 140, 150, 180, 130],  # grupo 1

    [165, 176, 145, 189, 170, 189, 159, 190],  # grupo 2

    [145, 136, 178, 200, 123, 145, 145, 134],  # grupo 3

    [201, 110, 187, 175, 156, 165, 156, 135]  # grupo 4

]

result = []

for inner_list in todos:
    result.append(max(inner_list))

max_index = result.index(max(result))

print("El grupo que contiene la mayor altura de todos es el: ", "Grupo #", max_index + 1,
      ", el cual contiene las siguientes alturas:", todos[max_index])
