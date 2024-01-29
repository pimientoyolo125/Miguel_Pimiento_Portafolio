import os
import sys
from tkinter import *
from tkinter import messagebox

stileB = {"bg": "#363636", "relief": FLAT, "activebackground":"#121212"}

stileT = {"bg": "#363636", "fg": "#84C9FB", "relief": FLAT}

def canPersonas():
    try:
        ruta_file = os.path.dirname(os.path.abspath(sys.argv[0]))
        ruta_file = os.path.join(ruta_file, "file.txt")
        archivo = open(ruta_file, "r")
        lineas = archivo.readlines()
        archivo.close()
    except:
        pass
    count = 0
    for i in lineas:
        if(i == "\n"):
            count +=1
    return count

def listaDePersonas():
    listaPersonas = []
    try:
        ruta_file = os.path.dirname(os.path.abspath(sys.argv[0]))
        ruta_file = os.path.join(ruta_file, "file.txt")
        archivo = open(ruta_file, "r")
        lineas = archivo.readlines()
        archivo.close()
        count = 1
        bandera = True
        for linea in lineas:
            if(bandera):
                listaPersonas.append(linea)
                count+=1
                bandera = False
            else:
                if(linea == "\n"):
                    bandera = True
    except:
        pass
    return listaPersonas
    
def ventanaLista():
    #-------------ventana y frame---------------------
    ventanalist = Tk()
    ventanalist.title("Lista")
    ventanalist.resizable(0,0)
    ruta_icono = os.path.dirname(os.path.abspath(sys.argv[0]))
    ruta_icono = os.path.join(ruta_icono, "icono.ico")
    if os.path.isfile(ruta_icono):
        ventanalist.iconbitmap(ruta_icono)
    else:
        print(f"Error: No se encontró el archivo de icono en la ruta: {ruta_icono}")
    ventanalist.geometry("400x510+500+" + str(int(ventanalist.winfo_screenheight()/2 - 250)))
    
    
    frame = Frame(ventanalist)
    ventanalist.configure(background="#121212")
    frame.configure(background="#121212")
    frame.pack()
    #-----------------------------------------------------------------------
    #----------citio de texto-----------------------------------------------
    textoCom = Text(frame, width=45, height=30, font=("Cooper Black",10), **stileT)
    textoCom.grid(row=0, column=0, padx=0, pady=25)
    
    #--scrooll:
    barra = Scrollbar(frame, command=textoCom.yview, **stileB)
    barra.grid(row=0, column=1, padx = 5,pady=10,  sticky="nsew")
    textoCom.config(yscrollcommand=barra.set)
    #-------------------------------------------------------------------------
    
    #---------------leer archivo----------------------------------------------
    try:
        ruta_file = os.path.dirname(os.path.abspath(sys.argv[0]))
        ruta_file = os.path.join(ruta_file, "file.txt")
        archivo = open(ruta_file, "r")
        texto = archivo.read()
        archivo.close()
        textoCom.insert(INSERT, "Cantidad de personas: " + str(canPersonas()) + "\n\n")
        textoCom.insert(INSERT, texto)
        textoCom.configure(state="disabled")
    except:
        textoCom.insert(INSERT, "El archivo esta vacio")
        textoCom.configure(state="disabled")
    
    #--------------------------------------------------------------------------------------
    ventanalist.mainloop()
    
def ventanaListaEnumerada():
    #-------------ventana y frame---------------------
    ventanalist = Tk()
    ventanalist.title("Lista Enumerada")
    ventanalist.resizable(0,0)
    ruta_icono = os.path.dirname(os.path.abspath(sys.argv[0]))
    ruta_icono = os.path.join(ruta_icono, "icono.ico")
    if os.path.isfile(ruta_icono):
        ventanalist.iconbitmap(ruta_icono)
    else:
        print(f"Error: No se encontró el archivo de icono en la ruta: {ruta_icono}")
    ventanalist.geometry("400x510+900+" + str(int(ventanalist.winfo_screenheight()/2 - 250)))
    
    
    frame = Frame(ventanalist)
    ventanalist.configure(background="#121212")
    frame.configure(background="#121212")
    frame.pack()
    #-----------------------------------------------------------------------
    #----------citio de texto-----------------------------------------------
    textoCom = Text(frame, width=45, height=30, font=("Cooper Black",10), **stileT)
    textoCom.grid(row=0, column=0, padx=0, pady=25)
    
    #--scrooll:
    barra = Scrollbar(frame, command=textoCom.yview, **stileB)
    barra.grid(row=0, column=1, padx=5,pady=10, sticky="nsew")
    textoCom.config(yscrollcommand=barra.set)
    #-------------------------------------------------------------------------
    
    #---------------leer archivo----------------------------------------------
    try:
        ruta_file = os.path.dirname(os.path.abspath(sys.argv[0]))
        ruta_file = os.path.join(ruta_file, "file.txt")
        archivo = open(ruta_file, "r")
        lineas = archivo.readlines()
        archivo.close()
        textoCom.insert(INSERT, "Cantidad de personas: " + str(canPersonas()) + "\n\n")
        count = 1
        bandera = True
        for linea in lineas:
            if(bandera):
                textoCom.insert(END, str(count) + "." +linea)
                count+=1
                bandera = False
            else:
                if(linea == "\n"):
                    bandera = True
                
        textoCom.configure(state="disabled")
    except:
        textoCom.insert(INSERT, "El archivo esta vacio")
        textoCom.configure(state="disabled")
    
    #--------------------------------------------------------------------------------------
    ventanalist.mainloop()