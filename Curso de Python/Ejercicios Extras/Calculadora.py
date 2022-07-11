# Creacion de una calculadora utilizando tkinter
import tkinter as tk


# Funcion para limpiar la pantalla
def limpiar():
    pantalla.delete(0, tk.END)

# Funcion para calcular la operacion
def calcular():
    try:
        resultado = eval(pantalla.get())
        pantalla.delete(0, tk.END)
        pantalla.insert(0, resultado)
    except:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, 'Error')

# Funcion para agregar un punto
def punto():
    if '.' not in pantalla.get():
        pantalla.insert(tk.END, '.')

# Funcion para agregar un signo
def signo():
    if pantalla.get()[0] != '-':
        pantalla.insert(0, '-')
    else:
        pantalla.delete(0, 1)

# Funcion para agregar una operacion
def operacion():
    if pantalla.get() != '':
        if '+' in pantalla.get():
            try:
                # Se guardan los datos en la variable operacion
                operacion = pantalla.get()
                # Se separa el string en dos partes eliminando el signo +
                operacion = operacion.split('+')
                # Se guarda el resultado de la operacion en la variable resultado
                resultado = float(operacion[0]) + float(operacion[1])
                resultado = str(resultado)
                # Se limpia la pantalla
                pantalla.delete(0, tk.END)
                # Se inserta el resultado en la pantalla
                pantalla.insert(0, resultado)
            except:
                pantalla.delete(0, tk.END)
                pantalla.insert(0, 'Error')
        elif '-' in pantalla.get():
            try:
                # Se guardan los datos en la variable operacion
                operacion = pantalla.get()
                # Se separa el string en dos partes eliminando el signo +
                operacion = operacion.split('-')
                # Se guarda el resultado de la operacion en la variable resultado
                resultado = float(operacion[0]) - float(operacion[1])
                resultado = str(resultado)
                # Se limpia la pantalla
                pantalla.delete(0, tk.END)
                # Se inserta el resultado en la pantalla
                pantalla.insert(0, resultado)
            except:
                pantalla.delete(0, tk.END)
                pantalla.insert(0, 'Error')
        elif '*' in pantalla.get():
            try:
                # Se guardan los datos en la variable operacion
                operacion = pantalla.get()
                # Se separa el string en dos partes eliminando el signo +
                operacion = operacion.split('*')
                # Se guarda el resultado de la operacion en la variable resultado
                resultado = float(operacion[0]) * float(operacion[1])
                resultado = str(resultado)
                # Se limpia la pantalla
                pantalla.delete(0, tk.END)
                # Se inserta el resultado en la pantalla
                pantalla.insert(0, resultado)
            except:
                pantalla.delete(0, tk.END)
                pantalla.insert(0, 'Error')
        elif '/' in pantalla.get():
            try:
                # Se guardan los datos en la variable operacion
                operacion = pantalla.get()
                # Se separa el string en dos partes eliminando el signo +
                operacion = operacion.split('/')
                # Se guarda el resultado de la operacion en la variable resultado
                resultado = float(operacion[0]) / float(operacion[1])
                resultado = str(resultado)
                # Se limpia la pantalla
                pantalla.delete(0, tk.END)
                # Se inserta el resultado en la pantalla
                pantalla.insert(0, resultado)
            except:
                pantalla.delete(0, tk.END)
                pantalla.insert(0, 'Error')
        elif '**' in pantalla.get():
            try:
                # Se guardan los datos en la variable operacion
                operacion = pantalla.get()
                # Se separa el string en dos partes eliminando el signo +
                operacion = operacion.split('**')
                # Se guarda el resultado de la operacion en la variable resultado
                resultado = float(operacion[0]) ** float(operacion[1])
                resultado = str(resultado)
                # Se limpia la pantalla
                pantalla.delete(0, tk.END)
                # Se inserta el resultado en la pantalla
                pantalla.insert(0, resultado)
            except:
                pantalla.delete(0, tk.END)
                pantalla.insert(0, 'Error')
        elif '%' in pantalla.get():
            try:
                # Se guardan los datos en la variable operacion
                operacion = pantalla.get()
                # Se separa el string en dos partes eliminando el signo +
                operacion = operacion.split('%')
                # Se guarda el resultado de la operacion en la variable resultado
                resultado = float(operacion[0]) % float(operacion[1])
                resultado = str(resultado)
                # Se limpia la pantalla
                pantalla.delete(0, tk.END)
                # Se inserta el resultado en la pantalla
                pantalla.insert(0, resultado)
            except:
                pantalla.delete(0, tk.END)
                pantalla.insert(0, 'Error')
        elif operacion == '=':
            calcular()
        else:
            pantalla.insert(tk.END, 'Error')

