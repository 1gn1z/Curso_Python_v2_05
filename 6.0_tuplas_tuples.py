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

punto[0] = 3