#crear una tupla de 5 elementos de tipos diferentes

mi_tupla =  (1,'Roger', 5.34, 'Python', False)
print(mi_tupla)

# agregar mas elementos en una tupla??

mi_tupla = mi_tupla + (11, 'Nuevo elemento')

print (mi_tupla)

# acumular elementos

mi_tupla += (0,'x')

print(mi_tupla)

#subtupla
#el segundo hasta el penultimo

print(mi_tupla[1:-1])

#subtupla con saltos
#los elementos pares - que esten en indice par
#ojo que el cero es par

print('los elementos pares son: ', mi_tupla[::2])

#los elementos impares

print('los elementos impares son: ', mi_tupla[1::2])