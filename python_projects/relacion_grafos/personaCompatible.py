import os
import sys
from tkinter import *
from tkinter import messagebox
from grafo import matrizAyacencia
from lista import canPersonas
from lista import listaDePersonas

stileT = {"bg": "#363636", "fg": "#84C9FB", "relief": FLAT}

def matrizVar():
    relaciones = matrizAyacencia()
    valor = [[0 for j in range(2)] for i in range(canPersonas())]

    for i in range(canPersonas()):
        for j in range(i+1, canPersonas()):   
            if(relaciones[i][j] != 0):
                valor[i][0]+=1
                valor[j][0]+=1
            valor[i][1]+=relaciones[i][j]
            valor[j][1]+=relaciones[i][j]
    return valor

def ventanaCompatible():
    #-------------ventana y frame---------------------
    ventanaComp = Tk()
    ventanaComp.title("Compatibilidad")
    ventanaComp.resizable(0,0)
    ruta_icono = os.path.dirname(os.path.abspath(sys.argv[0]))
    ruta_icono = os.path.join(ruta_icono, "icono.ico")
    if os.path.isfile(ruta_icono):
        ventanaComp.iconbitmap(ruta_icono)
    else:
        print(f"Error: No se encontró el archivo de icono en la ruta: {ruta_icono}")
    ventanaComp.geometry("480x500+500+" + str(int(ventanaComp.winfo_screenheight()/2 - 250)))
    
    
    frame = Frame(ventanaComp)
    ventanaComp.configure(background="#121212")
    frame.configure(background="#121212")
    frame.pack()
    #-----------------------------------------------------------------------
    #----------citio de texto-----------------------------------------------
    textoCom = Text(frame, width=55, height=30, font=("Cooper Black",10), **stileT)
    textoCom.grid(row=0, column=0, padx=0, pady=15)
    
    #--scrooll:
    barra = Scrollbar(frame, command=textoCom.yview)
    barra.grid(row=0, column=1, sticky="nsew", padx=5, pady=15)
    textoCom.config(yscrollcommand=barra.set)
    
    valores = matrizVar()
    listapersonas = listaDePersonas() 
    
    #-------------------------------------------------------------------------
    if(len(listapersonas) == 0):
        textoCom.insert(END, "No hay lista por mostrar")
    else:
        for i in range(canPersonas()):
            for j in range(canPersonas()-1):
                if(valores[j][0]*valores[j][1]<valores[j+1][0]*valores[j+1][1]):
                    valores[j], valores[j+1] = valores[j+1], valores[j]
                    listapersonas[j], listapersonas[j+1] = listapersonas[j+1], listapersonas[j]
                    
        textoCom.insert(END, "Cantidad de personas: " + str(canPersonas()))
        textoCom.insert(END, "\n\nOrdenandas de mayor a menor en compatibilidad:\n\n")
        for i in range(canPersonas()):
            textoCom.insert(END, str(i+1) + ". " + listapersonas[i] + "Numero de conexiones: " +str(valores[i][0])+ "\nCantidad de gustos conectados: " + str(valores[i][1])+ "\n\n")
            
    textoCom.configure(state="disabled") 
    #-------------------------------------------------------------------------------------
    ventanaComp.mainloop()