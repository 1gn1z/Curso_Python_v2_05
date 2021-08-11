# Tipo de dato compuesto tupla = estático

punto = (2, 5)
print('Tipo de dato:', type(punto))
print('Contenido de la variable punto:', punto)
print('Cantidad de elementos de la tupla punto:', len(punto))

print()
# Acceso a los elementos de una tupla:
x = punto[0]
y = punto[1]
print('El valor en x es igual a:', x)
print('El valor en y es igual a:', y)
print()

# Desempaquetamiento:
valor1, valor2 = punto
print('El valor en x es igual a:', valor1)
print('El valor en y es igual a:', valor2)

print()

# Acceso con índices negativos (de derecha a izquierda)

ultimo_elemento = punto[-1]
penultimo_elemento = punto[-2]
print('El valor en x es igual a:', ultimo_elemento)
print('El valor en y es igual a:', penultimo_elemento)

print()

# Concepto de inmutabilidad en una tupla:

# punto[0] = 3 # Genera TypeError

# Al reasignar una variable, el valor anterior se pierde.
punto = (3, 7)
x = punto[0]
y = punto[1]
print('El valor en x es igual a:', x)
print('El valor en y es igual a:', y)

print()

# Iteración de un objeto tipo tupla (tuple):

numeros_primos = (2, 3, 5, 7, 11, 13, 17, 19)

print('Cantidad de elementos de la tupla numeros_primos', len(numeros_primos))

# Iteración con un ciclo WHILE:

i = 0   # esta variable será el índice que recorrerá todos  los elementos de la tupla
while i < len(numeros_primos):  # menor que porque si ponemos menor o igual, no nos daría el último elemento  
    print(f'El valor del elemento en el índice {i} es igual a {numeros_primos[i]}.')
    i += 1  # incrementamos en 1 el valor de i para que avance en los índices, y para NO tener un ciclo infinito, porque si no aumentamos el valor de i la condicion del while siempre se cumpliría, en este caso al sumar 8 la condicion se cumple (ya no es menor que len(numeros_primos) sino que es igual, por ende temrmina el ciclo).

print()


# Iteración con un ciclo FOR:

for i in range(len(numeros_primos)):
    print(f'El valor del elemento en el índice {i} es igual a {numeros_primos[i]}.')

print()

# Iteración con un ciclo FOR MEJORADO:

for n in numeros_primos:
    print('Valor:' ,n)

print()

# Iteración de una tupla por medio de la función enumate():
print('Iteración de la tulpa numeros_primos con la función enumarate')

for i, v in enumerate(numeros_primos):
    print(f'El valor del elemento índice {i} es igual al {v}.')

print()

# Mecanismos alternativos para crear tuplas:
# Modo A:

numeros = 1, 2, 3
print('Tipo de dato de la variable números:', type(numeros))
print('Cantidad de elementos de la tupla:', len(numeros))
print('Contenido:', numeros)

print()

numeros = 1,
print('Tipo de dato de la variable números:', type(numeros))
print('Cantidad de elementos de la tupla:', len(numeros))
print('Contenido:', numeros)
print()
print()

# Modo B: uso de la clase tuple:


nums = tuple([1, 2, 3])
print('Tipo de dato de la variable números:', type(nums))
print('Cantidad de elementos de la tupla:', len(nums))
print('Contenido:', nums)
