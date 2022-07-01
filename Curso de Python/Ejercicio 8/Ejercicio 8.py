numeroInicial = int(input("Ingrese un numero de inicio: "))
numeroFinal = int(input("Ingrese otro numero final: "))
arregloDeImpares = []

for numeroActual in range(numeroInicial, numeroFinal + 1):
    if numeroActual % 2 != 0:
        arregloDeImpares.append(numeroActual)

print(arregloDeImpares)
