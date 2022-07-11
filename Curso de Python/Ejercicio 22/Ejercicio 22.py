# Programa que muestra una lista de nombres de personas y permite seleccionar alguno de ellos.

import tkinter as tk
from tkinter import ttk

window = tk.Tk() # Se crea la ventana principal
window.title("Ejercicio 21") # Se le pone un titulo a la ventana
window.resizable(0, 0) # Se deshabilitan la opción para cambiar el tamaño de la ventana
x_ventana = window.winfo_screenwidth() // 2 - 350 // 2 # Se calcula el centro de la ventana en el eje x
y_ventana = window.winfo_screenheight() // 2 - 150 // 2 # Se calcula el centro de la ventana en el eje y
posicion = str(350) + "x" + str(150) + "+" + str(x_ventana) + "+" + str(y_ventana) # Se crea la cadena de posicion centrada
window.geometry(posicion) # Se inicializa la ventana en el centro de la pantalla

# Se crea una lista de nombres de personas
nombres = ["Juan", "Pedro", "María", "José", "Luis", "Rosa", "Carlos", "Juan", "Pedro", "María", "José", "Luis", "Rosa", "Carlos"]

# Se crea una lista de botones que muestran el nombre de la persona seleccionada
botones = []

# Se crea una lista de variables que guardan el nombre de la persona seleccionada
seleccionadas = []

# Se muestran las opciones de la lista
for i in range(len(nombres)):
    botones.append(ttk.Button(window, text=nombres[i], command=lambda i=i: seleccionar(i)))
    botones[i].grid(column=i % 4, row=i // 4, pady=5, padx=5)
    seleccionadas.append(tk.StringVar())
    seleccionadas[i].set(None)

def seleccionar(i):
    print("Se ha seleccionado: " + nombres[i])

tk.mainloop()
