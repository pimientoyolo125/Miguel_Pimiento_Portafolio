import os
import sys
from tkinter import *
from tkinter import messagebox
import tkinter
from lista import canPersonas
from lista import ventanaListaEnumerada
import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from listas import nodo
from PIL import Image, ImageTk 
import PIL.Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

stileB = {"bg": "#363636", "fg": "#84C9FB", "relief": FLAT, "activebackground":"#121212", "activeforeground" :"#363636"}

def venList():
    ventanaListaEnumerada()

def listaPersonas():
    try:
        ruta_file = os.path.dirname(os.path.abspath(sys.argv[0]))
        ruta_file = os.path.join(ruta_file, "file.txt")
        archivo = open(ruta_file, "r")
        lineas = archivo.readlines()
        archivo.close()
        bandera = True
        lista = []
        for linea in lineas:
            if(bandera):
                lista.append(linea)
                bandera = False
            else:
                if(linea == "\n"):
                    bandera = True
    except:
        messagebox.showwarning("Advertencia", "Error: no se puede abrir el archivo o no existe")
        ventanaGraf.destroy()
        
    return lista
    

def similitudes(array1, array2):
    contador = 0
    bandera = True
    for pal in array1[1:]:
        if(pal in (array2[1:])):
            contador +=1
    return contador

def matrizAyacencia():
    try:
        ruta_file = os.path.dirname(os.path.abspath(sys.argv[0]))
        ruta_file = os.path.join(ruta_file, "file.txt")
        archivo = open(ruta_file, "r")
        lineas = archivo.readlines()
        archivo.close()
    except:
        messagebox.showwarning("Alerta", "No se puede construir el  grafo")
        ventanaGraf.destroy()
    
    personas = []
    añadir = []
    for linea in lineas:
        if(linea != "\n"):
            añadir.append(linea)
        else:
            personas.append(list(añadir))
            añadir.clear()
            
    Matriz = []
    aux = []
    for i in range(canPersonas()):
        aux.clear()
        for j in range(canPersonas()):
            if(j==i):
                aux.append(0)
            else:
                aux.append(similitudes(personas[i], personas[j]))
        Matriz.append(list(aux))
        
    return Matriz

def imagenGrafo():
    Matriz = matrizAyacencia()
    personas = listaPersonas()
    grafo = nx.Graph()
    nodos = []
    for fila in range(canPersonas()):
        nodos.append(nodo(str(personas[fila]), int(fila+1)))
    
    for fila in range(canPersonas()):
        for col in range(canPersonas()):
            if(Matriz[fila][col] != 0):
                grafo.add_edge(nodos[fila], nodos[col], weight=Matriz[fila][col])

    plt.subplot()
    pos = nx.layout.circular_layout(grafo)
    c = ["#FF0000","#FFE400","#428A02","#7800FF"]  
    colores = []
    for (u,v) in grafo.edges:
            if(grafo[u][v]['weight'] == 1 or grafo[u][v]['weight']==2):
                colores.append("#FF0000")
            elif(grafo[u][v]['weight'] == 3 or grafo[u][v]['weight'] == 4):
                colores.append("#FFE400")
            elif(grafo[u][v]['weight'] == 5 or grafo[u][v]['weight'] == 6):
                colores.append("#428A02")
            elif(grafo[u][v]['weight'] >= 7):
                colores.append( "#7800FF")
            
    nx.draw(grafo,pos=pos,edge_color=colores,edge_cmap=plt.cm.rainbow)
    
    nx.draw_networkx_labels(grafo, pos)
    
    plt.title("Relaciones entre personas: ")

    divider = make_axes_locatable(plt.gca())
    ax_cb = divider.new_horizontal(size="5%", pad=0.05)

    cmap = mpl.colors.ListedColormap(c)
    bounds = [0, 3, 5, 7]
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

    pesosw = list([grafo[u][v]['weight'] for (u, v) in grafo.edges()])
    norm = mpl.colors.Normalize(vmin=1, vmax=8)
    cb1 = mpl.colorbar.ColorbarBase(ax=ax_cb, cmap=cmap, norm=norm, orientation='vertical')
    plt.gcf().add_axes(ax_cb)
    
    plt.savefig("grahp.png")
    
    plt.close()
    
    
def ventanaGraf():
    ventanaGrafo = tkinter.Tk()
    ventanaGrafo.title("Grafo")
    ventanaGrafo.resizable(0,0)
    ruta_icono = os.path.dirname(os.path.abspath(sys.argv[0]))
    ruta_icono = os.path.join(ruta_icono, "icono.ico")
    if os.path.isfile(ruta_icono):
        ventanaGrafo.iconbitmap(ruta_icono)
    else:
        print(f"Error: No se encontró el archivo de icono en la ruta: {ruta_icono}")
    ventanaGrafo.geometry("700x700+450+" + str(int(ventanaGrafo.winfo_screenheight()/2 - 350)))
    
    frameMy = tkinter.Frame(ventanaGrafo)
    ventanaGrafo.configure(background="#121212")
    frameMy.configure(background="#121212")
    frameMy.pack()
    #--------------------------------------------------------------------------
    #----label para imagen------------------------------------------------------
    
    ruta_image = os.path.dirname(os.path.abspath(sys.argv[0]))
    ruta_image = os.path.join(ruta_image, "grahp.png")
    miimage = Image.open(ruta_image)
    photo = ImageTk.PhotoImage(miimage, master=frameMy)
    ventanaGrafo.geometry(str(photo.width()+20)+ "x" + str(photo.height()+80) + "+450+" + str(int(ventanaGrafo.winfo_screenheight()/2 - (photo.height()+80)/2)))
    label = tkinter.Label(frameMy, image=photo, **stileB)
    label.grid(row=0, column=0, padx=10, pady=10)
    
    botonLista = Button(frameMy, text="Lista Enumerada", font=("Cooper Black", 18), command=venList, **stileB)
    botonLista.grid(row=1, column=0)
    
    ventanaGrafo.mainloop()
    