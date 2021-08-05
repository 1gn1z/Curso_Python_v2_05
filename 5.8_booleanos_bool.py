# Booleanos

# Falso => False
# Verdadero => True

llueve = False
print(type(llueve))
print(llueve)

print()

llueve = not llueve
print(type(llueve))
print(llueve)

# Al principio era Flase (no llueve), pero invertimos el valor lógico
# asi que la condicional imprime "el día está lluvioso"

if llueve:
    print('El día está lluvioso.')
else:
    print('El día NO está lluvioso.')

print()

# Operaciones con variables o valores booleanos (lógicos):

llave_1 = True
llave_2 = False

# Operadores lógicos: and (conjunción - y), or (disyunción - o)
print(llave_1 and llave_2)

# and es multiplicacion lógica (ambas deben ser true para que arroje true)

print(llave_1 and not llave_2)
# Aqui obtenemos true por que not b = true

# OR
# or es suma lógica (ambos deben ser false para que arroje false)
print()
print(llave_2 or llave_1)
print(llave_2 or not llave_1)

print()
print()

if llave_1 and not llave_2:
    print('Sí hay awa')
else:
    print('No hay awa')

print()

if llave_1 or llave_2:
    print('Sí hay awa')
else:
    print('No hay awa')

# con AND, AMBAS deben cumplirse para que de TRUE, de lo contrario dará FALSE.

#con OR, SOLO UNA debe cumplirsr para que de TRUE, solo si ambas no se cumplen dará FALSE.

print( )

if not llave_1 or llave_2:
    print('Sí hay awa')
else:
    print('No hay awa')

# Refactorización para renombrar variables    