import pygame
import Nodo
import Mapa
import Imagen
import Imagenes
import Relacion
import Floyd
import threading
import time
class Juego(object):
    """description of class"""
    nodos = []
    mapaJ = None
    ruta = []

    def llenar_lista_nodos(self):
        mapa = Mapa.Mapa
        m = mapa.generar_Mapa(mapa)
        self.mapaJ = m
        contador = 0
        for i in range(len(m)):
            for j in range(len(m)):
                if m[i][j] != '#' and m[i][j] != ' ':
                    n = Nodo.Nodo(contador, m[i][j], None, i, j)
                    self.nodos.append(n)
                    contador += 1
        for x in range(len(self.nodos)):
            self.ruta.append([])
            for j in range(len(self.nodos)):
                self.ruta[x].append(0)
        for i in range(len(self.nodos)):
            for j in range(len(self.nodos)):
                i1,j1 = self.nodos[i].x, self.nodos[i].y
                i2,j2 = self.nodos[j].x, self.nodos[j].y
                if (i1,j1+1)==(i2,j2) or (i1,j1-1)==(i2,j2) or (i1+1,j1)==(i2,j2) or (i1-1,j1)==(i2,j2):
                    self.ruta[i][j] = 1
                
    def validar(self,mposx,mposy,posx,posy):
        sumax = mposx + posx;
        sumay = mposy + posy;
        if sumax < 0 or sumax > 22 or sumay < 0 or sumay > 22:
            return False
        else:
            if self.mapaJ[sumax][sumay]=='#':
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
        
        self.llenar_lista_nodos(self)

        

        #m = Mapa.Mapa
        #m.generar_Mapa(m)
        #for x in range(len(self.nodos)):
        #    print(self.nodos[x].id,self.nodos[x].tipo)

        f = Floyd.Floyd
        camino = []
        f.pasarPesos(f,self.ruta)

        #print(self.nodos[0].x,self.nodos[0].y,"-------------")
        camino = f.getCamino(f, self.nodos[1], self.nodos[140], self.ruta, self.nodos)
        
        
        pygame.init()
        
        AZUL = (0, 0, 255)
        BLACK = (0, 0, 0)
        tamCuadro = 21
        imagenes = Imagenes.Imagenes(tamCuadro,tamCuadro)
        mapa_imagenes = []
        for x in range(23):
            mapa_imagenes.append([])
            for j in range(23):
                mapa_imagenes[x].append(Nodo.Nodo(0,'',None,0,0))
        
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
        while gameOver:
            
            #for x in range(len(camino)):
            
            
            screen.fill(BLACK)
            i1 = 0
            id = 0
            for j in range(1, 500, tamCuadro + 1):
                j1 = 0
                if i1 < 23:
                    for i in range(1, 500, tamCuadro+1):
                        if j1 < 23:
                            if primera_vandera == True:   
                                if self.mapaJ[i1][j1]=='#':
                                    img = self.asignar_Muro(self,i1,j1,i,j,tamCuadro+10,imagenes)
                                    n = Nodo.Nodo(id,self.mapaJ[i1][j1],img, i1, j1)
                                    mapa_imagenes[i1][j1] = n
                                    if img != None:
                                        screen.blit(img.imagen, (i+155, j+105))
                                        
                                
                                #imagen = pygame.image.load("recursos/muros/MuroSolo.png").convert_alpha()
                                #imagen = pygame.transform.scale(imagen,(tamCuadro,tamCuadro))
                                #screen.blit(imagen, (i+156, j+106))

                                if self.mapaJ[i1][j1]=='@':
                                    posicion_x_pacman = i1
                                    posicion_y_pacman = j1
                                    n = Nodo.Nodo(id,self.mapaJ[i1][j1],Imagen.Imagen(imagenes.obtener_imagen("pacman", tamCuadro+8, tamCuadro+8), i+156, j+106, tamCuadro+8, tamCuadro+8), i1, j1)
                                    mapa_imagenes[i1][j1] = n
                                    screen.blit(mapa_imagenes[i1][j1].imagen.imagen, (mapa_imagenes[i1][j1].imagen.x, mapa_imagenes[i1][j1].imagen.y))
                                    #imagen = pygame.image.load("recursos/otros/PacMan.png").convert_alpha()
                                    #imagen = pygame.transform.scale(imagen,(tamCuadro,tamCuadro))
                                    #screen.blit(imagen, (i+156, j+106))
                                if self.mapaJ[i1][j1]=='_':
                                
                                    n = Nodo.Nodo(id,self.mapaJ[i1][j1],Imagen.Imagen(imagenes.obtener_imagen("bola", tamCuadro, tamCuadro), i+160, j+110, tamCuadro, tamCuadro), i1, j1)
                                    mapa_imagenes[i1][j1] = n
                                    screen.blit(mapa_imagenes[i1][j1].imagen.imagen, (mapa_imagenes[i1][j1].imagen.x, mapa_imagenes[i1][j1].imagen.y))
                                    #imagen = pygame.image.load("recursos/otros/bolas.png").convert_alpha()
                                    #imagen = pygame.transform.scale(imagen,(tamCuadro,tamCuadro))
                                    #screen.blit(imagen, (i+160, j+110))
                                
                                if self.mapaJ[i1][j1]==''or self.mapaJ[i1][j1]==' 'or self.mapaJ[i1][j1]=='-'or self.mapaJ[i1][j1]=='1'or self.mapaJ[i1][j1]=='2'or self.mapaJ[i1][j1]=='3'or self.mapaJ[i1][j1]=='4':
                                    n = Nodo.Nodo(id,self.mapaJ[i1][j1],Imagen.Imagen(imagenes.obtener_imagen("nada", tamCuadro, tamCuadro), i+160, j+110, tamCuadro, tamCuadro), i1, j1)
                                    mapa_imagenes[i1][j1] = n
                                    screen.blit(mapa_imagenes[i1][j1].imagen.imagen, (mapa_imagenes[i1][j1].imagen.x, mapa_imagenes[i1][j1].imagen.y))
                                    #imagen = pygame.image.load("recursos/otros/Nada.png").convert_alpha()
                                    #imagen = pygame.transform.scale(imagen,(tamCuadro,tamCuadro))
                                    #screen.blit(imagen, (i+160, j+110))
                                id += 1
                            else:
                                #if self.mapaJ[i1][j1]=='#':
                                #    imag = mapa_imagenes[i1][j1].imagen
                                #    screen.blit(imag.imagen, (imag.x, imag.y))
                                #if self.mapaJ[i1][j1]=='@':
                                #    imag = mapa_imagenes[i1][j1].imagen
                                #    screen.blit(imag.imagen, (imag.x, imag.y))
                                #if self.mapaJ[i1][j1]=='_':
                                #    imag = mapa_imagenes[i1][j1].imagen
                                #    screen.blit(imag.imagen, (imag.x, imag.y))
                                #if self.mapaJ[i1][j1]==''or self.mapaJ[i1][j1]==' 'or self.mapaJ[i1][j1]=='-':
                                if mapa_imagenes[i1][j1].tipo=='@':
                                    posicion_x_pacman = i1
                                    posicion_y_pacman = j1
                                imag = mapa_imagenes[i1][j1].imagen
                                screen.blit(imag.imagen, (imag.x, imag.y))
                            
                            
                            j1 += 1
                    i1 += 1
            #for i in range(len(mapa_imagenes)):
            #    for j in range(len(mapa_imagenes)):
            #        if mapa_imagenes[i][j].tipo == '':
            #            print(" ", end="")
            #        else:
            #            print(mapa_imagenes[i][j].tipo,end="")
            #    print("")
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and bandera == True:
                    bandera = False
                    if event.key == pygame.K_RIGHT:
                        if(mapa_imagenes[posicion_x_pacman][posicion_y_pacman+1].tipo!='#'):
                            dire = "RIGHT"
                        else:
                            dire2 = "RIGHT"
                    elif event.key == pygame.K_LEFT:
                        if(mapa_imagenes[posicion_x_pacman][posicion_y_pacman-1].tipo!='#'):
                            dire = "LEFT"
                        else:
                            dire2 = "LEFT"
                    elif event.key == pygame.K_DOWN:
                        if(mapa_imagenes[posicion_x_pacman+1][posicion_y_pacman].tipo!='#'):
                            dire = "DOWN"
                        else:
                            dire2 = "DOWN"
                    elif event.key == pygame.K_UP:
                        if(mapa_imagenes[posicion_x_pacman-1][posicion_y_pacman].tipo!='#'):
                            dire = "UP"
                        else:
                            dire2 = "UP"
                    
                if event.type == pygame.QUIT:
                    gameOver = False
            if self.validar_dire(self,dire2,posicion_x_pacman,posicion_y_pacman,  mapa_imagenes)==True:
                dire = dire2
                dire2 = ""
            self.moverPacman(self,dire,posicion_x_pacman,posicion_y_pacman, mapa_imagenes, tamCuadro, imagenes)
            bandera = True
            primera_vandera = False
            self.hilo_Movimientos(self,1,10,camino, x1, mapa_imagenes,screen)
            x1 += 1
            if x1 == len(camino):
                x1 = 0
            pygame.display.flip()
            
            time.sleep(0.15)
            #clock.tick(0.5)
        pygame.quit()

    def validar_dire(self, dire2,posicion_x_pacman,posicion_y_pacman, mapa_imagenes):
        if dire2 == "RIGHT":
            if(mapa_imagenes[posicion_x_pacman][posicion_y_pacman+1].tipo!='#'):
                return True
        elif dire2 == "LEFT":
            if(mapa_imagenes[posicion_x_pacman][posicion_y_pacman-1].tipo!='#'):
                return True
        elif dire2 == "DOWN":
            if(mapa_imagenes[posicion_x_pacman+1][posicion_y_pacman].tipo!='#'):
                return True
        elif dire2 == "UP":
            if(mapa_imagenes[posicion_x_pacman-1][posicion_y_pacman].tipo!='#'):
                return True
        return False

    def moverPacman(self,dire,posicion_x_pacman,posicion_y_pacman, mapa_imagenes, tamCuadro, imagenes):
        
        if dire == "RIGHT":
            if(mapa_imagenes[posicion_x_pacman][posicion_y_pacman+1].tipo!='#'):
                #self.mapaJ[posicion_x_pacman][posicion_y_pacman+1]='@'
                mapa_imagenes[posicion_x_pacman][posicion_y_pacman+1].imagen.imagen = imagenes.obtener_imagen("pacman", tamCuadro+8, tamCuadro+8)
                mapa_imagenes[posicion_x_pacman][posicion_y_pacman+1].imagen.x -= 4
                mapa_imagenes[posicion_x_pacman][posicion_y_pacman+1].imagen.y -= 4
                mapa_imagenes[posicion_x_pacman][posicion_y_pacman+1].tipo = '@'
                mapa_imagenes[posicion_x_pacman][posicion_y_pacman].imagen.imagen = imagenes.obtener_imagen("nada", tamCuadro, tamCuadro)
                mapa_imagenes[posicion_x_pacman][posicion_y_pacman].imagen.x += 4
                mapa_imagenes[posicion_x_pacman][posicion_y_pacman].imagen.y += 4
                mapa_imagenes[posicion_x_pacman][posicion_y_pacman].tipo = ''
                self.mapaJ[posicion_x_pacman][posicion_y_pacman]=''
        elif dire == "LEFT":
            if(mapa_imagenes[posicion_x_pacman][posicion_y_pacman-1].tipo!='#'):
                mapa_imagenes[posicion_x_pacman][posicion_y_pacman-1].imagen.imagen = imagenes.obtener_imagen("pacman", tamCuadro+8, tamCuadro+8)
                mapa_imagenes[posicion_x_pacman][posicion_y_pacman-1].tipo = '@'
                mapa_imagenes[posicion_x_pacman][posicion_y_pacman-1].imagen.x -= 4
                mapa_imagenes[posicion_x_pacman][posicion_y_pacman-1].imagen.y -= 4
                mapa_imagenes[posicion_x_pacman][posicion_y_pacman].imagen.imagen = imagenes.obtener_imagen("nada", tamCuadro, tamCuadro)
                mapa_imagenes[posicion_x_pacman][posicion_y_pacman].imagen.x += 4
                mapa_imagenes[posicion_x_pacman][posicion_y_pacman].imagen.y += 4
                mapa_imagenes[posicion_x_pacman][posicion_y_pacman].tipo = ''
                #self.mapaJ[posicion_x_pacman][posicion_y_pacman-1]='@'
                self.mapaJ[posicion_x_pacman][posicion_y_pacman]=''
        elif dire == "DOWN":
            if(mapa_imagenes[posicion_x_pacman+1][posicion_y_pacman].tipo!='#'):
                mapa_imagenes[posicion_x_pacman+1][posicion_y_pacman].imagen.imagen = imagenes.obtener_imagen("pacman", tamCuadro+8, tamCuadro+8)
                mapa_imagenes[posicion_x_pacman+1][posicion_y_pacman].tipo = '@'
                mapa_imagenes[posicion_x_pacman+1][posicion_y_pacman].imagen.x -= 4
                mapa_imagenes[posicion_x_pacman+1][posicion_y_pacman].imagen.y -= 4
                mapa_imagenes[posicion_x_pacman][posicion_y_pacman].imagen.imagen = imagenes.obtener_imagen("nada", tamCuadro, tamCuadro)
                mapa_imagenes[posicion_x_pacman][posicion_y_pacman].imagen.x += 4
                mapa_imagenes[posicion_x_pacman][posicion_y_pacman].imagen.y += 4
                mapa_imagenes[posicion_x_pacman][posicion_y_pacman].tipo = ''
                #self.mapaJ[posicion_x_pacman+1][posicion_y_pacman]='@'
                self.mapaJ[posicion_x_pacman][posicion_y_pacman]=''
        elif dire == "UP":
            if(mapa_imagenes[posicion_x_pacman-1][posicion_y_pacman].tipo!='#'):
                mapa_imagenes[posicion_x_pacman-1][posicion_y_pacman].imagen.imagen = imagenes.obtener_imagen("pacman", tamCuadro+8, tamCuadro+8)
                mapa_imagenes[posicion_x_pacman-1][posicion_y_pacman].tipo = '@'
                mapa_imagenes[posicion_x_pacman-1][posicion_y_pacman].imagen.x -= 4
                mapa_imagenes[posicion_x_pacman-1][posicion_y_pacman].imagen.y -= 4
                mapa_imagenes[posicion_x_pacman][posicion_y_pacman].imagen.imagen = imagenes.obtener_imagen("nada", tamCuadro, tamCuadro)
                mapa_imagenes[posicion_x_pacman][posicion_y_pacman].imagen.x += 4
                mapa_imagenes[posicion_x_pacman][posicion_y_pacman].imagen.y += 4
                mapa_imagenes[posicion_x_pacman][posicion_y_pacman].tipo = ''
                #self.mapaJ[posicion_x_pacman-1][posicion_y_pacman]='@'
                self.mapaJ[posicion_x_pacman][posicion_y_pacman]=''
    #    if evento.type == pygame.keyup:
    #        if evento.key == pygame.k_right:
    #            velocidad_auto_x = 0
    #        if evento.key == pygame.k_left:
    #            velocidad_auto_x = 0
    #        if evento.key == pygame.k_down:
    #            velocidad_auto_y = 0
    #        if evento.key == pygame.k_up:
    #            velocidad_auto_y = 0
    #auto[0] += velocidad_auto_x
    #auto[1] += velocidad_auto_y
    hilo_terminado = False
    def hilo_Movimientos(self, inicio, fin, camino, x1, mapa_imagenes, screen):
        # Indica si ha terminado el hilo
        

        # Funcion que se ejecuta en un hilo
        global hilo_terminado
        # Bucle de inicio a fin, con espera de un segundo
        #for valor in range(inicio,fin):
        #print ("Hilo : "+str(valor))
        if x1 < len(camino):
            #print(camino[x1].x,camino[x1].y)
                
                
                
            #i = mapa_imagenes[camino[x1].x][camino[x1].y].imagen.x
            #j = mapa_imagenes[camino[x1].x][camino[x1].y].imagen.y
            #tamCuadro = mapa_imagenes[camino[x1].x][camino[x1].y].imagen.alto
            #imagen = Imagen.Imagen("otros/FantasmaA", i, j, tamCuadro, tamCuadro)
            #self.mapaJ[camino[x1].x][camino[x1].y] = ''
            mapa_imagenes[camino[x1].x][camino[x1].y].imagen.setImagen("otros/FantasmaA")
            mapa_imagenes[camino[x1].x][camino[x1].y].tipo = ''
            imag = mapa_imagenes[camino[x1].x][camino[x1].y].imagen
            screen.blit(imag.imagen, (imag.x, imag.y))
            if x1-1 > 0:
                #self.mapaJ[camino[x1-1].x][camino[x1-1].y] = '_'
                if self.mapaJ[camino[x1-1].x][camino[x1-1].y] == '_':
                    mapa_imagenes[camino[x1-1].x][camino[x1-1].y].imagen.setImagen("otros/bolas")
                    mapa_imagenes[camino[x1-1].x][camino[x1-1].y].tipo = '_'
                else:
                    mapa_imagenes[camino[x1-1].x][camino[x1-1].y].imagen.setImagen("otros/Nada")
                    mapa_imagenes[camino[x1-1].x][camino[x1-1].y].tipo = '-'
                imag = mapa_imagenes[camino[x1-1].x][camino[x1-1].y].imagen
                screen.blit(imag.imagen, (imag.x, imag.y))

            
        #time.sleep(0.01)
        # marca hilo terminado
        hilo_terminado = True
        #print("Terminado hilo ")
