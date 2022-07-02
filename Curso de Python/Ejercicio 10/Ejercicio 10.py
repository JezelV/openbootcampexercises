# Función para calcular el área de un triángulo

def area_triangulo(base, altura):
    area = (int(base) * int(altura)) / 2
    area = int(area)
    return "El área del triángulo es: " + str(area)

# Función para calcular el área de un círculo

def area_circulo(radio):
    area = (int(radio) ** 2) * 3.1415926535
    area = int(area)
    return "El área del círculo es: " + str(area)

# Inicio del programa

print("Introduce la base y altura del triangulo:")
print(area_triangulo(input(), input()))

print("Introduce el radio del círculo:")
print(area_circulo(input()))
