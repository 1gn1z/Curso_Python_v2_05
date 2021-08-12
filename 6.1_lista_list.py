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


# Acceso con desempaquetamiento:

print('Acceso a datos de una lista con desempaquetamiento')

cuatro, seis, ocho = seccion
print(cuatro, seis, ocho)

# 2. Modificación de una lista:

print('2. Modificación de elementos de una lista')
numeros[0] = 1
print('El primer elemento (índice 0) de la lista es:', numeros[0])

print()

# Acceso a un índice que no existe:

# valor = numeros[8]     IndexError 
# valor = numeros[-6]    IndexError 

# Izquierda a Derecha: 0 hasta n-1 (n es el número total de la lista (# de elementos))
# Derecja a izquierda: -1 hasta -n (si la lista tiene 5 elementos el primer elemento seria -5)

# 3. Modificación de una lista (vía índices negativos)

print('El último elemento (índice -1) de la lista es:', numeros[-1])
numeros[-1] = 12
print('El último elemento (índice -1) de la lista es:', numeros[-1])

print()

# Iteración de listas:

# Ciclo WHILE:
print('Iteración de lista con ciclo while:')

i = 0
while i < len(numeros):
    print(f'Índice: {i} - Valor: {numeros[i]}', numeros[i])
    i += 1
print(i)
