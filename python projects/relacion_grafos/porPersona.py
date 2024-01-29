import os
import sys
from tkinter import *
from tkinter import messagebox
from lista import canPersonas
from lista import listaDePersonas
from grafo import matrizAyacencia

stileT = {"bg": "#363636", "fg": "#84C9FB", "relief": FLAT}

stileB = {"bg": "#363636", "fg": "#84C9FB", "relief": FLAT, "activebackground":"#121212", "activeforeground" :"#363636"}

stileX = {"bg": "#363636", "fg": "#84C9FB", "relief": FLAT,  "activebackground":"#363636", "activeforeground" :"#84C9FB"}

def ventanaPersona():
    ventanaPer = Tk()
    ventanaPer.title("Busqueda por persona")
    ventanaPer.resizable(0,0)
    ruta_icono = os.path.dirname(os.path.abspath(sys.argv[0]))
    ruta_icono = os.path.join(ruta_icono, "icono.ico")
    if os.path.isfile(ruta_icono):
        ventanaPer.iconbitmap(ruta_icono)
    else:
        print(f"Error: No se encontró el archivo de icono en la ruta: {ruta_icono}")
    ventanaPer.geometry("400x370+500+" + str(int(ventanaPer.winfo_screenheight()/2 - 200)))
    
    frame = Frame(ventanaPer)
    ventanaPer.configure(background="#121212")
    frame.configure(background="#121212")
    frame.pack()
    
    textoCom = Text(frame, width=45, height=15, font=("Cooper Black",10), **stileT)
    textoCom.grid(row=1, column=0, padx=0, pady=15)
    
    person = StringVar(frame)
    
    #--scrooll:
    barra = Scrollbar(frame, command=textoCom.yview)
    barra.grid(row=1, column=1, sticky="nsew", padx=5, pady=15)
    textoCom.config(yscrollcommand=barra.set)
    #----------------------------------------------------------------------------------------------
    relaciones = matrizAyacencia()
    celdas = listaDePersonas()
    
    for i in range(canPersonas()):
        celdas[i] = celdas[i].replace("\n", "")

    def funOption():
        textoCom.configure(state="normal")
        textoCom.delete(1.0, END)
        
        if(person.get() == "Elija una persona" or person.get() == ""):
            textoCom.insert(END, "Por favor elija una persona")
        else:
            compB = []
            compM = []
            compA = []
            compMa = []
            
            indice = celdas.index(person.get())

            for i in range(canPersonas()):
                if(relaciones[i][indice] <= 2 and relaciones[i][indice] != 0 ):
                    compB.append(celdas[i])
                elif(relaciones[i][indice] <= 4 and relaciones[i][indice] != 0 ):
                    compM.append(celdas[i])
                elif(relaciones[i][indice] <= 6 and relaciones[i][indice] != 0 ):
                    compA.append(celdas[i])
                elif(relaciones[i][indice] != 0 ):
                    compMa.append(celdas[i])
        
            if(len(compB) == 0):
                textoCom.insert(END, "No hay compatibilidades bajas\n")
            else:
                textoCom.insert(END, "Compatibilidad Baja:\n")
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
        
    
    person.set("Elija una persona")
    option = OptionMenu(frame, person, *celdas)
    option.config(font=("Cooper Black",12), **stileX, highlightthickness=0)
    
    option.grid(row=0, column=0, pady=10)
    
    botonLista = Button(frame, text="Buscar", font=("Cooper Black", 15), command=funOption, **stileB)
    botonLista.grid(row=2, column=0)
    
    
    textoCom.configure(state="disabled")
    ventanaPer.mainloop()