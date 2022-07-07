import pickle
import os.path as path
from time import sleep
# Creación de una clase que representa un Vehículo

class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def acelerar(self):
        print("El vehículo está acelerando")

    def frenar(self):
        print("El vehículo está frenando")

    def girar(self):
        print("El vehículo está girando")

    def __str__(self):
        return "Marca: " + self.marca + " Modelo: " + self.modelo + " Color: " + self.color

# Creación de un menú que permita guardar y cargar vehículos utilizando el módulo pickle
# Ejemplo: Elige una opción: 1. Guardar vehículo 2. Cargar vehículo 3. Salir
# 1. Guardar vehículo

if __name__ == '__main__':
    opcion = 0
    while opcion != 3:
        try:
            opcion = int(input('Elige una opción: 1. Guardar vehículo 2. Cargar vehículo 3. Salir\nOpción: '))
            if opcion == 1:
                marca = input('Marca: ')
                modelo = input('Modelo: ')
                color = input('Color: ')
                vehiculo = Vehiculo(marca, modelo, color)
                with open(f'{marca}.bin', 'wb') as f:
                    pickle.dump(vehiculo, f)
                    print('Vehículo guardado exitosamente como: ', marca)
            elif opcion == 2:
                archivo = input('Introduce el nombre del archivo (sin la extensión): ')
                if archivo != '' and path.isfile(f'{archivo}.bin'):
                    with open(f'{archivo}.bin', 'rb') as f:
                        vehiculo = pickle.load(f)
                        print(vehiculo)
                else:
                    print('Lo siento, el archivo especificado no existe')
            elif opcion == 3:
                print('Saliendo...')
                sleep(1)
            else:
                print('Opción inválida')
                opcion = 0
                continue
        except ValueError:
            print('Opción inválida')
    
    print('Gracias por utilizar el programa :)')
    sleep(1)