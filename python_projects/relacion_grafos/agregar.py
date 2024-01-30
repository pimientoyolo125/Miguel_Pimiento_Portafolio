import os
import sys
from tkinter import *
from tkinter import messagebox

stileB = {"bg": "#363636", "fg": "#84C9FB", "relief": FLAT, "activebackground":"#121212", "activeforeground" :"#363636"}

stileL = {"bg": "#121212", "fg": "#84C9FB", "relief": FLAT}

stileE = {"bg": "#363636", "fg": "#84C9FB", "relief": FLAT, "justify": CENTER}

stileC = {"bg": "#121212", "fg": "#3BACFE", "relief": FLAT, "activebackground":"#121212", "activeforeground" :"#363636"}

stileR = {"bg": "#121212", "fg": "#3BACFE", "relief": FLAT, "activebackground":"#121212", "activeforeground" :"#363636"}
def ventanaAgregar():
    
    #------------ventana y el frame
    ventanaAgre = Tk()
    ventanaAgre.title("Agregar")
    ventanaAgre.resizable(0,0)
    ruta_icono = os.path.dirname(os.path.abspath(sys.argv[0]))
    ruta_icono = os.path.join(ruta_icono, "icono.ico")
    if os.path.isfile(ruta_icono):
        ventanaAgre.iconbitmap(ruta_icono)
    else:
        print(f"Error: No se encontró el archivo de icono en la ruta: {ruta_icono}")
    ventanaAgre.geometry("700x350+500+" + str(int(ventanaAgre.winfo_screenheight()/2 - 175)))
    
    
    frame = Frame(ventanaAgre)
    ventanaAgre.configure(background="#121212")
    frame.configure(background="#121212")
    frame.pack()
    #---------------------Variables para recoleccion de datos------------------------
    #Musica:
    regueton = StringVar(ventanaAgre)
    rock = StringVar(ventanaAgre)
    hip = StringVar(ventanaAgre)
    popular = StringVar(ventanaAgre)
    electronica = StringVar(ventanaAgre)
    k = StringVar(ventanaAgre)
    
    #deportes:
    futbol = StringVar(ventanaAgre)
    baloncesto = StringVar(ventanaAgre)
    tenis = StringVar(ventanaAgre)
    pipon = StringVar(ventanaAgre)
    combate = StringVar(ventanaAgre)
    ajedrez = StringVar(ventanaAgre)
    gimnasio = StringVar(ventanaAgre)
    voleybol = StringVar(ventanaAgre)
    
    #hobbies:
    hacer = StringVar(ventanaAgre)
    jugar = StringVar(ventanaAgre)
    internet = StringVar(ventanaAgre)
    television = StringVar(ventanaAgre)
    cine = StringVar(ventanaAgre)
    series = StringVar(ventanaAgre)
    anime = StringVar(ventanaAgre)
    estudiar = StringVar(ventanaAgre)
    parchar = StringVar(ventanaAgre)
    
    
    selecArea = IntVar(ventanaAgre)
    Area = ["\n", "Ciencias Humanas\n\n", "Ingenieria\n\n", "Ciencias Aplicadas\n\n", "Musica\n\n", "Artes\n\n"]
    #--------------------------------------------------------------------------------
    
    
    #------------Funciones---------------------------------------------------
    def crearArchivo(texto):
        try:
            archivo = open("file.txt", "a")
            archivo.write(texto)
            archivo.close()
            return True
        except Exception as exc:
            messagebox.showwarning("Advertencia", "Ha ocurrido un error al crear o escribir el archivo")
            return False
            
    
    def cancelar():
        ventanaAgre.destroy()
    
    def funAñadir():
        print(regueton.get())
        name = nombre.get()
        name.strip()
        if(name == ""):
            messagebox.showwarning("Advertencia", "Campos incompletos:\nEl campo del nombre no puede ir vacio")
        else:
            texto = ""
            texto += (name + "\n" + regueton.get() + rock.get() +hip.get() +popular.get() +electronica.get() +k.get() + futbol.get() +
                    baloncesto.get() + tenis.get() + pipon.get() +combate.get() + ajedrez.get() +gimnasio.get() + voleybol.get() + 
                    hacer.get() +jugar.get() + internet.get() + television.get() + cine.get() + series.get() + anime.get() + 
                    estudiar.get() + parchar.get() + Area[selecArea.get()])
            print(texto)
            if(crearArchivo(texto)):
                messagebox.showinfo("Mensaje", name+ " añadido con exito")
            ventanaAgre.destroy()
    #-------------------------------------------------------------------
    #labels
    #-------------------------------------------------------------------------------------------------------------
    Label(frame, text="Nombre:", font=("Cooper Black",10), **stileL).grid(row=0, column=1, padx = 10, pady = 5)
    Label(frame, text="Gustos musicales:", font=("Cooper Black",10), **stileL).grid(row=1, column=0, padx = 10, pady = 5)
    Label(frame, text="Gustos en deportes:", font=("Cooper Black",10), **stileL).grid(row=1, column=1, padx = 10, pady = 5)
    Label(frame, text="Hobbies:", font=("Cooper Black",10), **stileL).grid(row=1, column=2, padx = 10, pady = 5)
    Label(frame, text="Area que le gusta:", font=("Cooper Black",10), **stileL).grid(row=1, column=3, padx = 10, pady = 5)
    #---------------------------------------------------------------------------------------------------------------
    
    ## entrada de nombre
    nombre = Entry(frame, font=("Cooper Black",10), **stileE)
    nombre.grid(row=0, column=2)
    
    ##Musica
    #-----------------------------------------------------------------------------------------------------
    Checkbutton(frame, text="Regueton", font=("Cooper Black", 10), variable= regueton,onvalue="Regueton\n", offvalue="", **stileC).grid(row=2, column=0, sticky='w')
    Checkbutton(frame, text="Rock", font=("Cooper Black",10),variable= rock,onvalue="Rock\n", offvalue="",**stileC).grid(row=3, column=0, sticky='w')
    Checkbutton(frame, text="Hip Hop", font=("Cooper Black",10),variable= hip,onvalue="Hip Hop\n", offvalue="",**stileC).grid(row=4, column=0, sticky='w')
    Checkbutton(frame, text="Musica Popular", font=("Cooper Black",10),variable=popular,onvalue="Musica Popular\n", offvalue="",**stileC).grid(row=5, column=0, sticky='w')
    Checkbutton(frame, text="Electronica", font=("Cooper Black",10),variable=electronica,onvalue="Electronica\n", offvalue="",**stileC).grid(row=6, column=0, sticky='w')
    Checkbutton(frame, text="K-pop", font=("Cooper Black",10),variable= k,onvalue="K-pop\n", offvalue="",**stileC).grid(row=7, column=0, sticky='w')
    #------------------------------------------------------------------------------------------------------------
    
    ##Deportes
    #-----------------------------------------------------------------------------------------------------------
    Checkbutton(frame, text="Futbol", font=("Cooper Black", 10),variable= futbol,onvalue="Futbol\n", offvalue="", **stileC).grid(row=2, column=1, sticky='w')
    Checkbutton(frame, text="Baloncesto", font=("Cooper Black",10),variable= baloncesto,onvalue="Baloncesto\n", offvalue="", **stileC).grid(row=3, column=1, sticky='w')
    Checkbutton(frame, text="Tenis", font=("Cooper Black",10),variable= tenis,onvalue="Tenis\n", offvalue="", **stileC).grid(row=4, column=1, sticky='w')
    Checkbutton(frame, text="Pinpon", font=("Cooper Black",10),variable= pipon,onvalue="Pinpon\n", offvalue="", **stileC).grid(row=5, column=1, sticky='w')
    Checkbutton(frame, text="Deportes de combate", font=("Cooper Black",10),variable= combate,onvalue="Deportes de Combate\n", offvalue="", **stileC).grid(row=6, column=1, sticky='w')
    Checkbutton(frame, text="Ajedrez", font=("Cooper Black",10),variable= ajedrez,onvalue="Ajedrez\n", offvalue="", **stileC).grid(row=7, column=1, sticky='w')
    Checkbutton(frame, text="Gimnasio", font=("Cooper Black",10),variable= gimnasio,onvalue="Gimnasio\n", offvalue="", **stileC).grid(row=8, column=1, sticky='w')
    Checkbutton(frame, text="Voleybol", font=("Cooper Black",10),variable= voleybol,onvalue="Voleybol\n", offvalue="", **stileC).grid(row=9, column=1, sticky='w')
    #-----------------------------------------------------------------------------------------------------------
    
    ##Hobbies
    #-----------------------------------------------------------------------------------------------------------------------
    Checkbutton(frame, text="Hacer Deporte", font=("Cooper Black", 10),variable= hacer,onvalue="Hacer Deporte\n", offvalue="", **stileC).grid(row=2, column=2, sticky='w')
    Checkbutton(frame, text="Jugar Videojuegos", font=("Cooper Black",10),variable= jugar,onvalue="Jugar Videojuegos\n", offvalue="", **stileC).grid(row=3, column=2, sticky='w')
    Checkbutton(frame, text="Internet", font=("Cooper Black",10),variable= internet,onvalue="Internet\n", offvalue="", **stileC).grid(row=4, column=2, sticky='w')
    Checkbutton(frame, text="Television", font=("Cooper Black",10),variable= television,onvalue="Television\n", offvalue="", **stileC).grid(row=5, column=2, sticky='w')
    Checkbutton(frame, text="Cine", font=("Cooper Black",10),variable= cine,onvalue="Cine\n", offvalue="", **stileC).grid(row=6, column=2, sticky='w')
    Checkbutton(frame, text="Series", font=("Cooper Black",10),variable= series,onvalue="Series\n", offvalue="", **stileC).grid(row=7, column=2, sticky='w')
    Checkbutton(frame, text="Anime", font=("Cooper Black",10),variable= anime,onvalue="Anime\n", offvalue="", **stileC).grid(row=8, column=2, sticky='w')
    Checkbutton(frame, text="Estudiar", font=("Cooper Black",10),variable= estudiar,onvalue="Estudiar\n", offvalue="", **stileC).grid(row=9, column=2, sticky='w')
    Checkbutton(frame, text="Parchar", font=("Cooper Black",10),variable= parchar,onvalue="Parchar\n", offvalue="", **stileC).grid(row=10, column=2, sticky='w')
    #--------------------------------------------------------------------------------------------------------------------------------------
    
    ##Areas que le gusta
    #--------------------------------------------------------------------------------------------------------------------------------
    R1 = Radiobutton(frame, text="Ciencias Humanas", font=("Cooper Black", 10), variable=selecArea, value=1, **stileR)
    R1.grid(row=2, column=3, sticky='w')
    R1.config(value=1)
    R2 =Radiobutton(frame, text="Ingenieria", font=("Cooper Black", 10),variable=selecArea, value=2, **stileR)
    R2.grid(row=3, column=3, sticky='w')
    R3 = Radiobutton(frame, text="Ciencias Aplicadas", font=("Cooper Black", 10),variable=selecArea, value=3, **stileR)
    R3.grid(row=4, column=3, sticky='w')
    R4 = Radiobutton(frame, text="Musica", font=("Cooper Black", 10),variable=selecArea, value=4, **stileR)
    R4.grid(row=5, column=3, sticky='w')
    R5 = Radiobutton(frame, text="Artes", font=("Cooper Black", 10),variable=selecArea, value=5, **stileR)
    R5.grid(row=6, column=3, sticky='w')
    R = Radiobutton(frame, text="Ninguna de las anteriores", font=("Cooper Black", 10), variable=selecArea, value=0, **stileR)
    R.grid(row=7, column=3, sticky='w')
    R.select()
    #----------------------------------------------------------------------------------------------------------------------------------

    ##Boton para cancelar------------------------------------------------------------------
    botonCancel = Button(frame, text="Cancelar", font=("Cooper Black",12), command=cancelar, **stileB)
    botonCancel.grid(row=11, column=0, pady=10)
    #---------------------------------------------------------------------------------------
    
    #--------------boton agregar-------------------------------------------------------
    
    ##--boton:
    botonAg = Button(frame, text="Agregar", font=("Cooper Black",12), command=funAñadir, **stileB)
    botonAg.grid(row=11, column=3, pady=10)
    
    
    ventanaAgre.mainloop()