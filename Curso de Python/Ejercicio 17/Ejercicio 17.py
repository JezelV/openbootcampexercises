# Programa que crea un archivo txt que escriba una lista de personas dentro del mismo.
# El archivo txt debe tener una lista de personas con nombre, apellido y edad.
# El programa debe tener una opción para agregar una persona a la lista.
# El programa debe tener una opción para eliminar una persona de la lista.
# El programa debe tener una opción para modificar una persona de la lista.
# El programa debe tener una opción para mostrar la lista de personas.
# El programa debe tener una opción para salir.

from time import sleep
import os.path as path


def crear_archivo():
    if path.exists("personas.txt"):
        opcion = input("¿Borrar datos? (s/n)")
        if opcion == "s":
            archivo = open("personas.txt", "w")
            archivo.close()
            print("Datos eliminados")
            sleep(2)
        else:
            print("No se borrará nada")
            menu()
    else:
        archivo = open("personas.txt", "w")
        archivo.close()
        menu()

def agregar_persona():
    archivo = open("personas.txt", "a")
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    edad = input("Ingrese la edad: ")
    archivo.write(nombre + " " + apellido + " " + edad + "\n")
    archivo.close()

def eliminar_persona():
    archivo = open("personas.txt", "r")
    lineas = archivo.readlines()
    archivo.close()
    archivo = open("personas.txt", "w")
    nombre = input("Ingrese el nombre: ")
    for linea in lineas:
        if nombre not in linea:
            archivo.write(linea+'\t')
    archivo.close()

def modificar_persona():
    archivo = open("personas.txt", "r")
    lineas = archivo.readlines()
    archivo.close()
    archivo = open("personas.txt", "w")
    nombre = input("Ingrese el nombre: ")
    for linea in lineas:
        if nombre in linea:
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            edad = input("Ingrese la edad: ")
            archivo.write(nombre + "\t" + apellido + "\t" + edad + "\n")
        else:
            archivo.write(linea)
    archivo.close()

def mostrar_personas():
    archivo = open("personas.txt", "r")
    lineas = archivo.readlines()
    archivo.close()
    if lineas == []:
        print("No hay personas")
        sleep(2)
    else:
        for linea in lineas:
            if linea == lineas[0]:
                print("Name\tLast\tAge")

            for palabra in linea.split():
                print(palabra, end="\t")
            print('\n')
        print("\nNo hay más personas")
        sleep(2)

def menu():
    opcion = 0
    while True:
        print("1. Crear archivo / Borrar Datos")
        print("2. Agregar persona")
        print("3. Eliminar persona")
        print("4. Modificar persona")
        print("5. Mostrar personas")
        print("6. Salir")
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            crear_archivo()
        elif opcion == 2:
            agregar_persona()
        elif opcion == 3:
            eliminar_persona()
        elif opcion == 4:
            modificar_persona()
        elif opcion == 5:
            mostrar_personas()
        elif opcion == 6:
            print("Gracias por usar el programa")
            break;
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu()
    input("Presione enter para salir")
    exit()
