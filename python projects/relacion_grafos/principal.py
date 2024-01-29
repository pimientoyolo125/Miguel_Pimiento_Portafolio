import os
import sys
from tkinter import *
from agregar import ventanaAgregar
from lista import ventanaLista
from grafo import ventanaGraf
from grafo import imagenGrafo
from porPersona import ventanaPersona
from resultadosGenerales import ventanaGeneral
from PIL import Image, ImageTk
import PIL.Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from personaCompatible import ventanaCompatible

stiles = {"bg": "#363636", "fg": "#84C9FB", "relief": FLAT, "activebackground":"#121212", "activeforeground" :"#363636", "width":23}

gridi = {"padx":10, "pady":10, "sticky":"w"}

def funPersona():
    ventanaPersona()

def funGeneral():
    ventanaGeneral()

def funCompatible():
    ventanaCompatible()

def funAgregar():
    ventanaAgregar()
    
def funLista():
    ventanaLista()

def funGrafo():
    imagenGrafo()
    ventanaGraf()

ventana = Tk()
ventana.resizable(0,0)
ventana.title("Sistema compatibilidad")
ventana.geometry("400x410+50+" + str(int(ventana.winfo_screenheight()/2 - 205)))
ruta_icono = os.path.dirname(os.path.abspath(sys.argv[0]))
ruta_icono = os.path.join(ruta_icono, "icono.ico")
if os.path.isfile(ruta_icono):
    ventana.iconbitmap(ruta_icono)
else:
    print(f"Error: No se encontró el archivo de icono en la ruta: {ruta_icono}")


frame = Frame(ventana)
ventana.configure(background="#121212")
frame.configure(background="#121212")
frame.pack()

botonAgregar = Button(frame, text="Agregar", font=("Cooper Black",18),**stiles, command=funAgregar)
botonAgregar.grid(row=0, column=0, **gridi)

botonLista = Button(frame, text="Lista", font=("Cooper Black", 18), command=funLista, **stiles)
botonLista.grid(row=1, column=0, **gridi)

botonGrafo = Button(frame, text="Mostrar Grafo", font=("Cooper Black", 18), command=funGrafo, **stiles)
botonGrafo.grid(row=2, column=0, **gridi)

botonResultadosg = Button(frame, text="Resultados Generales", font=("Cooper Black", 18), command=funGeneral, **stiles)
botonResultadosg.grid(row=3, column=0, **gridi)

botonPersona = Button(frame, text="Resultado por persona", font=("Cooper Black", 18), command=funPersona, **stiles)
botonPersona.grid(row=4, column=0, **gridi)

botonMascompatible = Button(frame, text="Persona mas compatible", font=("Cooper Black", 18), command=funCompatible, **stiles)
botonMascompatible.grid(row=5, column=0, **gridi)

ventana. mainloop()