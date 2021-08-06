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

mensaje = f"Bivenvenido(a), {nombre}. Correo: {email}. Dirección: {direccion}."
print(mensaje)
