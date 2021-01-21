from random import randrange
import threading
import time
import Imagenes

TOTAL = 0

MY_LOCK = threading.Lock()
class HiloFantasma(threading.Thread):
    def __init__(self, delay, mapa_imagenes, algoritmo, nodos, ruta, fantasma, jugador, respaldo,fantasmas, validaciones):
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
        self.validaciones = validaciones

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
            idF3 = 0
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
                    if self.fantasmas[k][x]=='3'and k==2:
                        idF3 = x
                    if self.fantasmas[k][x]=='4'and k==3:
                        idF4 = x
            for i in range(len(self.mapa_imagenes)):
                for j in range(len(self.mapa_imagenes)):
                    if self.mapa_imagenes[i][j].tipo == '@':
                        idJ = self.mapa_imagenes[i][j].id

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
                        seg_jugador = True
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
                seg_jugador = True
            if seg_jugador == True:
                camino = self.algoritmo.getCamino(self.algoritmo, self.nodos[idJ], self.nodos[idF], self.ruta, self.nodos)
                fin = True
                seg_jugador = False
                x1 = 1
            if x1 < len(camino):
                
                
                    
                if self.validaciones[0][0]==True or self.validaciones[0][1]==True or self.validaciones[0][2]==True or self.validaciones[0][3]==True :
                   
                    if self.fantasma=='1':
                        self.fantasmas[fant][idF] = self.nodos[idF1].tipo
                        self.fantasmas[fant][self.mapa_imagenes[10][11].id] = self.fantasma
                    if self.fantasma=='2':
                        self.fantasmas[fant][idF] = self.nodos[idF2].tipo
                        self.fantasmas[fant][self.mapa_imagenes[11][12].id] = self.fantasma
                    if self.fantasma=='3':
                        self.fantasmas[fant][idF] = self.nodos[idF3].tipo
                        self.fantasmas[fant][self.mapa_imagenes[11][10].id] = self.fantasma
                    if self.fantasma=='4':
                        self.fantasmas[fant][idF] = self.nodos[idF4].tipo
                        self.fantasmas[fant][self.mapa_imagenes[11][11].id] = self.fantasma
                    self.validaciones[0][fant]=False
                    fin = True
                else:
                    if self.validaciones[1][0]==True:
                        if self.fantasma=='1':
                            self.fantasmas[fant][idF] = self.nodos[idF1].tipo
                            self.fantasmas[fant][self.mapa_imagenes[10][11].id] = self.fantasma
                            self.validaciones[1][fant]=False
                        fin = True
                    elif self.validaciones[1][1]==True:
                        if self.fantasma=='2':
                            self.fantasmas[fant][idF] = self.nodos[idF2].tipo
                            self.fantasmas[fant][self.mapa_imagenes[11][12].id] = self.fantasma
                            self.validaciones[1][fant]=False
                        fin = True
                    elif self.validaciones[1][2]==True:
                        if self.fantasma=='3':
                            self.fantasmas[fant][idF] = self.nodos[idF3].tipo
                            self.fantasmas[fant][self.mapa_imagenes[11][10].id] = self.fantasma
                            self.validaciones[1][fant]=False
                        fin = True
                    elif self.validaciones[1][3]==True:
                        if self.fantasma=='4':
                            self.fantasmas[fant][idF] = self.nodos[idF4].tipo
                            self.fantasmas[fant][self.mapa_imagenes[11][11].id] = self.fantasma
                            self.validaciones[1][fant]=False
                        fin = True
                    else:
                        if self.mapa_imagenes[camino[x1].x][camino[x1].y].tipo != '@':
                            id = self.mapa_imagenes[camino[x1].x][camino[x1].y].id
                    
                            if self.fantasmas[fant][id] != self.fantasma:
                                self.fantasmas[fant][id] = self.fantasma
                                if x1 > 0:
                                    id2 = self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].id
                                    if self.respaldo[camino[x1-1].x][camino[x1-1].y] == '_':
                                        self.fantasmas[fant][id2] = '_'
                                    else:
                                        self.fantasmas[fant][id2] = '-'
                        
                if fin == False:
                    x1 += 1
            else:
                fin = True
        
            
            TOTAL = TOTAL + 1
            MY_LOCK.release()
            
        


