import numpy
import pygame
import random
import time
from datetime import datetime
import os

def colocar_poros(estados_casillas, porosidad, largo_tierra,  casillas_x, casillas_y):
    for i in range(int(int(casillas_x*largo_tierra)*casillas_y*porosidad)):
        x = random.randrange(int(casillas_x*largo_tierra))
        y = random.randrange(casillas_y)
        while estado_casillas[x][y] == 2:
            x = random.randrange(int(casillas_x*largo_tierra))
            y = random.randrange(casillas_y)
        estado_casillas[x][y] = 2
    return estado_casillas

def encontrar_llave(diccionario, valor_buscado):
    for llave, valor in diccionario.items():
        if valor_buscado == valor:
            return llave
    return None

pygame.init()

reloj = pygame.time.Clock()

#densidad de poros
contador_generaciones = 0 #lleva la cuenta de la generaciones que pasaron (inicia en 0)
porosidad = 0.5 #cantidad de poros en proporcion de area de tierra
largo_tierra = 0.6 #porcentaje de ancho de casillas destinada a la tierra
probabilidad_lateral = 0.6 #probabipidad de que el contaminante se mueva lateralmente
probabilidad_tierra_agua = 0.7 #probabilidad de pasar de la tierra al agua
probabilidad_difusion = 0.3
velocidad_agua = 3 # cada n generaciones el contaminante se mueve a la derecha (entero)
concentracion_contaminante = 0.5 #concentracion inicial del contaminante
concentracion_min = 0.1 #concentracion minima del contaminante en el agua
saltos = (concentracion_contaminante-concentracion_min)/5 # saltados entre concentraciones


#colores--------------------------
colores = {
    "tierra" : (78,59,49),
    "poro": (43, 128, 0), 
    "blanco":(255,255,255),
    "agua": (0, 20, 200),
    "contaminante" : (221,215,0),
    "negro" : (0,0,0)
}

#tipos casillas---------------------
estados = {
    "tierra" : 1,
    "poro": 2,
    "agua": 3,
    "contaminante" : 4
}

#creacion de ventana
dimension_cuadricula = 20
alto = 600 + dimension_cuadricula
ancho = 1200

