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
    print(f'Índice: {i} - Valor: {numeros[i]}')
    i += 1

print()

# Iteracion con indices negativos:

i = len(numeros) - 1 # recordar que la longitud en indices negativos es n-1
while i >= 0:
    print(f'Índice: {i} - Valor: {numeros[i]}')
    i -= 1

print()

# Ciclo FOR:
print('Iteración con índices de una lista con un ciclo for:')

for i in range(0, len(numeros)):
    print(f'Índice: {i} - Valor: {numeros[i]}')

print()
print()
print()
print('Iteración con índices de una lista con un ciclo for (del último elemento hacia el primero:')

for i in range(len(numeros) -1, -1, -1): 
    print(f'Índice: {i} - Valor: {numeros[i]}')

#for i in numeros:
#    print(i)

print()

print('Iteración por elemento de una lista usando un ciclo for:')

for i in numeros:   # Conocido en otros lenguajes como FOR EACH
    print(f'Valor: {i}')

print()

# Iteración de lista con la función enumerate()
print('Iteración de lista con la función enumerate():')

for i, v in enumerate(numeros):
    print(f'Índice: {i} - Valor: {v}')

# Operaciones sobre listas (clase 'list'):

# Inserción de elementos en una lista por medio de 'append()':
# Añade el elemento al final de la lista.
print('Inserción de elementos en una lista por medio de append():')

numeros.append(14)
numeros.append(16)
print('Cantidad actual de elementos en la lista numeros: ',len(numeros))
print('Contenido actual de la lista "numeros":', numeros)

print()

print('Inserción de elementos en una lista por medio de insert():')

numeros.insert(1, 2)
print('Contenido actual de la lista "numeros":', numeros)

# Inserción con índices negativos:
# Voy a agregar 18 al final sin ver el tuto :P

# numeros.insert(-1, 18)
# Salida [1, 2, 4, 6, 8, 12, 14, 18, 16] :(

numeros.insert(-1, 15)
print('Contenido actual de la lista "numeros":', numeros)

print()

# Remoción de un elemento con la función remove()
print('Remoción de un elemento con la función remove()')

# Vamos a eliminar el elemento 1
numeros.remove(1)    # Se pone el elemento a eliminar (1a coincidencia)
print('Contenido actual de la lista "numeros":', numeros)