# Funcion borrar
def borrar():
    pantalla.delete(0, tk.END)

# Funcion rehacer que elimina el ultimo caracter ingresado
def rehacer():
    pantalla.delete(len(pantalla.get())-1, tk.END)

# Funcion raiz
def raiz():
    try:
        if pantalla.get() != '':
            # Se guarda el resultado de la raiz en la variable resultado
            resultado = pantalla.get()
            resultado = int(resultado) ** 0.5
            # Se limpia la pantalla
            pantalla.delete(0, tk.END)
            # Se inserta el resultado en la pantalla
            pantalla.insert(0, resultado)
        else:
            pantalla.insert(tk.END, 'Error')
    except:
        # Limpiar la pantalla
        pantalla.delete(0, tk.END)
        # Insertar el mensaje de error
        pantalla.insert(tk.END, 'Error')
    
# Funcion igual
def igual():
    if pantalla.get() != '':
        pantalla.delete(0, tk.END)
        pantalla.insert(0, eval(pantalla.get()))

# Inicio del programa
if __name__ == '__main__':
    root = tk.Tk()
    root.title('Mi Calculadora \( ͡• ͜ʖ ͡•)/')
    root.config(bg='#8e1f3c')
    root.geometry('675x600')

    # Creacion de la pantalla autoajustable en el tamaño de la ventana
    pantalla = tk.Entry(root, width=35, bg='#d0d0d0', font=('Arial', 20))
    pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    pantalla.insert(0, '0')

    # Creacion de los botones
    # Botón 1: Número 1
    boton1 = tk.Button(root, text='1', width=5, height=2, bg='#89cfff', font=('Arial', 20), command=lambda:pantalla.insert(tk.END, '1'))
    boton1.grid(row=1, column=0, padx=10, pady=10)

    # Botón 2: Número 2
    boton2 = tk.Button(root, text='2', width=5, height=2, bg='#89cfff', font=('Arial', 20), command=lambda:pantalla.insert(tk.END, '2'))
    boton2.grid(row=1, column=1, padx=10, pady=10)

    # Botón 3: Número 3
    boton3 = tk.Button(root, text='3', width=5, height=2, bg='#89cfff', font=('Arial', 20), command=lambda:pantalla.insert(tk.END, '3'))
    boton3.grid(row=1, column=2, padx=10, pady=10)

    # Botón 4: Número 4
    boton4 = tk.Button(root, text='4', width=5, height=2, bg='#89cfff', font=('Arial', 20), command=lambda:pantalla.insert(tk.END, '4'))
    boton4.grid(row=2, column=0, padx=10, pady=10)

    # Botón 5: Número 5
    boton5 = tk.Button(root, text='5', width=5, height=2, bg='#89cfff', font=('Arial', 20), command=lambda:pantalla.insert(tk.END, '5'))
    boton5.grid(row=2, column=1, padx=10, pady=10)

    # Botón 6: Número 6
    boton6 = tk.Button(root, text='6', width=5, height=2, bg='#89cfff', font=('Arial', 20), command=lambda:pantalla.insert(tk.END, '6'))
    boton6.grid(row=2, column=2, padx=10, pady=10)

    # Botón 7: Número 7
    boton7 = tk.Button(root, text='7', width=5, height=2, bg='#89cfff', font=('Arial', 20), command=lambda:pantalla.insert(tk.END, '7'))
    boton7.grid(row=3, column=0, padx=10, pady=10)

    # Botón 8: Número 8
    boton8 = tk.Button(root, text='8', width=5, height=2, bg='#89cfff', font=('Arial', 20), command=lambda:pantalla.insert(tk.END, '8'))
    boton8.grid(row=3, column=1, padx=10, pady=10)

    # Botón 9: Número 9
    boton9 = tk.Button(root, text='9', width=5, height=2, bg='#89cfff', font=('Arial', 20), command=lambda:pantalla.insert(tk.END, '9'))
    boton9.grid(row=3, column=2, padx=10, pady=10)

    # Botón 10: Número 0
    boton0 = tk.Button(root, text='0', width=5, height=2, bg='#89cfff', font=('Arial', 20), command=lambda:pantalla.insert(tk.END, '0'))
    boton0.grid(row=4, column=0, padx=10, pady=10)

    # Botón 11: Punto
    botonpunto = tk.Button(root, text='.', width=5, height=2, bg='#89cfff', font=('Arial', 20), command=punto)
    botonpunto.grid(row=4, column=1, padx=10, pady=10)

    # Botón 12: Signo
    botonsigno = tk.Button(root, text='+/-', width=5, height=2, bg='#89cfff', font=('Arial', 20), command=signo)
    botonsigno.grid(row=4, column=2, padx=10, pady=10)

    # Botón 13: Borrar
    botonborrar = tk.Button(root, text='C', width=5, height=2, bg='#89cfff', font=('Arial', 20), command=rehacer)
    botonborrar.grid(row=5, column=0, padx=10, pady=10)

    # Botón 14: Borrar todo
    botonborratodo = tk.Button(root, text='CE', width=5, height=2, bg='#89cfff', font=('Arial', 20), command=borrar)
    botonborratodo.grid(row=5, column=1, padx=10, pady=10)

    # Botón 15: Operación
    botonoperacion = tk.Button(root, text='=', width=5, height=2, bg='#89cfff', font=('Arial', 20), command=operacion)
    botonoperacion.grid(row=5, column=2, padx=10, pady=10)

    # Botón 16: Suma
    botonsuma = tk.Button(root, text='+', width=5, height=2, bg='#89cfff', font=('Arial', 20), command=lambda:pantalla.insert(tk.END, '+'))
    botonsuma.grid(row=1, column=3, padx=10, pady=10)

    # Botón 17: Resta
    botonresta = tk.Button(root, text='-', width=5, height=2, bg='#89cfff', font=('Arial', 20), command=lambda:pantalla.insert(tk.END, '-'))
    botonresta.grid(row=2, column=3, padx=10, pady=10)

    # Botón 18: Multiplicación
    botonmultiplicacion = tk.Button(root, text='x', width=5, height=2, bg='#89cfff', font=('Arial', 20), command=lambda:pantalla.insert(tk.END, '*'))
    botonmultiplicacion.grid(row=3, column=3, padx=10, pady=10)

    # Botón 19: División
    botondivision = tk.Button(root, text='/', width=5, height=2, bg='#89cfff', font=('Arial', 20), command=lambda:pantalla.insert(tk.END, '/'))
    botondivision.grid(row=4, column=3, padx=10, pady=10)

    # Botón 20: Porcentaje
    botonporcentaje = tk.Button(root, text='%', width=5, height=2, bg='#89cfff', font=('Arial', 20), command=lambda:pantalla.insert(tk.END, '%'))
    botonporcentaje.grid(row=5, column=3, padx=10, pady=10)
    
    # Botón 21: Raiz
    botonraiz = tk.Button(root, text='√', width=5, height=2, bg='#89cfff', font=('Arial', 20), command=raiz)
    botonraiz.grid(row=1, column=4, padx=10, pady=10)

    # Ejecución de la aplicación
    root.mainloop()

    # Fin del programa
    print('Gracias por utilizar la Calculadora')
