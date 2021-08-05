# Números complejos:

numero_complejo = 2 - 3j
print("Contenido variable compleja:", numero_complejo)
print("El tipo de dato de la variable numero_complejo es ", type(numero_complejo))

print()

numero_complejo = complex(2, -3)

# Operaciones básicas con variables de tipo de dato simple complejo

print('Operaciones aritméticas sobre números complejos:')

suma = 2 - 3j + (1 +5j)
print("Suma: ",suma)
print()

resta = 2 - 3j - complex(1, 5) # usamos la funcion complex en lugar de la parte final de la variable suma.

print('Resta:', resta)

print()

multiplicacion = 2 - 3j * complex(1, 5)
print("Multiplicación:", multiplicacion)