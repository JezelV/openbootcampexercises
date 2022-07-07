
# Se importa reduce
from functools import reduce

# Programa que obtendrá los elementos impares de una lista pasada por parámetro con filter() y realizará una suma de todos los elementos obtenidos mediante reduce().

if __name__ == '__main__':
    # Primero se crea una lista con los países introducidos eliminando las comas
    lista = input('Introduce una lista de países separados por comas: ')
    # Se comprueba si la lista no contiene comas
    if ',' not in lista:
        print('Los datos proporcionados deben separarse por comas')
    else:
        # Se crea una lista a partir de la cadena introducida, para ordenarla y eliminar las repeticiones
        lista = lista.split(', ')
        # Se comprueba que lista no esté vacío
        if lista == ['']:
            print('No se proporcionó ninguna información')
        else:
            lista = [int(i) for i in lista]
            # Se obtiene una lista con los elementos impares de la lista original
            lista = filter(lambda x: x % 2 != 0, lista)
            # Se utiliza list() para convertir el iterador de filter() en una lista
            lista = list(lista)
            # Se suman todos los elementos de la lista obtenida
            lista = reduce(lambda x, y: x + y, lista)
            # Se convierte en entero
            lista = int(lista)
            print(f'La suma de los elementos impares de la lista proporcionada es:\n{lista}')
            
    print('Fin del programa')
