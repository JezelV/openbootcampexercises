# Función para calcular si un año es bisiesto

def esBisiesto(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

if esBisiesto(int(input("Bienvenido, Introduce un año: "))):
    print("Es un año bisiesto")
else:
    print("No es un año bisiesto")

print("Fin del programa")
