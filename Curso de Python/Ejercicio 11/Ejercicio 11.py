# Función para calcular números primos

def esPrimo(numero):
    if numero == 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True

if (esPrimo(int(input("Bienvenido, Introduce un número: ")))):
    print("Es un número primo")
else:
    print("No es un número primo")

print("Fin del programa")