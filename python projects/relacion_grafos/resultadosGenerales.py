import os
import sys
from tkinter import *
from tkinter import messagebox
from lista import canPersonas
from lista import listaDePersonas
from grafo import matrizAyacencia

stileB = {"bg": "#363636", "relief": FLAT, "activebackground":"#121212"}

stileT = {"bg": "#363636", "fg": "#84C9FB", "relief": FLAT}

def ventanaGeneral():
    ventanaGen = Tk()
    ventanaGen.title("Resultados generales")
    ventanaGen.resizable(0,0)
    ruta_icono = os.path.dirname(os.path.abspath(sys.argv[0]))
    ruta_icono = os.path.join(ruta_icono, "icono.ico")
    if os.path.isfile(ruta_icono):
        ventanaGen.iconbitmap(ruta_icono)
    else:
        print(f"Error: No se encontró el archivo de icono en la ruta: {ruta_icono}")
    ventanaGen.geometry("420x480+500+" + str(int(ventanaGen.winfo_screenheight()/2 - 250)))
    
    
    frame = Frame(ventanaGen)
    ventanaGen.configure(background="#121212")
    frame.configure(background="#121212")
    frame.pack()
    #-----------------------------------------------------------------------
    #----------citio de texto-----------------------------------------------
    textoCom = Text(frame, width=45, height=30, font=("Cooper Black",10), **stileT)
    textoCom.grid(row=0, column=0, padx=10, pady=15)
    
    #--scrooll:
    barra = Scrollbar(frame, command=textoCom.yview, **stileB)
    barra.grid(row=0, column=1, sticky="nsew", padx=5, pady=15)
    textoCom.config(yscrollcommand=barra.set)
    #----------------------------------------------------------------------------------------------
    relaciones = matrizAyacencia()
    celdas = listaDePersonas()
    
    for i in range(canPersonas()):
        celdas[i] = celdas[i].replace("\n", "")
    
    compB = []
    compM = []
    compA = []
    compMa = []

    for i in range(canPersonas()):
        for j in range(i+1, canPersonas()):   
            if(relaciones[i][j] <= 2 and relaciones[i][j] != 0 ):
                compB.append(celdas[i] + "─" + celdas[j])
            elif(relaciones[i][j] <= 4 and relaciones[i][j] != 0 ):
                compM.append(celdas[i] + "─" + celdas[j])
            elif(relaciones[i][j] <= 6 and relaciones[i][j] != 0 ):
                compA.append(celdas[i] + "─" +celdas[j])
            elif(relaciones[i][j] != 0 ):
                compMa.append(celdas[i] + "─" +celdas[j])

    if(len(compB) == 0):
        textoCom.insert(END, "\nNo hay compatibilidades bajas\n")
    else:
        textoCom.insert(END, "\nCompatibilidad Baja:\n")
        for i in range(len(compB)):
            textoCom.insert(END, "* " + compB[i] + "\n")
            
    if(len(compM) == 0):
        textoCom.insert(END, "\nNo hay compatibilidades medias\n")
    else:
        textoCom.insert(END, "\nCompatibilidad Media:\n")
        for i in range(len(compM)):
            textoCom.insert(END, "* " + compM[i] + "\n")
    
    if(len(compA) == 0):
        textoCom.insert(END, "\nNo hay compatibilidades altas\n")
    else:
        textoCom.insert(END, "\nCompatibilidad Alta:\n")
        for i in range(len(compA)):
            textoCom.insert(END, "* " + compA[i] + "\n")
    
    if(len(compMa) == 0):
        textoCom.insert(END, "\nNo hay compatibilidades muy altas\n")
    else:
        textoCom.insert(END, "\nCompatibilidad Muy Alta:\n")
        for i in range(len(compMa)):
            textoCom.insert(END, "* " + compMa[i] + "\n")
    
    textoCom.configure(state="disabled")
    #--------------------------------------------------------------------------------------------
    
    ventanaGen.mainloop()