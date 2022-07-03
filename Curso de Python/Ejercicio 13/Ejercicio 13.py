
class Vehiculo:
    Color = ""
    Ruedas = ""
    Puertas = ""

class Coche(Vehiculo):
    Velocidad = ""
    Cilindrada = ""

miCarro = Coche()

# Impresión de el objeto miCarro por consola:
print(miCarro) # Imprime el espacio en memoria del objeto miCarro

# Asignación de valores a los atributos de miCarro:
miCarro.Color = "Rojo"
miCarro.Ruedas = "4"
miCarro.Puertas = "5"
miCarro.Velocidad = "120km/h"
miCarro.Cilindrada = "1.0"

# Impresión de los atributos de miCarro por consola:
print("Color: ", miCarro.Color)
print("Ruedas: ", miCarro.Ruedas)
print("Puertas: ", miCarro.Puertas)
print("Velocidad Actual: ", miCarro.Velocidad)
print("Cilindrada: ", miCarro.Cilindrada)

