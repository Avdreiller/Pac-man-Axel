import threading
import time

TOTAL = 0

MY_LOCK = threading.Lock()
class HiloFantasma(threading.Thread):
    delay = 0
    mapa_imagenes = None
    d = None
    nodos = None
    ruta = None

    def run(self):

        global TOTAL
        x1 = 0
        while True:
            time.sleep(self.delay)

            MY_LOCK.acquire()
            
            camino = self.d.getCamino(self.d, self.nodos[100], self.nodos[0], self.ruta, self.nodos)
            if x1 < len(camino):
                self.mapa_imagenes[camino[x1].x][camino[x1].y].imagen.setImagen("otros/FantasmaA")
                self.mapa_imagenes[camino[x1].x][camino[x1].y].tipo = ''
                if x1-1 > 0:
                    #self.mapaJ[camino[x1-1].x][camino[x1-1].y] = '_'
                    if self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].tipo == '_':
                        self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].imagen.setImagen("otros/bolas")
                        self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].tipo = '_'
                    else:
                        self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].imagen.setImagen("otros/Nada")
                        self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].tipo = '-'
            x1 += 1
            if x1 > len(camino):
                x1 = 0
            #print("hola")

        

            TOTAL = TOTAL + 1

            MY_LOCK.release()

        