casillas_x = ancho//dimension_cuadricula
casillas_y = (alto//dimension_cuadricula)-1

ventana = pygame.display.set_mode((ancho, alto))
ventana.fill(colores["blanco"])

#titulo para la ventana
pygame.display.set_caption("Difusion")

#icono para la ventana
try: 
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_imagen_icono = os.path.join(directorio_actual, "icono_difusion.png")
    icono = pygame.image.load(ruta_imagen_icono)
    pygame.display.set_icon(icono)
except:
    print("No se ha podido cargar la imagen")

#otras variables
gameOver = False
pausa = True
velocidad_generacion = 1
fuente = pygame.font.SysFont(name="Arial", size=14, bold=False, italic=False)

#creacion cuadriculas---------------------------------------
estado_casillas = numpy.zeros((casillas_x, casillas_y))
concentraciones_agua = numpy.zeros((casillas_x, casillas_y))

for x in range(int(casillas_x*largo_tierra)):
    for y in range(casillas_y):
        estado_casillas[x][y] = estados["tierra"]

for x in range(int(casillas_x*largo_tierra), casillas_x):
    for y in range(casillas_y):
        estado_casillas[x][y] = estados["agua"]
        
estado_casillas = colocar_poros(estado_casillas, porosidad, largo_tierra, casillas_x, casillas_y)

instante = datetime.now()

#bucle del juego
while not gameOver:
    # eventos------------------------------------
    for evento in pygame.event.get():
            
        # terminar el juego-----------------------
        if evento.type == pygame.QUIT:
            gameOver = True
            
        # evento de presionar teclas---------------
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                pausa = not pausa
                
            if evento.key == pygame.K_RIGHT:
                if (velocidad_generacion <= 0.05):
                    velocidad_generacion = 0
                else:
                    velocidad_generacion -= 0.05

            if evento.key == pygame.K_LEFT:
                if (velocidad_generacion >= 1):
                    velocidad_generacion = 1
                else:
                    velocidad_generacion += 0.05

        #evento de mause--------------------------
        mouseClick = pygame.mouse.get_pressed()
        if (mouseClick[0]or mouseClick[2]):
            posx, posy = pygame.mouse.get_pos()
            x = int(numpy.floor(posx/dimension_cuadricula))
            if(estado_casillas[x][0] == 2):
                estado_casillas[x][0] = 4
            
            
                        
        
    if (not pausa and (datetime.now()-instante).total_seconds() >= velocidad_generacion):
        
        #reglas para el limite tierra - agua
        for i in range(casillas_y):
            if(estado_casillas[int(casillas_x*largo_tierra)-1][i] == estados["contaminante"] and estado_casillas[int(casillas_x*largo_tierra)][i] == estados["agua"]):
                if(random.random() < probabilidad_tierra_agua):
                    estado_casillas[int(casillas_x*largo_tierra)-1][i] = estados["poro"]
                    estado_casillas[int(casillas_x*largo_tierra)][i] = estados["contaminante"]
                    concentraciones_agua[int(casillas_x*largo_tierra)][i] = concentracion_contaminante
        
        #reglas para el contaminante en el suelo
        contador_generaciones += 1
        instante = datetime.now()
        for y in range(casillas_y-1, -1, -1):
            for x in range(int(casillas_x*largo_tierra)):
                if(estado_casillas[x][y]==estados["contaminante"] and (y+1)<casillas_y):
                    if(estado_casillas[x][y+1]==estados["poro"]):
                        estado_casillas[x][y]=estados["poro"]
                        estado_casillas[x][y+1]=estados["contaminante"]
                    
                    elif(estado_casillas[x-1][y+1] == estados["poro"] or estado_casillas[x+1][y+1] == estados["poro"]):
                        list_temp = []
                        if(estado_casillas[x-1][y+1] == estados["poro"]):
                            list_temp.append(x-1)
                        if(estado_casillas[x+1][y+1] == estados["poro"]):
                            list_temp.append(x+1)
                        
                        estado_casillas[x][y] = estados["poro"]
                        estado_casillas[random.choice(list_temp)][y+1] = estados["contaminante"]
                        
                    elif(estado_casillas[x-1][y] == estados["poro"] or estado_casillas[x+1][y] == estados["poro"]):
                        list_temp = []
                        if(estado_casillas[x-1][y] == estados["poro"]):
                            list_temp.append(x-1)
                        if(estado_casillas[x+1][y] == estados["poro"]):
                            list_temp.append(x+1)
                            
                        if(probabilidad_lateral > random.random()):
                            estado_casillas[x][y] = estados["poro"]
                            estado_casillas[random.choice(list_temp)][y] = estados["contaminante"]
                    
                elif(estado_casillas[x][y] == estados["contaminante"] and (estado_casillas[x-1][y] == estados["poro"] or estado_casillas[x+1][y] == estados["poro"])):
                        list_temp = []
                        if(estado_casillas[x-1][y] == estados["poro"]):
                            list_temp.append(x-1)
                        if(estado_casillas[x+1][y] == estados["poro"]):
                            list_temp.append(x+1)
                        
                        if(probabilidad_lateral > random.random()):
                            estado_casillas[x][y] = estados["poro"]
                            estado_casillas[random.choice(list_temp)][y] = estados["contaminante"]
                            
        
        #movimiento lateral en el agua
        if(contador_generaciones%velocidad_agua == 0):
            for y in range(casillas_y):
                for x in range(casillas_x-1, int(casillas_x*largo_tierra)-1, -1):
                    if(estado_casillas[x][y] == estados["contaminante"]):
                        if( x+1 >= casillas_x):
                            estado_casillas[x][y] = estados["agua"]
                            concentraciones_agua[x][y] = 0
                        else:
                            estado_casillas[x][y] = estados["agua"]
                            estado_casillas[x+1][y] = estados["contaminante"]
                            concentraciones_agua[x+1][y] = concentraciones_agua[x][y]
                            concentraciones_agua[x][y] = 0
                            
                            
        #reglas para la difusion del contaminante en el agua
        temp_estados = numpy.copy(estado_casillas)
        temp_concentraciones = numpy.copy(concentraciones_agua)
        for y in range(casillas_y):
            for x in range(int(casillas_x*largo_tierra) ,casillas_x):
                if(estado_casillas[x][y] == estados["contaminante"]):
                    if(x-1> int(casillas_x*largo_tierra) and random.random() < probabilidad_difusion and temp_concentraciones[x][y] > concentracion_min):
                        temp_estados[x-1][y] = estados["contaminante"]
                        temp_concentraciones[x][y] = max(temp_concentraciones[x][y]-saltos, concentracion_min)
                        if (temp_concentraciones[x-1][y]==0):
                            temp_concentraciones[x-1][y] = concentracion_min
                        else:
                            temp_concentraciones[x-1][y] = min(temp_concentraciones[x-1][y]+saltos, concentracion_contaminante)
                            
                            
                    if(y+1 < casillas_y and random.random() < probabilidad_difusion and temp_concentraciones[x][y] > concentracion_min):
                        temp_estados[x][y+1] = estados["contaminante"]
                        temp_concentraciones[x][y] = max(temp_concentraciones[x][y]-saltos, concentracion_min)
                        if (temp_concentraciones[x][y+1]==0):
                            temp_concentraciones[x][y+1] = concentracion_min
                        else:
                            temp_concentraciones[x][y+1] = min(temp_concentraciones[x][y+1]+saltos, concentracion_contaminante)
                            
                    if(y-1 >= 0 and random.random() < probabilidad_difusion and temp_concentraciones[x][y] > concentracion_min):
                        temp_estados[x][y-1] = estados["contaminante"]
                        temp_concentraciones[x][y] = max(temp_concentraciones[x][y]-saltos, concentracion_min)
                        if (temp_concentraciones[x][y-1]==0):
                            temp_concentraciones[x][y-1] = concentracion_min
                        else:
                            temp_concentraciones[x][y-1] = min(temp_concentraciones[x][y-1]+saltos, concentracion_contaminante)
                            
                    if(x+1< casillas_x and random.random() < probabilidad_difusion and temp_concentraciones[x][y] > concentracion_min):
                        temp_estados[x+1][y] = estados["contaminante"]
                        temp_concentraciones[x][y] = max(temp_concentraciones[x][y]-saltos, concentracion_min)
                        if (temp_concentraciones[x+1][y]==0):
                            temp_concentraciones[x+1][y] = concentracion_min
                        else:
                            temp_concentraciones[x+1][y] = min(temp_concentraciones[x+1][y]+saltos, concentracion_contaminante)
        
        estado_casillas = numpy.copy(temp_estados)
        concentraciones_agua = numpy.copy(temp_concentraciones)
        
    ventana.fill(colores["blanco"])
    
    # dibujar la cuadricula----------------------
    for x in range(casillas_x):
        for y in range(casillas_y):
            polygono = [(x*dimension_cuadricula, (y+1)*dimension_cuadricula),
                        ((x+1)*dimension_cuadricula, (y+1)*dimension_cuadricula),
                        ((x+1)*dimension_cuadricula, (y+2)*dimension_cuadricula),
                        (x*dimension_cuadricula, (y+2)*dimension_cuadricula)]
            
            if(x<=int(casillas_x*largo_tierra)):
                llave = encontrar_llave(estados, estado_casillas[x][y])
                pygame.draw.polygon(ventana, colores[llave], polygono, 0)
            else:
                if(estado_casillas[x][y] == estados["contaminante"]):
                    c = concentraciones_agua[x][y]
                    c_min = concentracion_min
                    c_max = concentracion_contaminante
                    R =int(221*(c-c_min)/(c_max - c_min))
                    G = int(35*(c-c_min)/(c_max - c_min) + 150)
                    B = int((200*(c_min-c))/(c_max-c_min) + 200)
                    
                    pygame.draw.polygon(ventana,(R, G, B), polygono, 0)
                else:
                    pygame.draw.polygon(ventana,colores["agua"], polygono, 0)
            
                
            
                
    #----------------------------------------------------------------------------
    #----------------------------------------------------------------------------      
    #-------------------------texto superior-------------------------------------
    #----------------------------------------------------------------------------
    #----------------------------------------------------------------------------
    
    text_colocar = "" #variable tipo estring, modificar esta variable dependiendo el texto que quieran colocar
    texto_colocar = "Estado: " + ("Pausado" if pausa else "Ejecutandose") # ejemplo
    
    
    texto = fuente.render(texto_colocar, True, colores["negro"]) #genera la fuente apartir del texto y su color (recomendado no cambiar)
    
    ventana.blit(texto, (1, 3))#este coloca el texto en la posicion correcta en la ventana (recomendado no cambiar posicion)
    
    #----------------------------------------------------------------------------
    #----------------------------------------------------------------------------      
    #----------------------------------------------------------------------------
    #----------------------------------------------------------------------------
    #----------------------------------------------------------------------------
    
    pygame.display.flip()
    reloj.tick(30)
    
pygame.quit()
