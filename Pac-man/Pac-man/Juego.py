import pygame
import Nodo
import Mapa
import Imagen
import Imagenes
import Relacion
import Floyd
import threading
import time
import Dijkstra
import HiloFantasma
import HiloGeneral
import PantallaCarga
class Juego(object):
    """description of class"""
    def __init__(self, puntos):
        self.nodos = []
        self.mapa_imagenes = []
        self.ruta = []
        self.respaldo = []
        self.pacman = None
        self.fantasmas = []
        self.vidas = []
        self.total_puntos = 0
        self.puntaje = puntos

    def obtener_Mapa(self,nivel):
        m =[]
        archivo_texto=open("datos/mapas/Nivel"+str(nivel+1)+".txt","r")
        lineas = []
        for line in archivo_texto:
            lineas.append(line)
        
        for x in range(23):
            m.append([])
            for j in range(23):
                m[x].append(lineas[x][j])
        archivo_texto.close()
        return m
    def llenar_lista_nodos(self,nivel):
        #mapa = Mapa.Mapa
        m = self.obtener_Mapa(nivel)
        self.respaldo = m
        self.mapa_imagenes = []
        contador = 0
        self.nodos = []
        self.ruta = []
        id = -1
        for i in range(len(m)):
            self.mapa_imagenes.append([])
            for j in range(len(m)):
                if m[i][j] != '#' and m[i][j] != ' 'and m[i][j] != '':
                    if m[i][j] == '_' or m[i][j] == '+':
                        self.total_puntos += 1
                    n = Nodo.Nodo(contador, m[i][j], None, i, j)
                    self.nodos.append(n)
                    id = contador
                    contador += 1
                n = Nodo.Nodo(id, m[i][j], None, i, j)
                self.mapa_imagenes[i].append(n)
                id = -1

        for x in range(4):
            lista = []
            for k in range(len(self.nodos)):
                lista.append(self.nodos[k].tipo)
            self.fantasmas.append(lista)

        for x in range(len(self.nodos)):
            self.ruta.append([])
            for j in range(len(self.nodos)):
                self.ruta[x].append(0)

        for i in range(len(self.nodos)):
            for j in range(len(self.nodos)):
                i1,j1 = self.nodos[i].x, self.nodos[i].y
                i2,j2 = self.nodos[j].x, self.nodos[j].y
                if (j1-1 == -1 or j1+1 == len(m)) and (j2-1 == -1 or j2+1 == len(m)):
                    self.ruta[i][j] = 1
                if (i1,j1+1)==(i2,j2) or (i1,j1-1)==(i2,j2) or (i1+1,j1)==(i2,j2) or (i1-1,j1)==(i2,j2):
                    self.ruta[i][j] = 1

                
    def validar(self,mposx,mposy,posx,posy):
        sumax = mposx + posx;
        sumay = mposy + posy;
        if sumax < 0 or sumax > 22 or sumay < 0 or sumay > 22:
            return False
        else:
            if self.mapa_imagenes[sumax][sumay].tipo=='#':
                return True
        return False

    def asignar_Muro(self, mposx, mposy,i,j,tamCuadro,imagenes):

        if self.validar(mposx, mposy,0,1) == True and self.validar(mposx, mposy,0,-1) == True and self.validar(mposx, mposy,1,0) == True and self.validar(mposx, mposy,-1,0) == True:
            return Imagen.Imagen(imagenes.obtener_imagen_muro("Intersección", tamCuadro, tamCuadro), i+155, j+105, tamCuadro, tamCuadro)
        if self.validar(mposx, mposy,0,1) == False and self.validar(mposx, mposy,0,-1) == False and self.validar(mposx, mposy,1,0) == False and self.validar(mposx, mposy,-1,0) == False:
            return Imagen.Imagen(imagenes.obtener_imagen_muro("MuroSolo", tamCuadro, tamCuadro), i+155, j+105, tamCuadro, tamCuadro)
        if self.validar(mposx, mposy,0,1) == True and self.validar(mposx, mposy,0,-1) == False and self.validar(mposx, mposy,1,0) == False and self.validar(mposx, mposy,-1,0) == False:
            return Imagen.Imagen(imagenes.obtener_imagen_muro_final("FinalIzquierdo", tamCuadro, tamCuadro), i+155, j+105, tamCuadro, tamCuadro)
        if self.validar(mposx, mposy,0,1) == False and self.validar(mposx, mposy,0,-1) == True and self.validar(mposx, mposy,1,0) == False and self.validar(mposx, mposy,-1,0) == False:
            return Imagen.Imagen(imagenes.obtener_imagen_muro_final("FinalDerecho", tamCuadro, tamCuadro), i+155, j+105, tamCuadro, tamCuadro)
        if self.validar(mposx, mposy,0,1) == False and self.validar(mposx, mposy,0,-1) == False and self.validar(mposx, mposy,1,0) == True and self.validar(mposx, mposy,-1,0) == False:
            return Imagen.Imagen(imagenes.obtener_imagen_muro_final("FinalSuperior", tamCuadro, tamCuadro), i+155, j+105, tamCuadro, tamCuadro)
        if self.validar(mposx, mposy,0,1) == False and self.validar(mposx, mposy,0,-1) == False and self.validar(mposx, mposy,1,0) == False and self.validar(mposx, mposy,-1,0) == True:
            return Imagen.Imagen(imagenes.obtener_imagen_muro_final("FinalInferior", tamCuadro, tamCuadro), i+155, j+105, tamCuadro, tamCuadro)
        if self.validar(mposx, mposy,0,1) == True and self.validar(mposx, mposy,0,-1) == True and self.validar(mposx, mposy,1,0) == False and self.validar(mposx, mposy,-1,0) == False:
            return Imagen.Imagen(imagenes.obtener_imagen_muro_intermedio("MuroIntermedioHorizontal", tamCuadro, tamCuadro), i+155, j+105, tamCuadro, tamCuadro)
        if self.validar(mposx, mposy,0,1) == False and self.validar(mposx, mposy,0,-1) == False and self.validar(mposx, mposy,1,0) == True and self.validar(mposx, mposy,-1,0) == True:
            return Imagen.Imagen(imagenes.obtener_imagen_muro_intermedio("MuroIntermedioVertical", tamCuadro, tamCuadro), i+155, j+105, tamCuadro, tamCuadro)
        if self.validar(mposx, mposy,0,1) == True and self.validar(mposx, mposy,0,-1) == False and self.validar(mposx, mposy,1,0) == True and self.validar(mposx, mposy,-1,0) == False:
            return Imagen.Imagen(imagenes.obtener_imagen_muro_esquina("EsquinaSuperiorIzquierda", tamCuadro, tamCuadro), i+155, j+105, tamCuadro, tamCuadro)
        if self.validar(mposx, mposy,0,1) == False and self.validar(mposx, mposy,0,-1) == True and self.validar(mposx, mposy,1,0) == False and self.validar(mposx, mposy,-1,0) == True:
            return Imagen.Imagen(imagenes.obtener_imagen_muro_esquina("EsquinaInferiorDerecha", tamCuadro, tamCuadro), i+155, j+105, tamCuadro, tamCuadro)
        if self.validar(mposx, mposy,0,1) == True and self.validar(mposx, mposy,0,-1) == False and self.validar(mposx, mposy,1,0) == False and self.validar(mposx, mposy,-1,0) == True:
            return Imagen.Imagen(imagenes.obtener_imagen_muro_esquina("EsquinaInferiorIzquierda", tamCuadro, tamCuadro), i+155, j+105, tamCuadro, tamCuadro)
        if self.validar(mposx, mposy,0,1) == False and self.validar(mposx, mposy,0,-1) == True and self.validar(mposx, mposy,1,0) == True and self.validar(mposx, mposy,-1,0) == False:
            return Imagen.Imagen(imagenes.obtener_imagen_muro_esquina("EsquinaSuperiorDerecha", tamCuadro, tamCuadro), i+155, j+105, tamCuadro, tamCuadro)
        if self.validar(mposx, mposy,0,1) == True and self.validar(mposx, mposy,0,-1) == True and self.validar(mposx, mposy,1,0) == True and self.validar(mposx, mposy,-1,0) == False:
            return Imagen.Imagen(imagenes.obtener_imagen_muro_interseccion("InterseccionSuperior", tamCuadro, tamCuadro), i+155, j+105, tamCuadro, tamCuadro)
        if self.validar(mposx, mposy,0,1) == False and self.validar(mposx, mposy,0,-1) == True and self.validar(mposx, mposy,1,0) == True and self.validar(mposx, mposy,-1,0) == True:
            return Imagen.Imagen(imagenes.obtener_imagen_muro_interseccion("InterseccionDerecha", tamCuadro, tamCuadro), i+155, j+105, tamCuadro, tamCuadro)
        if self.validar(mposx, mposy,0,1) == True and self.validar(mposx, mposy,0,-1) == False and self.validar(mposx, mposy,1,0) == True and self.validar(mposx, mposy,-1,0) == True:
            return Imagen.Imagen(imagenes.obtener_imagen_muro_interseccion("InterseccionIzquierda", tamCuadro, tamCuadro), i+155, j+105, tamCuadro, tamCuadro)
        if self.validar(mposx, mposy,0,1) == True and self.validar(mposx, mposy,0,-1) == True and self.validar(mposx, mposy,1,0) == False and self.validar(mposx, mposy,-1,0) == True:
            return Imagen.Imagen(imagenes.obtener_imagen_muro_interseccion("InterseccionInferior", tamCuadro, tamCuadro), i+155, j+105, tamCuadro, tamCuadro)
        return None
        

    def pantalla_juego(self, recorrido, peso, nivel):
        posicion_x_pacman = 0
        posicion_y_pacman = 0
        contador_fantasma = 0

        AZUL = (0, 0, 255)
        BLACK = (0, 0, 0)
        tamCuadro = 21
        imagenes = Imagenes.Imagenes()
        d = Dijkstra.Dijkstra
        f = Floyd.Floyd()
        super_Velocidad= Imagen.Imagen(imagenes.obtener_imagen_boton("speed",40,40), 750, 20, 40, 40)
        no_super_velocidad= Imagen.Imagen(imagenes.obtener_imagen_boton("nspeed",40,40), 750, 20, 40, 40)
        bandera_hilo = True
        gameOver = True
        bandera = True
        powerP = False
        
        dire = "RIGHT"
        dire2 = ""

        tiempo_Color = 7
        lista_Tiempo = [10,1,6]
        lista_Validaciones = [False,False,False]
        validacion_Fin = [True]
        validaciones = [[False,False,False,False],[False,False,False,False],False]
        
        
        
        #fuente = pygame.font.Font(None, 30)
        fuente = pygame.font.SysFont("Stencil", 25)
        while bandera == True:
            self.llenar_lista_nodos(nivel)
            d = Dijkstra.Dijkstra
            if d.calcular_pesos(d, self.ruta) == True:
                bandera = False
        #print(total_puntos)
        bandera = True
        
        
        camino = []
        f.recorrido = recorrido[0]
        f.peso = peso[0]
        #f.pasarPesos(f,self.ruta)
        

        for x in range(6):
            self.vidas.append(imagenes.obtener_imagen("pacman", tamCuadro+8, tamCuadro+8))

        pygame.init()
        
        
        
        size = (820, 720)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Pac Man")
        clock = pygame.time.Clock()
        
        logo = pygame.image.load("recursos/muros/MuroSolo.png")
        logo = pygame.transform.scale(logo, (tamCuadro,tamCuadro))

        a = HiloGeneral.HiloGeneral(10,0,lista_Tiempo,lista_Validaciones, validacion_Fin)
        a.start()
        a1 = HiloGeneral.HiloGeneral(1,1,lista_Tiempo,lista_Validaciones, validacion_Fin)
        a1.start()
        a1 = HiloGeneral.HiloGeneral(6,2,lista_Tiempo,lista_Validaciones, validacion_Fin)
        a1.start()
        
        self.llenar_Matriz_Imagenes(tamCuadro, imagenes, posicion_x_pacman, posicion_y_pacman)
        color_Fantasma = 0 
        super_Habilidad = False
        while gameOver:
            for event in pygame.event.get():
                if pygame.mouse.get_pressed(3)==(1,0,0):
                    x1, y1 = event.pos
                    if(super_Velocidad.comparar_cord(x1,y1) and super_Habilidad == True):
                        super_Habilidad = False
                        lista_Tiempo[1] = 1
                        lista_Validaciones[1] = False
                if event.type == pygame.KEYDOWN and bandera == True:
                    bandera = False
                    if event.key == pygame.K_RIGHT:
                        y=posicion_y_pacman
                        if posicion_y_pacman+1 >= len(self.mapa_imagenes):
                            y = -1
                        if(self.mapa_imagenes[posicion_x_pacman][y+1].tipo!='#'):
                            dire = "RIGHT"
                        else:
                            dire2 = "RIGHT"
                    elif event.key == pygame.K_LEFT:
                        if(self.mapa_imagenes[posicion_x_pacman][posicion_y_pacman-1].tipo!='#'):
                            dire = "LEFT"
                        else:
                            dire2 = "LEFT"
                    elif event.key == pygame.K_DOWN:
                        if(self.mapa_imagenes[posicion_x_pacman+1][posicion_y_pacman].tipo!='#'):
                            dire = "DOWN"
                        else:
                            dire2 = "DOWN"
                    elif event.key == pygame.K_UP:
                        if(self.mapa_imagenes[posicion_x_pacman-1][posicion_y_pacman].tipo!='#'):
                            dire = "UP"
                        else:
                            dire2 = "UP"
                    
                if event.type == pygame.QUIT:
                    gameOver = False
            
            self.moverPacman(dire,posicion_x_pacman,posicion_y_pacman, tamCuadro, imagenes)
            self.pacman = self.mapa_imagenes[posicion_x_pacman][posicion_y_pacman]

            screen.fill(BLACK)

            fantasma1 = 0
            fantasma2 = 0
            fantasma3 = 0
            fantasma4 = 0
            for k in range(len(self.fantasmas)):
                for x in range(len(self.fantasmas[k])):
                    if self.fantasmas[k][x]=='1'and k==0:
                        fantasma1 = x
                    if self.fantasmas[k][x]=='2' and k==1:
                        fantasma2 = x
                    if self.fantasmas[k][x]=='3'and k==2:
                        fantasma3 = x
                    if self.fantasmas[k][x]=='4'and k==3:
                        fantasma4 = x
            n = None 
            for j in range(len(self.mapa_imagenes)):
                    for i in range(len(self.mapa_imagenes)):
                        if self.mapa_imagenes[i][j].tipo=='@':
                            posicion_x_pacman = i
                            posicion_y_pacman = j
                                
                        imag = self.mapa_imagenes[i][j].imagen
                        screen.blit(imag.imagen, (imag.i, imag.j))

                        n = self.mapa_imagenes[i][j]
                        if n != None:
                            x = n.imagen.i
                            y = n.imagen.j
                            if n.tipo != '@':
                                x -= 4
                                y -= 4
                            v = False
                            if powerP != True:
                                if self.mapa_imagenes[i][j].id == fantasma1:
                                    imag = Imagen.Imagen(imagenes.obtener_imagen_fantasma("blinky", tamCuadro+8, tamCuadro+8), x, y, tamCuadro+8, tamCuadro+8)
                                    screen.blit(imag.imagen, (imag.i, imag.j))
                                    #v = True
                                if self.mapa_imagenes[i][j].id == fantasma2:
                                    imag = Imagen.Imagen(imagenes.obtener_imagen_fantasma("pinky", tamCuadro+8, tamCuadro+8), x, y, tamCuadro+8, tamCuadro+8)
                                    screen.blit(imag.imagen, (imag.i, imag.j))
                                    #v = True
                                if self.mapa_imagenes[i][j].id == fantasma3:
                                    imag = Imagen.Imagen(imagenes.obtener_imagen_fantasma("inky", tamCuadro+8, tamCuadro+8), x, y, tamCuadro+8, tamCuadro+8)
                                    screen.blit(imag.imagen, (imag.i, imag.j))
                                    #v = True
                                if self.mapa_imagenes[i][j].id == fantasma4:
                                    imag = Imagen.Imagen(imagenes.obtener_imagen_fantasma("clyde", tamCuadro+8, tamCuadro+8), x, y, tamCuadro+8, tamCuadro+8)
                                    screen.blit(imag.imagen, (imag.i, imag.j))
                                #v = True
                            #if v == True:
                            else:
                                if self.mapa_imagenes[i][j].id == fantasma1 or self.mapa_imagenes[i][j].id == fantasma2 or self.mapa_imagenes[i][j].id == fantasma3 or self.mapa_imagenes[i][j].id == fantasma4:
                                    if validaciones[1][0] == True and self.mapa_imagenes[i][j].id == fantasma1:
                                        imag = Imagen.Imagen(imagenes.obtener_imagen_fantasma("ojosD", tamCuadro+8, tamCuadro+8), x, y, tamCuadro+8, tamCuadro+8)
                                        screen.blit(imag.imagen, (imag.i, imag.j))
                                    elif self.mapa_imagenes[i][j].id == fantasma1:
                                        if lista_Tiempo[0] == tiempo_Color:
                                            if color_Fantasma == 0:
                                                color_Fantasma = 1
                                                tiempo_Color += 1
                                            else:
                                                color_Fantasma = 0
                                                tiempo_Color += 1 

                                        if color_Fantasma == 0:
                                            imag = Imagen.Imagen(imagenes.obtener_imagen_fantasma("sad", tamCuadro+8, tamCuadro+8), x, y, tamCuadro+8, tamCuadro+8)
                                            screen.blit(imag.imagen, (imag.i, imag.j))
                                        else:
                                            imag = Imagen.Imagen(imagenes.obtener_imagen_fantasma("sadGris", tamCuadro+8, tamCuadro+8), x, y, tamCuadro+8, tamCuadro+8)
                                            screen.blit(imag.imagen, (imag.i, imag.j))
                                    if validaciones[1][1] == True and self.mapa_imagenes[i][j].id == fantasma2:
                                        imag = Imagen.Imagen(imagenes.obtener_imagen_fantasma("ojosD", tamCuadro+8, tamCuadro+8), x, y, tamCuadro+8, tamCuadro+8)
                                        screen.blit(imag.imagen, (imag.i, imag.j))
                                    elif self.mapa_imagenes[i][j].id == fantasma2:
                                        if lista_Tiempo[0] == tiempo_Color:
                                            if color_Fantasma == 0:
                                                color_Fantasma = 1
                                                tiempo_Color += 1
                                            else:
                                                color_Fantasma = 0
                                                tiempo_Color += 1 

                                        if color_Fantasma == 0:
                                            imag = Imagen.Imagen(imagenes.obtener_imagen_fantasma("sad", tamCuadro+8, tamCuadro+8), x, y, tamCuadro+8, tamCuadro+8)
                                            screen.blit(imag.imagen, (imag.i, imag.j))
                                        else:
                                            imag = Imagen.Imagen(imagenes.obtener_imagen_fantasma("sadGris", tamCuadro+8, tamCuadro+8), x, y, tamCuadro+8, tamCuadro+8)
                                            screen.blit(imag.imagen, (imag.i, imag.j))
                                    if validaciones[1][2] == True and self.mapa_imagenes[i][j].id == fantasma3:
                                        imag = Imagen.Imagen(imagenes.obtener_imagen_fantasma("ojosD", tamCuadro+8, tamCuadro+8), x, y, tamCuadro+8, tamCuadro+8)
                                        screen.blit(imag.imagen, (imag.i, imag.j))
                                    elif self.mapa_imagenes[i][j].id == fantasma3:
                                        if lista_Tiempo[0] == tiempo_Color:
                                            if color_Fantasma == 0:
                                                color_Fantasma = 1
                                                tiempo_Color += 1
                                            else:
                                                color_Fantasma = 0
                                                tiempo_Color += 1 

                                        if color_Fantasma == 0:
                                            imag = Imagen.Imagen(imagenes.obtener_imagen_fantasma("sad", tamCuadro+8, tamCuadro+8), x, y, tamCuadro+8, tamCuadro+8)
                                            screen.blit(imag.imagen, (imag.i, imag.j))
                                        else:
                                            imag = Imagen.Imagen(imagenes.obtener_imagen_fantasma("sadGris", tamCuadro+8, tamCuadro+8), x, y, tamCuadro+8, tamCuadro+8)
                                            screen.blit(imag.imagen, (imag.i, imag.j))
                                    if validaciones[1][3] == True and self.mapa_imagenes[i][j].id == fantasma4:
                                        imag = Imagen.Imagen(imagenes.obtener_imagen_fantasma("ojosD", tamCuadro+8, tamCuadro+8), x, y, tamCuadro+8, tamCuadro+8)
                                        screen.blit(imag.imagen, (imag.i, imag.j))
                                    elif self.mapa_imagenes[i][j].id == fantasma4:
                                        if lista_Tiempo[0] == tiempo_Color:
                                            if color_Fantasma == 0:
                                                color_Fantasma = 1
                                                tiempo_Color += 1
                                            else:
                                                color_Fantasma = 0
                                                tiempo_Color += 1 

                                        if color_Fantasma == 0:
                                            imag = Imagen.Imagen(imagenes.obtener_imagen_fantasma("sad", tamCuadro+8, tamCuadro+8), x, y, tamCuadro+8, tamCuadro+8)
                                        else:
                                            imag = Imagen.Imagen(imagenes.obtener_imagen_fantasma("sadGris", tamCuadro+8, tamCuadro+8), x, y, tamCuadro+8, tamCuadro+8)
                                        screen.blit(imag.imagen, (imag.i, imag.j))

            if lista_Validaciones[0] == True:
                powerP = False
                lista_Validaciones[0] = False
            if self.respaldo[posicion_x_pacman][posicion_y_pacman]=='+':
                powerP = True
                lista_Tiempo[0] = 0
                tiempo_Color = 7
                color_Fantasma = 0
            validaciones[2] = powerP
            
            
            if powerP == False:
                if validaciones[0][0] == False and validaciones[0][1] == False and validaciones[0][2] == False and validaciones[0][3] == False:
                    idP = self.mapa_imagenes[posicion_x_pacman][posicion_y_pacman].id
                    if(idP == fantasma1 or idP == fantasma2 or idP == fantasma3 or idP == fantasma4):
                        self.validar_Muerte(posicion_x_pacman-1,posicion_y_pacman)
                        self.mapa_imagenes[13][11].imagen.imagen = imagenes.obtener_imagen("pacman", tamCuadro+8, tamCuadro+8)
                        self.mapa_imagenes[13][11].tipo = '@'
                        self.mapa_imagenes[13][11].imagen.i -= 4
                        self.mapa_imagenes[13][11].imagen.j -= 4
                        
                        self.mapa_imagenes[posicion_x_pacman][posicion_y_pacman].imagen.imagen = imagenes.obtener_imagen("nada", tamCuadro, tamCuadro)
                        self.mapa_imagenes[posicion_x_pacman][posicion_y_pacman].imagen.i += 4
                        self.mapa_imagenes[posicion_x_pacman][posicion_y_pacman].imagen.j += 4
                        self.mapa_imagenes[posicion_x_pacman][posicion_y_pacman].tipo = ''
                        self.respaldo[posicion_x_pacman][posicion_y_pacman]=''
                        posicion_x_pacman = 13
                        posicion_y_pacman = 11
                        for x in range(len(validaciones[0])):
                            validaciones[0][x] = True
                        if len(self.vidas) != 0:
                            self.vidas.pop()
            
            else:
                idP = self.mapa_imagenes[posicion_x_pacman][posicion_y_pacman].id
                val = False
                if idP == fantasma1 and validaciones[1][0] == False:
                    if contador_fantasma >= 1:
                        self.puntaje += 100
                    self.puntaje += 300
                    validaciones[1][0] = True
                    contador_fantasma += 1
                    val = True
                if idP == fantasma2 and validaciones[1][1] == False:
                    if contador_fantasma >= 1:
                        self.puntaje += 100
                    self.puntaje += 300
                    validaciones[1][1] = True
                    contador_fantasma += 1
                    val = True
                if idP == fantasma3 and validaciones[1][2] == False:
                    if contador_fantasma >= 1:
                        self.puntaje += 100
                    self.puntaje += 300
                    validaciones[1][2] = True
                    contador_fantasma += 1
                    val = True
                if idP == fantasma4 and validaciones[1][3] == False:
                    if contador_fantasma >= 1:
                        self.puntaje += 100
                    self.puntaje += 300
                    validaciones[1][3] = True
                    contador_fantasma += 1
                    val = True
                if val == True:
                    if lista_Validaciones[1]==False and lista_Tiempo[1] == 1:
                        lista_Tiempo[1] = 0
                    elif lista_Validaciones[1]==False and lista_Tiempo[1] != 1:
                        super_Habilidad = True
                    
                        
            if lista_Validaciones[1] == True:
                lista_Validaciones[1] = False
                
            i1 = 165
            for x in range(len(self.vidas)):

                screen.blit(self.vidas[x], (i1, 625))
                i1+=30            

            if self.validar_dire(dire2,posicion_x_pacman,posicion_y_pacman)==True:
                dire = dire2
                dire2 = ""
            if self.validar_dire(dire,posicion_x_pacman,posicion_y_pacman)==False:
                dire2 = ""

            
            bandera = True

            text = "Puntaje"
            mensaje = fuente.render(text, 1, (27, 67, 207))
            screen.blit(mensaje, (30, 115))

            text = str(self.puntaje)
            j = 145
            for c in text:
                mensaje = fuente.render(c, 1, (225, 121, 121))
                screen.blit(mensaje, (80, j))
                j+=25

            if bandera_hilo == True:
                
                self.hilo(d, f, '1',0.1, validaciones, validacion_Fin)
                self.hilo(d, f, '4',0.3, validaciones, validacion_Fin)
                self.hilo(d, f, '2',0.3, validaciones, validacion_Fin)
                self.hilo(d, f, '3',0.3, validaciones, validacion_Fin)
                
                bandera_hilo = False
            if super_Habilidad == True:
                screen.blit(super_Velocidad.imagen,(super_Velocidad.i,super_Velocidad.j))
            else:
                screen.blit(no_super_velocidad.imagen,(no_super_velocidad.i,no_super_velocidad.j))
            pygame.display.flip()
            
            #time.sleep(0.15)
            clock.tick(8)
            print(self.total_puntos)
            if self.total_puntos <= 0 and nivel < 10:
                validacion_Fin[0] = False
                pc = PantallaCarga.PantallaCarga
                pc.pantalla(pc,'J',nivel+1,self.puntaje)
        pygame.quit()

    def llenar_Matriz_Imagenes(self,tamCuadro, imagenes, posicion_x_pacman, posicion_y_pacman):
        i1 = 0
        for j in range(1, 500, tamCuadro + 1):
                j1 = 0
                if i1 < 23:
                    for i in range(1, 500, tamCuadro+1):
                        if j1 < 23:
                              
                            if self.mapa_imagenes[i1][j1].tipo =='#':
                                img = self.asignar_Muro(i1,j1,i,j,tamCuadro+10,imagenes)
                                self.mapa_imagenes[i1][j1].imagen = img
                                        
                            elif self.mapa_imagenes[i1][j1].tipo=='@':
                                posicion_x_pacman = i1
                                posicion_y_pacman = j1
                                img = Imagen.Imagen(imagenes.obtener_imagen("pacman", tamCuadro+8, tamCuadro+8), i+156, j+106, tamCuadro+8, tamCuadro+8)
                                self.nodos[self.mapa_imagenes[i1][j1].id].imagen = img
                                self.mapa_imagenes[i1][j1].imagen = img
                            elif self.mapa_imagenes[i1][j1].tipo=='_':
                                img = Imagen.Imagen(imagenes.obtener_imagen("bola", tamCuadro, tamCuadro), i+160, j+110, tamCuadro, tamCuadro)
                                self.nodos[self.mapa_imagenes[i1][j1].id].imagen = img
                                self.mapa_imagenes[i1][j1].imagen = img
                            elif self.mapa_imagenes[i1][j1].tipo=='+':
                                img = Imagen.Imagen(imagenes.obtener_imagen("power", tamCuadro, tamCuadro), i+160, j+110, tamCuadro, tamCuadro)
                                self.nodos[self.mapa_imagenes[i1][j1].id].imagen = img
                                self.mapa_imagenes[i1][j1].imagen = img
                            elif self.mapa_imagenes[i1][j1].tipo==''or self.mapa_imagenes[i1][j1].tipo==' 'or self.mapa_imagenes[i1][j1].tipo=='-' or self.mapa_imagenes[i1][j1].tipo=='1' or self.mapa_imagenes[i1][j1].tipo=='2' or self.mapa_imagenes[i1][j1].tipo=='3' or self.mapa_imagenes[i1][j1].tipo=='4':
                                img = Imagen.Imagen(imagenes.obtener_imagen("nada", tamCuadro, tamCuadro), i+160, j+110, tamCuadro, tamCuadro)
                                self.nodos[self.mapa_imagenes[i1][j1].id].imagen = img
                                self.mapa_imagenes[i1][j1].imagen = img
                            
                            j1 += 1
                    i1 += 1
    def validar_dire(self, dire2,posicion_x_pacman,posicion_y_pacman):
        if dire2 == "RIGHT":
            y=posicion_y_pacman
            if posicion_y_pacman+1 >= len(self.mapa_imagenes):
                y = -1
            if(self.mapa_imagenes[posicion_x_pacman][y+1].tipo!='#'):
                return True
        elif dire2 == "LEFT":
            if(self.mapa_imagenes[posicion_x_pacman][posicion_y_pacman-1].tipo!='#'):
                return True
        elif dire2 == "DOWN":
            if(self.mapa_imagenes[posicion_x_pacman+1][posicion_y_pacman].tipo!='#'):
                return True
        elif dire2 == "UP":
            if(self.mapa_imagenes[posicion_x_pacman-1][posicion_y_pacman].tipo!='#'):
                return True
        return False

    def hilo(self, dijkstra, floyd, fantasma, dalay,validaciones, validacion_Fin):
        a = HiloFantasma.HiloFantasma(dalay,self.mapa_imagenes, dijkstra, floyd, self.nodos,self.ruta,fantasma, self.pacman, self.respaldo, self.fantasmas,validaciones,validacion_Fin)
        a.start()

    def moverPacman(self,dire,posicion_x_pacman,posicion_y_pacman, tamCuadro, imagenes):
        val = False
        x1=posicion_x_pacman
        y1=posicion_y_pacman
        if dire == "RIGHT":
            x=posicion_x_pacman
            y=posicion_y_pacman
            if posicion_y_pacman+1 >= len(self.mapa_imagenes):
                y = -1
            if(self.mapa_imagenes[posicion_x_pacman][y+1].tipo!='#'):
                self.validar_Muerte(posicion_x_pacman,y+1)
                self.mapa_imagenes[x][y+1].imagen.imagen = imagenes.obtener_imagen("pacman", tamCuadro+8, tamCuadro+8)
                self.mapa_imagenes[x][y+1].imagen.i -= 4
                self.mapa_imagenes[x][y+1].imagen.j -= 4
                self.mapa_imagenes[x][y+1].tipo = '@'
                val = True
                y1 = y+1
                
        elif dire == "LEFT":
            if(self.mapa_imagenes[posicion_x_pacman][posicion_y_pacman-1].tipo!='#'):
                self.validar_Muerte(posicion_x_pacman,posicion_y_pacman-1)
                self.mapa_imagenes[posicion_x_pacman][posicion_y_pacman-1].imagen.imagen = imagenes.obtener_imagen("pacman", tamCuadro+8, tamCuadro+8)
                self.mapa_imagenes[posicion_x_pacman][posicion_y_pacman-1].tipo = '@'
                self.mapa_imagenes[posicion_x_pacman][posicion_y_pacman-1].imagen.i -= 4
                self.mapa_imagenes[posicion_x_pacman][posicion_y_pacman-1].imagen.j -= 4
                val = True
                y1-=1
                
        elif dire == "DOWN":
            if(self.mapa_imagenes[posicion_x_pacman+1][posicion_y_pacman].tipo!='#'):
                self.validar_Muerte(posicion_x_pacman+1,posicion_y_pacman)
                self.mapa_imagenes[posicion_x_pacman+1][posicion_y_pacman].imagen.imagen = imagenes.obtener_imagen("pacman", tamCuadro+8, tamCuadro+8)
                self.mapa_imagenes[posicion_x_pacman+1][posicion_y_pacman].tipo = '@'
                self.mapa_imagenes[posicion_x_pacman+1][posicion_y_pacman].imagen.i -= 4
                self.mapa_imagenes[posicion_x_pacman+1][posicion_y_pacman].imagen.j -= 4
                val = True
                x1+=1
                
        elif dire == "UP":
            if(self.mapa_imagenes[posicion_x_pacman-1][posicion_y_pacman].tipo!='#'):
                self.validar_Muerte(posicion_x_pacman-1,posicion_y_pacman)
                self.mapa_imagenes[posicion_x_pacman-1][posicion_y_pacman].imagen.imagen = imagenes.obtener_imagen("pacman", tamCuadro+8, tamCuadro+8)
                self.mapa_imagenes[posicion_x_pacman-1][posicion_y_pacman].tipo = '@'
                self.mapa_imagenes[posicion_x_pacman-1][posicion_y_pacman].imagen.i -= 4
                self.mapa_imagenes[posicion_x_pacman-1][posicion_y_pacman].imagen.j -= 4
                val = True
                x1-=1
        if val == True:
            self.mapa_imagenes[posicion_x_pacman][posicion_y_pacman].imagen.imagen = imagenes.obtener_imagen("nada", tamCuadro, tamCuadro)
            self.mapa_imagenes[posicion_x_pacman][posicion_y_pacman].imagen.i += 4
            self.mapa_imagenes[posicion_x_pacman][posicion_y_pacman].imagen.j += 4
            self.mapa_imagenes[posicion_x_pacman][posicion_y_pacman].tipo = ''
            
            if self.respaldo[x1][y1] == '_':
                self.total_puntos -= 1
                self.puntaje += 10
                #print(total_puntos)
            if self.respaldo[x1][y1] == '+':
                self.total_puntos -= 1
                self.puntaje += 50
                #print(total_puntos)
            self.respaldo[posicion_x_pacman][posicion_y_pacman]=''
    
    def validar_Muerte(self,posicion_x_pacman,posicion_y_pacman):
        if self.mapa_imagenes[posicion_x_pacman][posicion_y_pacman].tipo == '4':
            print("Comio")

