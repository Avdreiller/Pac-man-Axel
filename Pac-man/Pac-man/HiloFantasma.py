from random import randrange
import threading
import time
import Imagenes

TOTAL = 0

MY_LOCK = threading.Lock()
class HiloFantasma(threading.Thread):
    def __init__(self, delay, mapa_imagenes, algoritmo, nodos, ruta, fantasma, jugador, respaldo,fantasmas):
        threading.Thread.__init__(self)
        self.delay = delay
        self.mapa_imagenes = mapa_imagenes
        self.algoritmo = algoritmo
        self.nodos = nodos
        self.ruta = ruta
        self.fantasma = fantasma
        self.jugador = jugador
        self.respaldo = respaldo
        self.fantasmas = fantasmas

    def run(self):
        imagenes = Imagenes.Imagenes()
        global TOTAL
        x1 = 1
        posicion_x_fantasma = -1
        posicion_y_fantasma = -1
        conta = 0
        fin = True
        seg_jugador = False
        fant = 0
        if self.fantasma == '2':
            fant = 1
            time.sleep(0.5)
        elif self.fantasma == '3':
            fant = 2
            time.sleep(1)
        elif self.fantasma == '1':
            fant = 0
        elif self.fantasma == '4':
            fant = 3
        while True:
            time.sleep(self.delay)
            MY_LOCK.acquire()
            idJ = 0
            idF = 0
            idF1 = 0
            idF2 = 0
            idF4 = 0
            valr = False
            for k in range(len(self.fantasmas)):
                for x in range(len(self.fantasmas[k])):
                    if self.fantasmas[k][x] == self.fantasma and k == fant:
                        idF = x
                    if self.fantasmas[k][x]=='1'and k==0:
                        idF1 = x
                    if self.fantasmas[k][x]=='2' and k==1:
                        idF2 = x
                    if self.fantasmas[k][x]=='4'and k==3:
                        idF4 = x
                    
                    #valr = True
                    
                    #posicion_x_fantasma = self.fantasmas[0][x].x
                    #posicion_y_fantasma = self.fantasmas[0][x].y
            for i in range(len(self.mapa_imagenes)):
                for j in range(len(self.mapa_imagenes)):
                    if self.mapa_imagenes[i][j].tipo == '@':
                        idJ = self.mapa_imagenes[i][j].id
                    #if self.mapa_imagenes[i][j].tipo == self.fantasma:
                        #valr = True
                        #posicion_x_fantasma = i
                        #posicion_y_fantasma = j
                    if self.mapa_imagenes[i][j].id == idF:
                        posicion_x_fantasma = i
                        posicion_y_fantasma = j
                    #if self.mapa_imagenes[i][j].tipo == '1':
                    #    idF1 = self.mapa_imagenes[i][j].id
                    #if self.mapa_imagenes[i][j].tipo == '2':
                    #    idF2 = self.mapa_imagenes[i][j].id
                    #if self.mapa_imagenes[i][j].tipo == '4':
                    #    idF4 = self.mapa_imagenes[i][j].id

            #if valr == True:    
                #idF = self.mapa_imagenes[posicion_x_fantasma][posicion_y_fantasma].id
            #else:
                #idF = self.mapa_imagenes[posicion_x_fantasma][posicion_y_fantasma].id

            if self.fantasma == '4':
                if fin == True:
                    ran = randrange(len(self.nodos))
                    camino = self.algoritmo.getCamino(self.algoritmo, self.nodos[ran], self.nodos[idF], self.ruta, self.nodos)
                    fin = False
                    x1 = 1
            elif self.fantasma == '3':
                if fin == True:
                    ran = randrange(100)
                
                    
                    if ran < 45:
                        #camino = self.algoritmo.getCamino(self.algoritmo, self.nodos[idJ], self.nodos[idF], self.ruta, self.nodos)
                        seg_jugador = True
                        #x1 = 1
                        #fin = True
                        #x1 = 1
                    elif ran >= 45 and ran <=45:
                        if fin == True:
                            ran = randrange(len(self.nodos))
                            camino = self.algoritmo.getCamino(self.algoritmo, self.nodos[ran], self.nodos[idF], self.ruta, self.nodos)
                            fin = False
                            x1 = 1

                    elif ran > 45:
                        ran1 = randrange(3)
                        if ran1 == 0:
                            camino = self.algoritmo.getCamino(self.algoritmo, self.nodos[idF1], self.nodos[idF], self.ruta, self.nodos)
                        elif ran1 == 1:
                            camino = self.algoritmo.getCamino(self.algoritmo, self.nodos[idF2], self.nodos[idF], self.ruta, self.nodos)
                        elif ran1 == 2:
                            camino = self.algoritmo.getCamino(self.algoritmo, self.nodos[idF4], self.nodos[idF], self.ruta, self.nodos)
                        else:
                            print("No Entro al segundo rando")
                        fin = True
                        x1 = 1
                    else:
                        print("No Entro al primer rando")


            else:
                #camino = self.algoritmo.getCamino(self.algoritmo, self.nodos[idJ], self.nodos[idF], self.ruta, self.nodos)
                seg_jugador = True
                #x1 = 1
            if seg_jugador == True:
                camino = self.algoritmo.getCamino(self.algoritmo, self.nodos[idJ], self.nodos[idF], self.ruta, self.nodos)
                fin = True
                seg_jugador = False
                x1 = 1
            if x1 < len(camino):
                
                if self.mapa_imagenes[camino[x1].x][camino[x1].y].tipo != '@':
                    id = self.mapa_imagenes[camino[x1].x][camino[x1].y].id
                    
                    if self.fantasmas[fant][id] != self.fantasma:
                        self.fantasmas[fant][id] = self.fantasma
                        posicion_x_fantasma = camino[x1].x
                        posicion_y_fantasma = camino[x1].y
                        if x1 > 0:
                            id2 = self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].id
                            if self.respaldo[camino[x1-1].x][camino[x1-1].y] == '_':
                                self.fantasmas[fant][id2] = '_'
                            else:
                                self.fantasmas[fant][id2] = '-'
                    #elif self.fantasma == '2':
                    #    self.mapa_imagenes[camino[x1].x][camino[x1].y].imagen.imagen = imagenes.obtener_imagen_fantasma("pinky", 29, 29)
                    #elif self.fantasma == '3':
                    #    self.mapa_imagenes[camino[x1].x][camino[x1].y].imagen.imagen = imagenes.obtener_imagen_fantasma("inky", 29, 29)
                    #elif self.fantasma == '4':
                    #    self.mapa_imagenes[camino[x1].x][camino[x1].y].imagen.imagen = imagenes.obtener_imagen_fantasma("clyde", 29, 29)
                    
                    #if self.mapa_imagenes[camino[x1].x][camino[x1].y] != self.fantasma:
                    #    self.mapa_imagenes[camino[x1].x][camino[x1].y].imagen.i = self.nodos[id].imagen.i-4
                    #    self.mapa_imagenes[camino[x1].x][camino[x1].y].imagen.j = self.nodos[id].imagen.j-4
                    #    self.mapa_imagenes[camino[x1].x][camino[x1].y].tipo = self.fantasma
                    #    posicion_x_fantasma = camino[x1].x
                    #    posicion_y_fantasma = camino[x1].y

                    
                    #    if x1 > 0:
                    #        if self.respaldo[camino[x1-1].x][camino[x1-1].y] == '_':
                    #            self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].imagen.imagen = imagenes.obtener_imagen("bola", 21, 21)
                    #            self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].tipo = '_'
                        
                    #        else:
                    #            self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].imagen.imagen = imagenes.obtener_imagen("nada", 21, 21)
                    #            self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].tipo = '-'
                    #        id = self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].id
                    #        self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].imagen.i = self.nodos[id].imagen.i+4
                    #        self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].imagen.j = self.nodos[id].imagen.j+4
                        
                if fin == False:
                    x1 += 1
            else:
                fin = True
        

            TOTAL = TOTAL + 1

            MY_LOCK.release()
            
        


