# Números enteros:

edad = 28
x = -5
puntaje = 300

print(type(edad))
print(type(x))

print(edad)
print(x)

# Con estos datos podemos hacer todo tipo de operaciones aritmeticas
# queremos añadirle 50 a puntaje:

print()
# %i es un placeholder para ENTEROS.
print('Puntaje antes de la adición de 50 puntos: %i' %puntaje)
puntaje = puntaje + 50
print('Puntaje después de la adición de 50 puntos: %i' %puntaje)

# Se pueden hacer: +,-,*,/,% (resudio) y ** (exponenciación)

#x = x + 10  forma normal
print('Valor de x antes de la adición: %i' %x)
x += 10    # forma mas chida :3
print('Valor de x despues de la adición: %i' %x)