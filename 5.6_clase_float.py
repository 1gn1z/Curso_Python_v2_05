# La función float retorna un número de punto flotante a partir de un entero o una cadena.

pi = 3.1415
precio = 29.95

print('El valor de la variable pi es: %.2f' %pi)
print('El valor de la variable precio es: %.2f' %precio)

# El uso de %f imprime la información con 6 decimales en total.
'''
Salida:
El valor de la variable pi es: 3.141500
El valor de la variable precio es: 29.950000
'''

print(pi)
print(precio)

print()

print('El tipo de dato para la variable pi es:', type(pi))
print('El tipo de dato para la variable precio es:', type(precio))

print()

print('Operaciones aritméticas sobre números de punto flotante:')

# Queremos representar la circunferencia completa de un circulo
# Con Pi tenemos la mitad de dicha circunferencia:

pi = pi*2
print('El nuevo valor de la variable pi es:', pi)

total = precio * 5
print('El total de la compra es: %.2f' %total)

# --------------------------------

print()
print('Creación de un número real (punto flotante) a aprtir de una cadena de caracteres:')

precio_computador = float(input('Digite el precio del computador: '))

