
# Programa que remueve los países repetidos en una lista utilizando el módulo set
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
        # Eliminamos los elementos repetidos
        lista = set(lista)
        # Ordenar alfabeticamente
        lista = sorted(lista)
        # Mostrar la lista en un string separado por comas
        print('Los países (o cadenas) introducidos son: ' + ', '.join(lista))
