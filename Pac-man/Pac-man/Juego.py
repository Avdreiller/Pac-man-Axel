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
class Juego(object):
    """description of class"""
    nodos = []
    mapa_imagenes = []
    ruta = []
    respaldo = []
    pacman = None
    fantasmas = []


    def llenar_lista_nodos(self):
        mapa = Mapa.Mapa
        m = mapa.generar_Mapa(mapa)
        self.respaldo = m
        self.mapa_imagenes = []
        contador = 0
        self.nodos = []
        self.ruta = []
        #for x in range(len(m)):
        #    self.mapa_imagenes.append([])
        #    for j in range(len(m)):
        #        self.mapa_imagenes[x].append(Nodo.Nodo(0,'',None,0,0))
        id = -1
        for i in range(len(m)):
            self.mapa_imagenes.append([])
            for j in range(len(m)):
                
                
                if m[i][j] != '#' and m[i][j] != ' 'and m[i][j] != '':
                    n = Nodo.Nodo(contador, m[i][j], None, i, j)
                    #print("("+m[i][j]+")")
                    self.nodos.append(n)
                    id = contador
                    contador += 1
                    
                n = Nodo.Nodo(id, m[i][j], None, i, j)
                #print(id, contador)
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
                #if j1-1 >= 0:
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

        if self.validar(self,mposx, mposy,0,1) == True and self.validar(self,mposx, mposy,0,-1) == True and self.validar(self,mposx, mposy,1,0) == True and self.validar(self,mposx, mposy,-1,0) == True:
            return Imagen.Imagen(imagenes.obtener_imagen_muro("Intersección", tamCuadro, tamCuadro), i+155, j+105, tamCuadro, tamCuadro)
        if self.validar(self,mposx, mposy,0,1) == False and self.validar(self,mposx, mposy,0,-1) == False and self.validar(self,mposx, mposy,1,0) == False and self.validar(self,mposx, mposy,-1,0) == False:
            return Imagen.Imagen(imagenes.obtener_imagen_muro("MuroSolo", tamCuadro, tamCuadro), i+155, j+105, tamCuadro, tamCuadro)
        if self.validar(self,mposx, mposy,0,1) == True and self.validar(self,mposx, mposy,0,-1) == False and self.validar(self,mposx, mposy,1,0) == False and self.validar(self,mposx, mposy,-1,0) == False:
            return Imagen.Imagen(imagenes.obtener_imagen_muro_final("FinalIzquierdo", tamCuadro, tamCuadro), i+155, j+105, tamCuadro, tamCuadro)
        if self.validar(self,mposx, mposy,0,1) == False and self.validar(self,mposx, mposy,0,-1) == True and self.validar(self,mposx, mposy,1,0) == False and self.validar(self,mposx, mposy,-1,0) == False:
            return Imagen.Imagen(imagenes.obtener_imagen_muro_final("FinalDerecho", tamCuadro, tamCuadro), i+155, j+105, tamCuadro, tamCuadro)
        if self.validar(self,mposx, mposy,0,1) == False and self.validar(self,mposx, mposy,0,-1) == False and self.validar(self,mposx, mposy,1,0) == True and self.validar(self,mposx, mposy,-1,0) == False:
            return Imagen.Imagen(imagenes.obtener_imagen_muro_final("FinalSuperior", tamCuadro, tamCuadro), i+155, j+105, tamCuadro, tamCuadro)
        if self.validar(self,mposx, mposy,0,1) == False and self.validar(self,mposx, mposy,0,-1) == False and self.validar(self,mposx, mposy,1,0) == False and self.validar(self,mposx, mposy,-1,0) == True:
            return Imagen.Imagen(imagenes.obtener_imagen_muro_final("FinalInferior", tamCuadro, tamCuadro), i+155, j+105, tamCuadro, tamCuadro)
        if self.validar(self,mposx, mposy,0,1) == True and self.validar(self,mposx, mposy,0,-1) == True and self.validar(self,mposx, mposy,1,0) == False and self.validar(self,mposx, mposy,-1,0) == False:
            return Imagen.Imagen(imagenes.obtener_imagen_muro_intermedio("MuroIntermedioHorizontal", tamCuadro, tamCuadro), i+155, j+105, tamCuadro, tamCuadro)
        if self.validar(self,mposx, mposy,0,1) == False and self.validar(self,mposx, mposy,0,-1) == False and self.validar(self,mposx, mposy,1,0) == True and self.validar(self,mposx, mposy,-1,0) == True:
            return Imagen.Imagen(imagenes.obtener_imagen_muro_intermedio("MuroIntermedioVertical", tamCuadro, tamCuadro), i+155, j+105, tamCuadro, tamCuadro)
        if self.validar(self,mposx, mposy,0,1) == True and self.validar(self,mposx, mposy,0,-1) == False and self.validar(self,mposx, mposy,1,0) == True and self.validar(self,mposx, mposy,-1,0) == False:
            return Imagen.Imagen(imagenes.obtener_imagen_muro_esquina("EsquinaSuperiorIzquierda", tamCuadro, tamCuadro), i+155, j+105, tamCuadro, tamCuadro)
        if self.validar(self,mposx, mposy,0,1) == False and self.validar(self,mposx, mposy,0,-1) == True and self.validar(self,mposx, mposy,1,0) == False and self.validar(self,mposx, mposy,-1,0) == True:
            return Imagen.Imagen(imagenes.obtener_imagen_muro_esquina("EsquinaInferiorDerecha", tamCuadro, tamCuadro), i+155, j+105, tamCuadro, tamCuadro)
        if self.validar(self,mposx, mposy,0,1) == True and self.validar(self,mposx, mposy,0,-1) == False and self.validar(self,mposx, mposy,1,0) == False and self.validar(self,mposx, mposy,-1,0) == True:
            return Imagen.Imagen(imagenes.obtener_imagen_muro_esquina("EsquinaInferiorIzquierda", tamCuadro, tamCuadro), i+155, j+105, tamCuadro, tamCuadro)
        if self.validar(self,mposx, mposy,0,1) == False and self.validar(self,mposx, mposy,0,-1) == True and self.validar(self,mposx, mposy,1,0) == True and self.validar(self,mposx, mposy,-1,0) == False:
            return Imagen.Imagen(imagenes.obtener_imagen_muro_esquina("EsquinaSuperiorDerecha", tamCuadro, tamCuadro), i+155, j+105, tamCuadro, tamCuadro)
        if self.validar(self,mposx, mposy,0,1) == True and self.validar(self,mposx, mposy,0,-1) == True and self.validar(self,mposx, mposy,1,0) == True and self.validar(self,mposx, mposy,-1,0) == False:
            return Imagen.Imagen(imagenes.obtener_imagen_muro_interseccion("InterseccionSuperior", tamCuadro, tamCuadro), i+155, j+105, tamCuadro, tamCuadro)
        if self.validar(self,mposx, mposy,0,1) == False and self.validar(self,mposx, mposy,0,-1) == True and self.validar(self,mposx, mposy,1,0) == True and self.validar(self,mposx, mposy,-1,0) == True:
            return Imagen.Imagen(imagenes.obtener_imagen_muro_interseccion("InterseccionDerecha", tamCuadro, tamCuadro), i+155, j+105, tamCuadro, tamCuadro)
        if self.validar(self,mposx, mposy,0,1) == True and self.validar(self,mposx, mposy,0,-1) == False and self.validar(self,mposx, mposy,1,0) == True and self.validar(self,mposx, mposy,-1,0) == True:
            return Imagen.Imagen(imagenes.obtener_imagen_muro_interseccion("InterseccionIzquierda", tamCuadro, tamCuadro), i+155, j+105, tamCuadro, tamCuadro)
        if self.validar(self,mposx, mposy,0,1) == True and self.validar(self,mposx, mposy,0,-1) == True and self.validar(self,mposx, mposy,1,0) == False and self.validar(self,mposx, mposy,-1,0) == True:
            return Imagen.Imagen(imagenes.obtener_imagen_muro_interseccion("InterseccionInferior", tamCuadro, tamCuadro), i+155, j+105, tamCuadro, tamCuadro)
        return None
        

    def pantalla_juego(self):
        posicion_x_pacman = 0
        posicion_y_pacman = 0
        bandera = True
        
        d = Dijkstra.Dijkstra
        while bandera == True:
            self.llenar_lista_nodos(self)
            d = Dijkstra.Dijkstra
            if d.calcular_pesos(d, self.ruta) == True:
                bandera = False
        bandera = True
        f = Floyd.Floyd
        
        camino = []
        #f.pasarPesos(f,self.ruta)
        

        #print(self.nodos[0].x,self.nodos[0].y,"-------------")
        #camino = f.getCamino(f, self.nodos[100], self.nodos[0], self.ruta, self.nodos)
        
        #camino = d.getCamino(d, self.nodos[100], self.nodos[0], self.ruta, self.nodos)
        #if(camino != None):
        #    for x in range(len(camino)):
        #        print(camino[x].id)
        pygame.init()
        
        AZUL = (0, 0, 255)
        BLACK = (0, 0, 0)
        tamCuadro = 21
        imagenes = Imagenes.Imagenes()
        #mapa_imagenes = []
        #for x in range(23):
        #    mapa_imagenes.append([])
        #    for j in range(23):
        #        self.mapa_imagenes[x].append(Nodo.Nodo(0,'',None,0,0))
        
        size = (820, 720)
        screen = pygame.display.set_mode(size)
        #pygame.key.set_repeat(500,30)
        pygame.display.set_caption("Grid on PYGAME")
        clock = pygame.time.Clock()
        gameOver = True
        logo = pygame.image.load("recursos/muros/MuroSolo.png")
        logo = pygame.transform.scale(logo, (tamCuadro,tamCuadro))
        primera_vandera = True
        x1 = 0
        dire = "RIGHT"
        dire2 = ""
        bandera_hilo = True
        powerP = False
        lista_Tiempo = []
        lista_Validaciones = []
        lista_Tiempo.append(10)
        lista_Validaciones.append(False)
        a = HiloGeneral.HiloGeneral(10,0,lista_Tiempo,lista_Validaciones)
        a.start()
        validaciones = [[False,False,False,False],[False,False,False,False]]
        while gameOver:
            #camino = d.getCamino(d, self.nodos[100], self.nodos[0], self.ruta, self.nodos)
            for event in pygame.event.get():
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

            screen.fill(BLACK)
            i1 = 0
            #id = 0

            for j in range(1, 500, tamCuadro + 1):
                j1 = 0
                if i1 < 23:
                    for i in range(1, 500, tamCuadro+1):
                        if j1 < 23:
                            if primera_vandera == True:   
                                if self.mapa_imagenes[i1][j1].tipo =='#':
                                    img = self.asignar_Muro(self,i1,j1,i,j,tamCuadro+10,imagenes)
                                    #self.nodos[id].imagen = img
                                    self.mapa_imagenes[i1][j1].imagen = img
                                    if img != None:
                                        screen.blit(img.imagen, (i+155, j+105))
                                        
                                elif self.mapa_imagenes[i1][j1].tipo=='@':
                                    posicion_x_pacman = i1
                                    posicion_y_pacman = j1
                                    img = Imagen.Imagen(imagenes.obtener_imagen("pacman", tamCuadro+8, tamCuadro+8), i+156, j+106, tamCuadro+8, tamCuadro+8)
                                    self.nodos[self.mapa_imagenes[i1][j1].id].imagen = img
                                    self.mapa_imagenes[i1][j1].imagen = img
                                    id = self.mapa_imagenes[i1][j1].id
                                    #print(self.mapa_imagenes[i1][j1].imagen.i,self.mapa_imagenes[i1][j1].imagen.j,id, "("+self.mapa_imagenes[i1][j1].tipo+")")
                                    #print(self.nodos[id].imagen.i,self.nodos[id].imagen.j,self.nodos[id].id)
                                    screen.blit(self.mapa_imagenes[i1][j1].imagen.imagen, (self.mapa_imagenes[i1][j1].imagen.i, self.mapa_imagenes[i1][j1].imagen.j))
                                elif self.mapa_imagenes[i1][j1].tipo=='_':
                                    img = Imagen.Imagen(imagenes.obtener_imagen("bola", tamCuadro, tamCuadro), i+160, j+110, tamCuadro, tamCuadro)
                                    self.nodos[self.mapa_imagenes[i1][j1].id].imagen = img
                                    self.mapa_imagenes[i1][j1].imagen = img
                                    screen.blit(self.mapa_imagenes[i1][j1].imagen.imagen, (self.mapa_imagenes[i1][j1].imagen.i, self.mapa_imagenes[i1][j1].imagen.j))
                                elif self.mapa_imagenes[i1][j1].tipo=='+':
                                    img = Imagen.Imagen(imagenes.obtener_imagen("power", tamCuadro, tamCuadro), i+160, j+110, tamCuadro, tamCuadro)
                                    self.nodos[self.mapa_imagenes[i1][j1].id].imagen = img
                                    self.mapa_imagenes[i1][j1].imagen = img
                                    screen.blit(self.mapa_imagenes[i1][j1].imagen.imagen, (self.mapa_imagenes[i1][j1].imagen.i, self.mapa_imagenes[i1][j1].imagen.j))
                                elif self.mapa_imagenes[i1][j1].tipo==''or self.mapa_imagenes[i1][j1].tipo==' 'or self.mapa_imagenes[i1][j1].tipo=='-' or self.mapa_imagenes[i1][j1].tipo=='1' or self.mapa_imagenes[i1][j1].tipo=='2' or self.mapa_imagenes[i1][j1].tipo=='3' or self.mapa_imagenes[i1][j1].tipo=='4':
                                    img = Imagen.Imagen(imagenes.obtener_imagen("nada", tamCuadro, tamCuadro), i+160, j+110, tamCuadro, tamCuadro)
                                    self.nodos[self.mapa_imagenes[i1][j1].id].imagen = img
                                    self.mapa_imagenes[i1][j1].imagen = img
                                    screen.blit(self.mapa_imagenes[i1][j1].imagen.imagen, (self.mapa_imagenes[i1][j1].imagen.i, self.mapa_imagenes[i1][j1].imagen.j))
                            else:
                                
                                if self.mapa_imagenes[i1][j1].tipo=='@':
                                    posicion_x_pacman = i1
                                    posicion_y_pacman = j1
                                    self.mapa_imagenes[i1][j1].imagen.i = i+156
                                    self.mapa_imagenes[i1][j1].imagen.j = j+106
                                
                                imag = self.mapa_imagenes[i1][j1].imagen
                                screen.blit(imag.imagen, (imag.i, imag.j))
                            j1 += 1
                    i1 += 1
            if lista_Validaciones[0] == True:
                powerP = False
                lista_Validaciones[0] = False
            if self.respaldo[posicion_x_pacman][posicion_y_pacman]=='+':
                powerP = True
                lista_Tiempo[0] = 0
            
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
            if powerP == False:
                if validaciones[0][0] == False and validaciones[0][1] == False and validaciones[0][2] == False and validaciones[0][3] == False:
                    idP = self.mapa_imagenes[posicion_x_pacman][posicion_y_pacman].id
                    if(idP == fantasma1 or idP == fantasma2 or idP == fantasma3 or idP == fantasma4):
                        self.validar_Muerte(self,posicion_x_pacman-1,posicion_y_pacman)
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
                        #for i in range(len(self.mapa_imagenes)):
                        #    for j in range(len(self.mapa_imagenes)):
                        #        if self.respaldo[i][j]=='1':
                        #            self.fantasmas[0][fantasma1] = self.nodos[fantasma1].tipo
                        #            self.fantasmas[0][self.mapa_imagenes[10][11].id] = '1'
                        #        if self.respaldo[i][j]=='2':
                        #            self.fantasmas[1][fantasma2] = self.nodos[fantasma2].tipo
                        #            self.fantasmas[1][self.mapa_imagenes[11][12].id] = '2'
                        #        if self.respaldo[i][j]=='3':
                        #            self.fantasmas[2][fantasma3] = self.nodos[fantasma3].tipo
                        #            self.fantasmas[2][self.mapa_imagenes[11][10].id] = '3'
                        #        if self.respaldo[i][j]=='4':
                        #            self.fantasmas[3][fantasma4] = self.nodos[fantasma4].tipo
                        #            self.fantasmas[3][self.mapa_imagenes[11][11].id] = '4'
            else:
                idP = self.mapa_imagenes[posicion_x_pacman][posicion_y_pacman].id
                if idP == fantasma1:
                    validaciones[1][0] = True
                if idP == fantasma2:
                    validaciones[1][1] = True
                if idP == fantasma3:
                    validaciones[1][2] = True
                if idP == fantasma4:
                    validaciones[1][3] = True

            for i in range(len(self.respaldo)):
                for j in range(len(self.respaldo)):
                    n = self.mapa_imagenes[i][j]
                    if n != None:
                        x = n.imagen.i
                        y = n.imagen.j
                        if n.tipo != '@':
                            x -= 4
                            y -= 4
                        if self.mapa_imagenes[i][j].id == fantasma1:
                            
                            imag = Imagen.Imagen(imagenes.obtener_imagen_fantasma("blinky", tamCuadro+8, tamCuadro+8), x, y, tamCuadro+8, tamCuadro+8)
                            if powerP == True:
                                imag = Imagen.Imagen(imagenes.obtener_imagen_fantasma("sad", tamCuadro+8, tamCuadro+8), x, y, tamCuadro+8, tamCuadro+8)
                            screen.blit(imag.imagen, (imag.i, imag.j))
                        if self.mapa_imagenes[i][j].id == fantasma2:
                            imag = Imagen.Imagen(imagenes.obtener_imagen_fantasma("pinky", tamCuadro+8, tamCuadro+8), x, y, tamCuadro+8, tamCuadro+8)
                            if powerP == True:
                                imag = Imagen.Imagen(imagenes.obtener_imagen_fantasma("sad", tamCuadro+8, tamCuadro+8), x, y, tamCuadro+8, tamCuadro+8)
                            screen.blit(imag.imagen, (imag.i, imag.j))
                        if self.mapa_imagenes[i][j].id == fantasma3:
                            imag = Imagen.Imagen(imagenes.obtener_imagen_fantasma("inky", tamCuadro+8, tamCuadro+8), x, y, tamCuadro+8, tamCuadro+8)
                            if powerP == True:
                                imag = Imagen.Imagen(imagenes.obtener_imagen_fantasma("sad", tamCuadro+8, tamCuadro+8), x, y, tamCuadro+8, tamCuadro+8)
                            screen.blit(imag.imagen, (imag.i, imag.j))
                        if self.mapa_imagenes[i][j].id == fantasma4:
                            imag = Imagen.Imagen(imagenes.obtener_imagen_fantasma("clyde", tamCuadro+8, tamCuadro+8), x, y, tamCuadro+8, tamCuadro+8)
                            if powerP == True:
                                imag = Imagen.Imagen(imagenes.obtener_imagen_fantasma("sad", tamCuadro+8, tamCuadro+8), x, y, tamCuadro+8, tamCuadro+8)
                            screen.blit(imag.imagen, (imag.i, imag.j))
            if self.validar_dire(self,dire2,posicion_x_pacman,posicion_y_pacman)==True:
                dire = dire2
                dire2 = ""
            if self.validar_dire(self,dire,posicion_x_pacman,posicion_y_pacman)==False:
                dire2 = ""

            self.moverPacman(self,dire,posicion_x_pacman,posicion_y_pacman, tamCuadro, imagenes)
            self.pacman = self.mapa_imagenes[posicion_x_pacman][posicion_y_pacman]
            bandera = True
            primera_vandera = False

            if bandera_hilo == True:
                
                self.hilo(self,d, '1',0.1, validaciones)
                self.hilo(self,d, '4',0.4, validaciones)
                self.hilo(self,d, '2',0.3, validaciones)
                self.hilo(self,d, '3',0.4, validaciones)
                
                
                bandera_hilo = False
            
            pygame.display.flip()
            
            #time.sleep(0.15)
            clock.tick(8)
        pygame.quit()

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

    def hilo(self, algoridmo, fantasma, dalay,validaciones):
        a = HiloFantasma.HiloFantasma(dalay,self.mapa_imagenes,algoridmo,self.nodos,self.ruta,fantasma, self.pacman, self.respaldo, self.fantasmas,validaciones)
        a.start()

    def moverPacman(self,dire,posicion_x_pacman,posicion_y_pacman, tamCuadro, imagenes):
        val = False
        if dire == "RIGHT":
            x=posicion_x_pacman
            y=posicion_y_pacman
            if posicion_y_pacman+1 >= len(self.mapa_imagenes):
                y = -1
            if(self.mapa_imagenes[posicion_x_pacman][y+1].tipo!='#'):
                self.validar_Muerte(self,posicion_x_pacman,y+1)
                self.mapa_imagenes[x][y+1].imagen.imagen = imagenes.obtener_imagen("pacman", tamCuadro+8, tamCuadro+8)
                self.mapa_imagenes[x][y+1].imagen.i -= 4
                self.mapa_imagenes[x][y+1].imagen.j -= 4
                self.mapa_imagenes[x][y+1].tipo = '@'
                val = True
                
        elif dire == "LEFT":
            if(self.mapa_imagenes[posicion_x_pacman][posicion_y_pacman-1].tipo!='#'):
                self.validar_Muerte(self,posicion_x_pacman,posicion_y_pacman-1)
                self.mapa_imagenes[posicion_x_pacman][posicion_y_pacman-1].imagen.imagen = imagenes.obtener_imagen("pacman", tamCuadro+8, tamCuadro+8)
                self.mapa_imagenes[posicion_x_pacman][posicion_y_pacman-1].tipo = '@'
                self.mapa_imagenes[posicion_x_pacman][posicion_y_pacman-1].imagen.i -= 4
                self.mapa_imagenes[posicion_x_pacman][posicion_y_pacman-1].imagen.j -= 4
                val = True
                
        elif dire == "DOWN":
            if(self.mapa_imagenes[posicion_x_pacman+1][posicion_y_pacman].tipo!='#'):
                self.validar_Muerte(self,posicion_x_pacman+1,posicion_y_pacman)
                self.mapa_imagenes[posicion_x_pacman+1][posicion_y_pacman].imagen.imagen = imagenes.obtener_imagen("pacman", tamCuadro+8, tamCuadro+8)
                self.mapa_imagenes[posicion_x_pacman+1][posicion_y_pacman].tipo = '@'
                self.mapa_imagenes[posicion_x_pacman+1][posicion_y_pacman].imagen.i -= 4
                self.mapa_imagenes[posicion_x_pacman+1][posicion_y_pacman].imagen.j -= 4
                val = True
                
        elif dire == "UP":
            if(self.mapa_imagenes[posicion_x_pacman-1][posicion_y_pacman].tipo!='#'):
                self.validar_Muerte(self,posicion_x_pacman-1,posicion_y_pacman)
                self.mapa_imagenes[posicion_x_pacman-1][posicion_y_pacman].imagen.imagen = imagenes.obtener_imagen("pacman", tamCuadro+8, tamCuadro+8)
                self.mapa_imagenes[posicion_x_pacman-1][posicion_y_pacman].tipo = '@'
                self.mapa_imagenes[posicion_x_pacman-1][posicion_y_pacman].imagen.i -= 4
                self.mapa_imagenes[posicion_x_pacman-1][posicion_y_pacman].imagen.j -= 4
                val = True
        if val == True:
            self.mapa_imagenes[posicion_x_pacman][posicion_y_pacman].imagen.imagen = imagenes.obtener_imagen("nada", tamCuadro, tamCuadro)
            self.mapa_imagenes[posicion_x_pacman][posicion_y_pacman].imagen.i += 4
            self.mapa_imagenes[posicion_x_pacman][posicion_y_pacman].imagen.j += 4
            self.mapa_imagenes[posicion_x_pacman][posicion_y_pacman].tipo = ''
            self.respaldo[posicion_x_pacman][posicion_y_pacman]=''
    
    #hilo_terminado = False
    #def hilo_Movimientos(self, inicio, fin, camino, x1, screen):
    #    global hilo_terminado
    #    if x1 < len(camino):
    #        self.mapa_imagenes[camino[x1].x][camino[x1].y].imagen.setImagen("otros/FantasmaA")
    #        self.mapa_imagenes[camino[x1].x][camino[x1].y].tipo = ''
    #        imag = self.mapa_imagenes[camino[x1].x][camino[x1].y].imagen
    #        screen.blit(imag.imagen, (imag.x, imag.y))
    #        if x1-1 > 0:
    #            if self.mapaJ[camino[x1-1].x][camino[x1-1].y] == '_':
    #                self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].imagen.setImagen("otros/bolas")
    #                self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].tipo = '_'
    #            else:
    #                self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].imagen.setImagen("otros/Nada")
    #                self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].tipo = '-'
    #            imag = self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].imagen
    #            screen.blit(imag.imagen, (imag.x, imag.y))
    #    hilo_terminado = True
    def validar_Muerte(self,posicion_x_pacman,posicion_y_pacman):
        if self.mapa_imagenes[posicion_x_pacman][posicion_y_pacman].tipo == '4':
            print("Comio")

