# importacion del modulo time para obtener el tiempo
import time

# Script que muestra el tiempo actual en formato HH:MM:SS y calcula si es o no es hora de ir a casa (después de las 19:00)

# Variable que contiene el tiempo restante para las 19:00
missingForSeven = 19 - int(time.strftime("%H", time.localtime()))

# Se imprime el tiempo actual
print(time.strftime("Son las %H:%M:%S", time.localtime()))

# Si el tiempo restante es menor o igual a cero, se imprime que ya es hora de ir a casa, de lo contrario, se imprime el tiempo restante
if (missingForSeven > 0):
    print("Faltan aprox.", (missingForSeven), "hora(s) para las 19:00")
    print("Todavía no es hora de ir a casa")
else:
    print("Van aprox.", -missingForSeven, "hora(s) después de las 19:00")
    print("Ya es hora de ir a casa")
