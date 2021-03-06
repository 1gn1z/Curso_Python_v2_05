# Tipo de dato compuesto string

nombre = "Kebor Mastah"
email = "kebor327@gmail.com"

direccion = ''' Calle Alfonso Herrera # 79
Colonia San Rafael Chamapa
Naucalpan de Juaréz, Estado de México
'''

print(nombre)
print(email)
print(direccion)

mensaje = "Bivenvenido(a), " + nombre + " Correo: " + email + " Direccion: " + direccion 
print(mensaje)


#Interpolación:
mensaje = f"Bivenvenido(a), {nombre}. Correo: {email}. Dirección: {direccion}."
print(mensaje)

# format() de la clase str:
mensaje = "Bienvenido(a), {}. Correo: {}. Dirección: {}.".format(nombre, email, direccion)
print(mensaje)

# formato con %s
mensaje = "Bienvenido(a), %s. Correo: %s. Dirección: %s." %(nombre, email, direccion)
print(mensaje)

# Inmutabilidad de cadenas de caracteres (str):

lenguaje = "Python"
print(lenguaje)
print(lenguaje[0])
print(lenguaje[1])
print(lenguaje[2])
print(lenguaje[3])
print(lenguaje[4])
print(lenguaje[5])

print()

# lenguaje[0] = "p" #TypeError

lenguaje = "p" + lenguaje[1:]
print(lenguaje)

# Tipos de datos inmutables, se dice que son estáticos.

# Averiguar la posición de memoria de una variable (o de una cadena en este caso)

print(id("python") == id("python"))

lenguaje = "Python".lower()
print(lenguaje)

print()

# Uso del método str.split()
valores = "2,3,5,7,11"
lista_valores = valores.split(',')
print(len(lista_valores))
print(lista_valores)

# Método str.find()
indice = valores.find('1')
print('El índice del elemento "1" es igual a', indice)

indice = valores.find('8')
print('El índice del elemento "8" es igual a', indice)

# Creación de una función (proceso) personalizado para buscar una cadena dentro de otra

def encontrar(cadena, caracter):
    indice = -1
    for i in range(0, len(cadena)):
        if caracter == cadena[i]:
            indice = i
            break
    return indice

indice = encontrar(valores, "2")
print('El indice del elemento "2" es igual a', indice)