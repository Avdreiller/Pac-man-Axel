import pygame
import Nodo
import Mapa
import Imagen
class Juego(object):
    """description of class"""
    nodos = []
    mapaJ = None

    def llenar_lista_nodos(self):
        mapa = Mapa.Mapa
        m = mapa.generar_Mapa(mapa)
        self.mapaJ = m
        contador = 1
        for i in range(len(m)):
            for j in range(len(m)):
                n = Nodo.Nodo(contador, m[i][j], None)
                self.nodos.append(n)
                contador += 1
    def validar(self,mposx,mposy,posx,posy):
        sumax = mposx + posx;
        sumay = mposy + posy;
        if sumax < 0 or sumax > 22 or sumay < 0 or sumay > 22:
            return False
        else:
            if self.mapaJ[sumax][sumay]=='#':
                return True
        return False

    def asignar_Muro(self, mposx, mposy,i,j,tamCuadro):

        if self.validar(self,mposx, mposy,0,1) == True and self.validar(self,mposx, mposy,0,-1) == True and self.validar(self,mposx, mposy,1,0) == True and self.validar(self,mposx, mposy,-1,0) == True:
            return Imagen.Imagen("muros/Intersección", i+160, j+110, tamCuadro, tamCuadro)
        if self.validar(self,mposx, mposy,0,1) == False and self.validar(self,mposx, mposy,0,-1) == False and self.validar(self,mposx, mposy,1,0) == False and self.validar(self,mposx, mposy,-1,0) == False:
            return Imagen.Imagen("muros/MuroSolo", i+160, j+110, tamCuadro, tamCuadro)
        if self.validar(self,mposx, mposy,0,1) == True and self.validar(self,mposx, mposy,0,-1) == False and self.validar(self,mposx, mposy,1,0) == False and self.validar(self,mposx, mposy,-1,0) == False:
            return Imagen.Imagen("muros/FinalIzquierdo", i+160, j+110, tamCuadro, tamCuadro)
        if self.validar(self,mposx, mposy,0,1) == False and self.validar(self,mposx, mposy,0,-1) == True and self.validar(self,mposx, mposy,1,0) == False and self.validar(self,mposx, mposy,-1,0) == False:
            return Imagen.Imagen("muros/FinalDerecho", i+160, j+110, tamCuadro, tamCuadro)
        if self.validar(self,mposx, mposy,0,1) == False and self.validar(self,mposx, mposy,0,-1) == False and self.validar(self,mposx, mposy,1,0) == True and self.validar(self,mposx, mposy,-1,0) == False:
            return Imagen.Imagen("muros/FinalSuperior", i+160, j+110, tamCuadro, tamCuadro)
        if self.validar(self,mposx, mposy,0,1) == False and self.validar(self,mposx, mposy,0,-1) == False and self.validar(self,mposx, mposy,1,0) == False and self.validar(self,mposx, mposy,-1,0) == True:
            return Imagen.Imagen("muros/FinalInferior", i+160, j+110, tamCuadro, tamCuadro)
        if self.validar(self,mposx, mposy,0,1) == True and self.validar(self,mposx, mposy,0,-1) == True and self.validar(self,mposx, mposy,1,0) == False and self.validar(self,mposx, mposy,-1,0) == False:
            return Imagen.Imagen("muros/MuroIntermedioHorizontal", i+160, j+110, tamCuadro, tamCuadro)
        if self.validar(self,mposx, mposy,0,1) == False and self.validar(self,mposx, mposy,0,-1) == False and self.validar(self,mposx, mposy,1,0) == True and self.validar(self,mposx, mposy,-1,0) == True:
            return Imagen.Imagen("muros/MuroIntermedioVertical", i+160, j+110, tamCuadro, tamCuadro)
        if self.validar(self,mposx, mposy,0,1) == True and self.validar(self,mposx, mposy,0,-1) == False and self.validar(self,mposx, mposy,1,0) == True and self.validar(self,mposx, mposy,-1,0) == False:
            return Imagen.Imagen("muros/EsquinaSuperiorIzquierda", i+160, j+110, tamCuadro, tamCuadro)
        if self.validar(self,mposx, mposy,0,1) == False and self.validar(self,mposx, mposy,0,-1) == True and self.validar(self,mposx, mposy,1,0) == False and self.validar(self,mposx, mposy,-1,0) == True:
            return Imagen.Imagen("muros/EsquinaInferiorDerecha", i+160, j+110, tamCuadro, tamCuadro)
        if self.validar(self,mposx, mposy,0,1) == True and self.validar(self,mposx, mposy,0,-1) == False and self.validar(self,mposx, mposy,1,0) == False and self.validar(self,mposx, mposy,-1,0) == True:
            return Imagen.Imagen("muros/EsquinaInferiorIzquierda", i+160, j+110, tamCuadro, tamCuadro)
        if self.validar(self,mposx, mposy,0,1) == False and self.validar(self,mposx, mposy,0,-1) == True and self.validar(self,mposx, mposy,1,0) == True and self.validar(self,mposx, mposy,-1,0) == False:
            return Imagen.Imagen("muros/EsquinaSuperiorDerecha", i+160, j+110, tamCuadro, tamCuadro)
        if self.validar(self,mposx, mposy,0,1) == True and self.validar(self,mposx, mposy,0,-1) == True and self.validar(self,mposx, mposy,1,0) == True and self.validar(self,mposx, mposy,-1,0) == False:
            return Imagen.Imagen("muros/IntersecciónSuperior", i+160, j+110, tamCuadro, tamCuadro)
        if self.validar(self,mposx, mposy,0,1) == False and self.validar(self,mposx, mposy,0,-1) == True and self.validar(self,mposx, mposy,1,0) == True and self.validar(self,mposx, mposy,-1,0) == True:
            return Imagen.Imagen("muros/IntersecciónDerecha", i+160, j+110, tamCuadro, tamCuadro)
        if self.validar(self,mposx, mposy,0,1) == True and self.validar(self,mposx, mposy,0,-1) == False and self.validar(self,mposx, mposy,1,0) == True and self.validar(self,mposx, mposy,-1,0) == True:
            return Imagen.Imagen("muros/IntersecciónIzquierda", i+160, j+110, tamCuadro, tamCuadro)
        if self.validar(self,mposx, mposy,0,1) == True and self.validar(self,mposx, mposy,0,-1) == True and self.validar(self,mposx, mposy,1,0) == False and self.validar(self,mposx, mposy,-1,0) == True:
            return Imagen.Imagen("muros/IntersecciónInferior", i+160, j+110, tamCuadro, tamCuadro)
        

    def pantalla_juego(self):
        posicion_x_pacman = 0
        posicion_y_pacman = 0
        bandera = True

        self.llenar_lista_nodos(self)
        m = Mapa.Mapa
        m.generar_Mapa(m)
        #for x in range(len(self.nodos)):
        #    print(self.nodos[x].id,self.nodos[x].tipo)
        pygame.init()
        
        AZUL = (0, 0, 255)
        BLACK = (0, 0, 0)
        tamCuadro = 21
 
        mapa_imagenes = []
        for x in range(23):
            mapa_imagenes.append([])
            for j in range(23):
                mapa_imagenes[x].append(Nodo.Nodo(0,'',None))
        
        size = (820, 720)
        screen = pygame.display.set_mode(size)
        #pygame.key.set_repeat(500,30)
        pygame.display.set_caption("Grid on PYGAME")
        clock = pygame.time.Clock()
        gameOver = True
        logo = pygame.image.load("recursos/muros/MuroSolo.png")
        logo = pygame.transform.scale(logo, (tamCuadro,tamCuadro))
        primera_vandera = True
        while gameOver:
           
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and bandera == True:
                    bandera = False
                    self.moverPacman(self,event,posicion_x_pacman,posicion_y_pacman,bandera)
                if event.type == pygame.QUIT:
                    gameOver = False
            bandera = True
            screen.fill(BLACK)
            i1 = 0
            id = 1
            for i in range(1, 500, tamCuadro + 1):
                j1 = 0
                if i1 < 23:
                    for j in range(1, 500, tamCuadro+1):
                        #pygame.draw.rect(screen, AZUL, [i, j, tamCuadro, tamCuadro], 0)
                        if j1 < 23:
                            if primera_vandera == True:
                                if self.mapaJ[j1][i1]=='#':
                                    img = self.asignar_Muro(self,j1,i1,i,j,tamCuadro+10)
                                    n = Nodo.Nodo(id,self.mapaJ[j1][i1],img)
                                    mapa_imagenes[j1][i1] = n
                                    if img != None:
                                        screen.blit(img.imagen, (i+155, j+105))
                                if self.mapaJ[j1][i1]=='@':
                                    posicion_x_pacman = j1
                                    posicion_y_pacman = i1
                                    imagen = Imagen.Imagen("otros/PacMan", i+160, j+110, tamCuadro+8, tamCuadro+8)
                                    screen.blit(imagen.imagen, (i+156, j+106))
                                    n = Nodo.Nodo(id,self.mapaJ[j1][i1],imagen)
                                    mapa_imagenes[j1][i1] = n
                                if self.mapaJ[j1][i1]=='_' or self.mapaJ[j1][i1]=='-':
                                    imagen = Imagen.Imagen("otros/bolas", i+160, j+110, tamCuadro, tamCuadro)
                                    screen.blit(imagen.imagen, (i+160, j+110))
                                    n = Nodo.Nodo(id,self.mapaJ[j1][i1],imagen)
                                    mapa_imagenes[j1][i1] = n
                                id += 1
                            else:
                                
                                if self.mapaJ[j1][i1]=='#':
                                    if img != None:
                                        screen.blit(mapa_imagenes[j1][i1].imagen.imagen, (i+155, j+105))
                                if self.mapaJ[j1][i1]=='@':
                                    posicion_x_pacman = j1
                                    posicion_y_pacman = i1
                                    imagen = Imagen.Imagen("otros/PacMan", i+160, j+110, tamCuadro+8, tamCuadro+8)
                                    screen.blit(imagen.imagen, (i+156, j+106))
                                if self.mapaJ[j1][i1]=='_' or self.mapaJ[j1][i1]=='-':
                                    imagen = Imagen.Imagen("otros/bolas", i+160, j+110, tamCuadro, tamCuadro)
                                    screen.blit(imagen.imagen, (i+160, j+110))
                            j1 += 1
                    i1 += 1
            primera_vandera = False
            pygame.display.flip()
            #clock.tick(1)
        pygame.quit()


    def moverPacman(self,evento,posicion_x_pacman,posicion_y_pacman,bandera):
        
        if evento.key == pygame.K_RIGHT:
            if(self.mapaJ[posicion_x_pacman][posicion_y_pacman+1]!='#'):
                self.mapaJ[posicion_x_pacman][posicion_y_pacman+1]='@'
                self.mapaJ[posicion_x_pacman][posicion_y_pacman]=''
            
        elif evento.key == pygame.K_LEFT:
            if(self.mapaJ[posicion_x_pacman][posicion_y_pacman-1]!='#'):
                self.mapaJ[posicion_x_pacman][posicion_y_pacman-1]='@'
                self.mapaJ[posicion_x_pacman][posicion_y_pacman]=''
        elif evento.key == pygame.K_DOWN:
            if(self.mapaJ[posicion_x_pacman+1][posicion_y_pacman]!='#'):
                self.mapaJ[posicion_x_pacman+1][posicion_y_pacman]='@'
                self.mapaJ[posicion_x_pacman][posicion_y_pacman]=''
        elif evento.key == pygame.K_UP:
            if(self.mapaJ[posicion_x_pacman-1][posicion_y_pacman]!='#'):
                self.mapaJ[posicion_x_pacman-1][posicion_y_pacman]='@'
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
