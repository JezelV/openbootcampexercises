

Nombre = "Juan"
Apellidos = "Perez Gomez"
Edad = 12
Email = "juanitoperez@mail.com"
Telefono = "+52 012 345 67 89"
Casado = False
conHijos = False
listaDeAmigos = ["Tete", "Pancho", "Pedro"]
peliculasVistas = {'primera': 'Toy Story 2', 'segunda': 'Sonic The Hedgehog', 'tercera': 'Catch me if you can'}

# *Mostrar informacion

print("Nombre:", Nombre)
print("Apellidos:", Apellidos)
print("Edad:", Edad)
print("Email:", Email)
print("Telefono:", Telefono)
print("Casado:", Casado)
print("Con hijos:", conHijos)
print("Lista de amigos:")
for amigo in listaDeAmigos:
    print(amigo)
print ("Peliculas vistas:")
for pelicula in peliculasVistas:
    print(pelicula + ": " + peliculasVistas[pelicula])
