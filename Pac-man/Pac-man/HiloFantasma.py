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
        imagenes = Imagenes.Imagenes(21,21)
        global TOTAL
        x1 = 1
        while True:
            time.sleep(self.delay)
            MY_LOCK.acquire()
            idJ = 0
            idF = 0
            for i in range(len(self.mapa_imagenes)):
                for j in range(len(self.mapa_imagenes)):
                    if self.mapa_imagenes[i][j].tipo == '@':
                        idJ = self.mapa_imagenes[i][j].id
                    if self.mapa_imagenes[i][j].tipo == '4':
                        idF = self.mapa_imagenes[i][j].id
            camino = self.algoritmo.getCamino(self.algoritmo, self.nodos[idJ], self.nodos[idF], self.ruta, self.nodos)
            if x1 < len(camino):
                self.mapa_imagenes[camino[x1].x][camino[x1].y].imagen.imagen = imagenes.obtener_imagen("clyde", 29, 29)
                
                if self.mapa_imagenes[camino[x1].x][camino[x1].y].tipo != '@':
                    id = self.mapa_imagenes[camino[x1].x][camino[x1].y].id
                    self.mapa_imagenes[camino[x1].x][camino[x1].y].imagen.i -= 4
                    self.mapa_imagenes[camino[x1].x][camino[x1].y].imagen.j -= 4
                
                
                if x1 > 0:
                    #self.mapaJ[camino[x1-1].x][camino[x1-1].y] = '_'
                    if self.respaldo[camino[x1-1].x][camino[x1-1].y] == '_':
                        self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].imagen.imagen = imagenes.obtener_imagen("bola", 21, 21)
                        self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].tipo = '_'
                        
                    else:
                        self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].imagen.imagen = imagenes.obtener_imagen("nada", 21, 21)
                        self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].tipo = '-'
                    #if self.mapa_imagenes[camino[x1].x][camino[x1].y].tipo != '@':
                    self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].imagen.i += 4
                    self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].imagen.j += 4
                self.mapa_imagenes[camino[x1].x][camino[x1].y].tipo = '4'
            
            #print("hola")

        

            TOTAL = TOTAL + 1

            MY_LOCK.release()

        


