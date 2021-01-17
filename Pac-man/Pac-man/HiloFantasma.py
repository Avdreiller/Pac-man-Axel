from random import randrange
import threading
import time
import Imagenes

TOTAL = 0

MY_LOCK = threading.Lock()
class HiloFantasma(threading.Thread):
    def __init__(self, delay, mapa_imagenes, algoritmo, nodos, ruta, fantasma, jugador, respaldo):
        threading.Thread.__init__(self)
        self.delay = delay
        self.mapa_imagenes = mapa_imagenes
        self.algoritmo = algoritmo
        self.nodos = nodos
        self.ruta = ruta
        self.fantasma = fantasma
        self.jugador = jugador
        self.respaldo = respaldo

    def run(self):
        imagenes = Imagenes.Imagenes()
        global TOTAL
        x1 = 1
        posicion_x_fantasma = -1
        posicion_y_fantasma = -1
        while True:
            time.sleep(self.delay)
            MY_LOCK.acquire()
            idJ = 0
            idF = 0
            valr = False
            for i in range(len(self.mapa_imagenes)):
                for j in range(len(self.mapa_imagenes)):
                    if self.mapa_imagenes[i][j].tipo == '@':
                        idJ = self.mapa_imagenes[i][j].id
                    if self.mapa_imagenes[i][j].tipo == self.fantasma:
                        valr = True
                        posicion_x_fantasma = i
                        posicion_y_fantasma = j
            if valr == True:    
                idF = self.mapa_imagenes[posicion_x_fantasma][posicion_y_fantasma].id
            else:
                idF = self.mapa_imagenes[posicion_x_fantasma][posicion_y_fantasma].id
            if self.fantasma == '4':
                ran = randrange(len(self.nodos))
                camino = self.algoritmo.getCamino(self.algoritmo, self.nodos[ran], self.nodos[idF], self.ruta, self.nodos)
            else:
                camino = self.algoritmo.getCamino(self.algoritmo, self.nodos[idJ], self.nodos[idF], self.ruta, self.nodos)
            if x1 < len(camino):
                
                if self.mapa_imagenes[camino[x1].x][camino[x1].y].tipo != '@':
                    if self.fantasma == '1':
                        self.mapa_imagenes[camino[x1].x][camino[x1].y].imagen.imagen = imagenes.obtener_imagen_fantasma("blinky", 29, 29)
                    elif self.fantasma == '2':
                        self.mapa_imagenes[camino[x1].x][camino[x1].y].imagen.imagen = imagenes.obtener_imagen_fantasma("pinky", 29, 29)
                    elif self.fantasma == '3':
                        self.mapa_imagenes[camino[x1].x][camino[x1].y].imagen.imagen = imagenes.obtener_imagen_fantasma("inky", 29, 29)
                    elif self.fantasma == '4':
                        self.mapa_imagenes[camino[x1].x][camino[x1].y].imagen.imagen = imagenes.obtener_imagen_fantasma("clyde", 29, 29)
                    id = self.mapa_imagenes[camino[x1].x][camino[x1].y].id
                    #print(self.mapa_imagenes[camino[x1].x][camino[x1].y].imagen.i,self.mapa_imagenes[camino[x1].x][camino[x1].y].imagen.j,id)
                    #print(self.nodos[id].imagen.i,self.nodos[id].imagen.j,self.nodos[id].id)
                    self.mapa_imagenes[camino[x1].x][camino[x1].y].imagen.i = self.nodos[id].imagen.i-4
                    self.mapa_imagenes[camino[x1].x][camino[x1].y].imagen.j = self.nodos[id].imagen.j-4
                    #self.mapa_imagenes[camino[x1].x][camino[x1].y].imagen.i -= 4
                    #self.mapa_imagenes[camino[x1].x][camino[x1].y].imagen.j -= 4
                    self.mapa_imagenes[camino[x1].x][camino[x1].y].tipo = self.fantasma
                    posicion_x_fantasma = camino[x1].x
                    posicion_y_fantasma = camino[x1].y

                    
                    if x1 > 0:
                        #self.mapaJ[camino[x1-1].x][camino[x1-1].y] = '_'
                        if self.respaldo[camino[x1-1].x][camino[x1-1].y] == '_':
                            self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].imagen.imagen = imagenes.obtener_imagen("bola", 21, 21)
                            self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].tipo = '_'
                        
                        #elif self.respaldo[camino[x1-1].x][camino[x1-1].y] == '-':
                        #    self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].imagen.imagen = imagenes.obtener_imagen("nada", 21, 21)
                        #    self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].tipo = '-'
                        #elif self.respaldo[camino[x1-1].x][camino[x1-1].y] == '1':
                        #    self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].imagen.imagen = imagenes.obtener_imagen_fantasma("blinky", 29, 29)
                        #    self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].tipo = '1'
                        #elif self.respaldo[camino[x1-1].x][camino[x1-1].y] == '2':
                        #    self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].imagen.imagen = imagenes.obtener_imagen_fantasma("pinky", 29, 29)
                        #    self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].tipo = '2'
                        #elif self.respaldo[camino[x1-1].x][camino[x1-1].y] == '3':
                        #    self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].imagen.imagen = imagenes.obtener_imagen_fantasma("inky", 29, 29)
                        #    self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].tipo = '3'
                        #elif self.respaldo[camino[x1-1].x][camino[x1-1].y] == '4':
                        #    self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].imagen.imagen = imagenes.obtener_imagen_fantasma("clyde", 29, 29)
                        #    self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].tipo = '4'
                        else:
                            self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].imagen.imagen = imagenes.obtener_imagen("nada", 21, 21)
                            self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].tipo = '-'
                        #if self.mapa_imagenes[camino[x1].x][camino[x1].y].tipo != '@':
                        id = self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].id
                        self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].imagen.i = self.nodos[id].imagen.i+4
                        self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].imagen.j = self.nodos[id].imagen.j+4
                        #self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].imagen.i += 4
                        #self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].imagen.j += 4
                else:
                    print("Comio")
                    
            
            #print("hola")

        

            TOTAL = TOTAL + 1

            MY_LOCK.release()

        


