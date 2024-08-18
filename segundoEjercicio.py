"""
Jonathan Ignacio Marley Ramirez
#2019200176

En este ejercicio lo hice en base de interfaz ya que el segundo y el tercer parcial estuvimos viendo mucho sobre
la libreria de Tkinter es una libreria donde podemos crear interfaces llamativas.

La libreria que utilice la libreria num2words para realizar la conversion de numeros a palabras
Esta libreria se instala de la siguiente manera: pip install num2words

la podemos instalar de la siguiente manera
pip install num2words
"""

import tkinter as tk
from tkinter import messagebox
from num2words import num2words
import re

def converter(numero):
    return num2words(numero, lang='es').upper()

def validator(cadena):
    patron = "^-?[0-9]+$"
    if re.match(patron, cadena):
        return True
    else:
        return False

def convertir_numero():
    num = entrada.get()
    if validator(num):
        resultado.set(converter(int(num)))
    else:
        messagebox.showerror("Error", "El valor introducido no es un número entero")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Conversor de Números a Palabras")
ventana.geometry("400x200")

# Variables de texto
entrada = tk.StringVar()
resultado = tk.StringVar()

# Etiqueta y campo de entrada
tk.Label(ventana, text="Introduce un número:").pack(pady=10)
tk.Entry(ventana, textvariable=entrada).pack(pady=5)

# Botón para realizar la conversión
tk.Button(ventana, text="Convertir", command=convertir_numero).pack(pady=10)

# Etiqueta para mostrar el resultado
tk.Label(ventana, text="Resultado en palabras:").pack(pady=10)
tk.Label(ventana, textvariable=resultado).pack(pady=5)

# Inicia el bucle principal de la ventana
ventana.mainloop()
