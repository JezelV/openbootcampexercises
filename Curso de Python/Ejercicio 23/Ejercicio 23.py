# Programa que crea una tabla "Alumnos" que consta de tres columnas, id de tipo entero, columna nombre de tipo cadena y apellido de tipo cadena.
# Luego se insertan 10 registros en la tabla.
# Por ultimo se realiza una búsqueda de un alumno por nombre y se muestran los datos por consola.

import sqlite3
import os

from pip import main

def main():
    # Se comprueba si la tabla ya existe, y si no existe se crea
    if 'alumnos.db' not in os.listdir():
        create_table()
    else:
        print("La tabla ya existe, no es necesario crearla")
    
    # Se comprueba si la tabla está vacía, y si no está vacía se insertan los datos
    conn = sqlite3.connect("./alumnos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alumnos")
    data = cursor.fetchall()
    if len(data) == 0:
        insert_data()
    else:
        print("La tabla ya contiene datos, no es necesario insertarlos")
    conn.close()

    search_data()

def create_table():
    conn = sqlite3.connect("./alumnos.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE alumnos(
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        apellido TEXT
        )''')
    conn.commit()
    conn.close()
    print("Tabla creada exitosamente")

def insert_data():
    conn = sqlite3.connect("./alumnos.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO alumnos VALUES(1, 'Juan', 'Perez')")
    cursor.execute("INSERT INTO alumnos VALUES(2, 'Pedro', 'Gonzalez')")
    cursor.execute("INSERT INTO alumnos VALUES(3, 'Maria', 'Gonzalez')")
    cursor.execute("INSERT INTO alumnos VALUES(4, 'Juan', 'Gonzalez')")
    cursor.execute("INSERT INTO alumnos VALUES(5, 'Juan', 'Perez')")
    cursor.execute("INSERT INTO alumnos VALUES(6, 'Pedro', 'Perez')")
    cursor.execute("INSERT INTO alumnos VALUES(7, 'Maria', 'Perez')")
    cursor.execute("INSERT INTO alumnos VALUES(8, 'Juan', 'Gomez')")
    cursor.execute("INSERT INTO alumnos VALUES(9, 'Pedro', 'Gomez')")
    cursor.execute("INSERT INTO alumnos VALUES(10, 'Maria', 'Gomez')")
    conn.commit()
    conn.close()
    print("Alumnos agregados correctamente")

def search_data():
    conn = sqlite3.connect("./alumnos.db")
    cursor = conn.cursor()
    input_name = input("Introduce el nombre del alumno que deseas buscar: ")
    query = f'SELECT * FROM alumnos WHERE nombre="{input_name}"'
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    if len(data) == 0:
        print("No se ha encontrado ningún alumno con ese nombre")
    elif len(data) == 1:
        print(f"El alumno con nombre {input_name} es: {data[0][1]} {data[0][2]}")
    else:
        print(f"Se han encontrado {len(data)} alumnos con el nombre {input_name}")
        aux = 1
        for i in data:
            print(f'Alumno {aux}: ')
            print(f'Nombre: {i[1]} {i[2]} ID: {i[0]}')
            aux += 1

if __name__ == '__main__':
    main()
