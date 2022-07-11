# En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.
# Al principio no tiene que haber una opción seleccionada.
# Al pulsar el botón de reinicio, todos los RadioButton deben de quedar como al principio.

import tkinter as tk
from tkinter import ttk

def reinicio():
    primeraSeleccion.set(None)


window = tk.Tk() # Se crea la ventana principal
window.title("Ejercicio 21") # Se le pone un titulo a la ventana
window.resizable(0, 0) # Se deshabilitan la opción para cambiar el tamaño de la ventana
x_ventana = window.winfo_screenwidth() // 2 - 420 // 2 # Se calcula el centro de la ventana en el eje x
y_ventana = window.winfo_screenheight() // 2 - 100 // 2 # Se calcula el centro de la ventana en el eje y
posicion = str(420) + "x" + str(100) + "+" + str(x_ventana) + "+" + str(y_ventana) # Se crea la cadena de posicion centrada
window.geometry(posicion) # Se inicializa la ventana en el centro de la pantalla

primeraSeleccion = tk.StringVar()

# Se muestran las opciones de la lista
r1 = ttk.Radiobutton(window, text="Opción 1", value=0, variable=primeraSeleccion)
r2 = ttk.Radiobutton(window, text="Opción 2", value=1, variable=primeraSeleccion)
r3 = ttk.Radiobutton(window, text="Opción 3", value=2, variable=primeraSeleccion)
r4 = ttk.Radiobutton(window, text="Opción 4", value=3, variable=primeraSeleccion)
r5 = ttk.Radiobutton(window, text="Opción 5", value=4, variable=primeraSeleccion)

r1.grid(column=0, row=1, pady=5, padx=5)
r2.grid(column=1, row=1, pady=5, padx=5)
r3.grid(column=2, row=1, pady=5, padx=5)
r4.grid(column=3, row=1, pady=5, padx=5)
r5.grid(column=4, row=1, pady=5, padx=5)

# Adicion del botón de reinicio
botonReiniciar = ttk.Button(window, text="Reiniciar", command=reinicio)
botonReiniciar.grid(column=0, row=2, pady=5, padx=5)

tk.mainloop()
