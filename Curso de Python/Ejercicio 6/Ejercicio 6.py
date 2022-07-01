
# Programa en Python para calcular el IMC (Índice de Masa Corporal)

peso = input("Ingrese su peso en kg: ")
altura = input("Ingrese su altura en m: ")

if peso.isdigit() and altura.isdigit():
    peso = float(peso)
    altura = float(altura)
    imc = peso / (altura ** 2)
    print("Tu índice de masa corporal es: ", round(imc, 2))

