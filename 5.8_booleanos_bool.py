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

a = True
b = False

# Operadores lógicos: and (conjunción - y), or (disyunción - o)
print(a and b)

# and es multiplicacion lógica (ambas deben ser true para que arroje true)

print(a and not b)
# Aqui obtenemos true por que not b = true

# OR
# or es suma lógica (ambos deben ser false para que arroje false)
print()
print(b or a)
print(b or not a)

print()
print()

if a and not b:
    print('Sí hay awa')
else:
    print('No hay awa')

print()

if a or b:
    print('Sí hay awa')
else:
    print('No hay awa')

# con AND, AMBAS deben cumplirse para que de TRUE, de lo contrario dará FALSE.

#con OR, SOLO UNA debe cumplirsr para que de TRUE, solo si ambas no se cumplen dará FALSE.