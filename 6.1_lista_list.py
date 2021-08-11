# Tipo de dato compuesto: lista
# Las listas son un tipo de dato dinámico

# 1. Creación de una lista:
numeros = [2, 4, 6, 8, 10]
print('Tipo de dato de la variable numeros:', type(numeros))
print('Cantidad de elementos', len(numeros))
print('Contenido', numeros) # representación en cadena de caracteres.

print()

#2. Acceso a los elementos de una lista:
dos = numeros[0]
diez = numeros[-1]
print('El primer elemento (índice 0) de la lista es:', dos)
print('El último elemento (índice -1) de la lista es:', diez)

print()

seccion = numeros[1:4]
print(seccion)