edad = input("Por favor ingresa tu edad: ")

if edad.isdigit():
    edad = int(edad)
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
