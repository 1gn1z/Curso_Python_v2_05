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