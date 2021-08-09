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

# Iteración con un ciclo While:
i = 0   # esta variable será el índice que recorrerá todos  los elementos de la tupla
while i < len(numeros_primos):  # menor que porque si ponemos menor o igual, no nos daría el último elemento  
    print(f'El valor del elemento en el índice {i} es igual a {numeros_primos[i]}.')
    i += 1  # incrementamos en 1 el valor de i para que avance en los índices, y para NO tener un ciclo infinito.

