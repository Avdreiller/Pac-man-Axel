from random import randrange
import threading
import time
import Imagenes
import pygame

TOTAL = 0

MY_LOCK = threading.Lock()
class HiloFantasma(threading.Thread):
    def __init__(self, delay, mapa_imagenes, dijkstra, floyd, nodos, ruta, fantasma, jugador, respaldo,fantasmas, validaciones,validacion_Fin):
        threading.Thread.__init__(self)
        self.delay = delay
        self.mapa_imagenes = mapa_imagenes
        self.dijkstra = dijkstra
        self.floyd = floyd
        self.nodos = nodos
        self.ruta = ruta
        self.fantasma = fantasma
        self.jugador = jugador
        self.respaldo = respaldo
        self.fantasmas = fantasmas
        self.validaciones = validaciones
        self.validacion_Fin = validacion_Fin

    def run(self):
        clock = pygame.time.Clock()
        imagenes = Imagenes.Imagenes()
        global TOTAL
        x1 = 1
        posicion_x_fantasma = -1
        posicion_y_fantasma = -1
        conta = 0
        fin = True
        seg_jugador = False
        seg_General = False
        id_Centro = self.mapa_imagenes[11][11].id
        fant = 0
        if self.fantasma == '2':
            fant = 1
            #time.sleep(0.5)
        elif self.fantasma == '3':
            fant = 2
            #time.sleep(1)
        elif self.fantasma == '1':
            fant = 0
        elif self.fantasma == '4':
            fant = 3
        camino = []
        while self.validacion_Fin[0] == True:
            if self.validaciones[2] == True:
                if self.validaciones[1][fant]!=True:
                    time.sleep(0.3)
                else:
                    time.sleep(0.01)
            if self.validaciones[1][fant]!=True:
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
            #if idJ != idF and (self.fantasma == '1' or self.fantasma == '2'):

            cam = camino
            camino, fin, x1, seg_jugador, seg_General = self.obtener_Ruta(fin, x1, seg_jugador, seg_General, idF,idF1,idF2,idF4, idJ, id_Centro, fant, cam)
            if camino != None:
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
                    #else:
                    #    if self.validaciones[1][0]==True:
                    #        if self.fantasma=='1':
                    #            self.fantasmas[fant][idF] = self.nodos[idF1].tipo
                    #            self.fantasmas[fant][self.mapa_imagenes[10][11].id] = self.fantasma
                    #            self.validaciones[1][fant]=False
                    #        fin = True
                    #    elif self.validaciones[1][1]==True:
                    #        if self.fantasma=='2':
                    #            self.fantasmas[fant][idF] = self.nodos[idF2].tipo
                    #            self.fantasmas[fant][self.mapa_imagenes[11][12].id] = self.fantasma
                    #            self.validaciones[1][fant]=False
                    #        fin = True
                    #    elif self.validaciones[1][2]==True:
                    #        if self.fantasma=='3':
                    #            self.fantasmas[fant][idF] = self.nodos[idF3].tipo
                    #            self.fantasmas[fant][self.mapa_imagenes[11][10].id] = self.fantasma
                    #            self.validaciones[1][fant]=False
                    #        fin = True
                    #    elif self.validaciones[1][3]==True:
                    #        if self.fantasma=='4':
                    #            self.fantasmas[fant][idF] = self.nodos[idF4].tipo
                    #            self.fantasmas[fant][self.mapa_imagenes[11][11].id] = self.fantasma
                    #            self.validaciones[1][fant]=False
                    #        fin = True
                    else:
                        
                        id = self.mapa_imagenes[camino[x1].x][camino[x1].y].id
                    
                        if self.fantasmas[fant][id] != self.fantasma:
                            self.fantasmas[fant][id] = self.fantasma
                            if x1 > 0:
                                id2 = self.mapa_imagenes[camino[x1-1].x][camino[x1-1].y].id
                                if self.respaldo[camino[x1-1].x][camino[x1-1].y] == '_':
                                    self.fantasmas[fant][id2] = '_'
                                else:
                                    self.fantasmas[fant][id2] = '-'
                    #if seg_General == True:
                        #x1 += 1
                        #if x1 >=1:
                        #    x1 = 1
                    

                    if fin == False:
                        x1 += 1
                else:
                
                    fin = True
                if idF == id_Centro and self.validaciones[1][fant] == True:
                    self.validaciones[1][fant]=False
                    fin = True
            
                TOTAL = TOTAL + 1
            
            MY_LOCK.release()
            
            
    def obtener_Ruta(self, fin, x1, seg_jugador, seg_General, idF,idF1,idF2,idF4, idJ, id_Centro, fant, camino):
        if self.validaciones[1][fant]==True:        
            camino = self.dijkstra.getCamino(self.dijkstra, self.nodos[id_Centro], self.nodos[idF], self.ruta, self.nodos)
            fin = True
            seg_jugador = False
            x1 = 1
            seg_General = True
        elif self.validaciones[2] == True:
            if fin == True:
                vall1 = True
                while vall1 == True:
                    vall = True
                    while vall == True:
                        ran = randrange(len(self.nodos))
                        if ran != idJ and ran != idF:
                            vall = False
                    camino1 = self.floyd.getCamino(self.nodos[ran], self.nodos[idJ], self.ruta, self.nodos)
                    camino2 = self.floyd.getCamino(self.nodos[idF], self.nodos[idJ], self.ruta, self.nodos)
                    if len(camino1)> 5:
                        vall2 = True
                        for x in range(len(camino1)):
                            if x != 0:
                                if self.mapa_imagenes[camino1[x].x][camino1[x].y].id == idJ:
                                    vall2 = False
                        if vall2 == True:
                            #if len(camino2)<len(camino1):
                            vall1 = False
                camino = self.floyd.getCamino(self.nodos[ran], self.nodos[idF], self.ruta, self.nodos)
                fin = False
                #seg_General = True
                x1 = 1
        else:
            if self.fantasma == '4':
                if fin == True:
                    vall1 = True
                    while vall1 == True:
                        vall = True
                        while vall == True:
                            ran = randrange(len(self.nodos))
                            if ran != idF:
                                vall = False
                        
                        camino = self.floyd.getCamino(self.nodos[ran], self.nodos[idF], self.ruta, self.nodos)
                        if len(camino)> 5:
                            vall1 = False
                    fin = False
                    #seg_General = True
                    x1 = 1
            elif self.fantasma == '3':
                if fin == True:
                    ran = randrange(100)
                
                    
                    if ran < 45:
                        seg_jugador = True
                    elif ran >= 45 and ran <=55:
                        if fin == True:
                            vall = True
                            while vall == True:
                                ran = randrange(len(self.nodos))
                                if ran != idF:
                                    vall = False
                            #ran = randrange(len(self.nodos))
                            camino = self.dijkstra.getCamino(self.dijkstra, self.nodos[ran], self.nodos[idF], self.ruta, self.nodos)
                            fin = False
                            x1 = 1
                            #seg_General = True
                    elif ran > 55:
                        ran1 = randrange(3)
                        if ran1 == 0:
                            camino = self.dijkstra.getCamino(self.dijkstra, self.nodos[idF1], self.nodos[idF], self.ruta, self.nodos)
                        elif ran1 == 1:
                            camino = self.dijkstra.getCamino(self.dijkstra, self.nodos[idF2], self.nodos[idF], self.ruta, self.nodos)
                        elif ran1 == 2:
                            camino = self.dijkstra.getCamino(self.dijkstra, self.nodos[idF4], self.nodos[idF], self.ruta, self.nodos)
                        else:
                            print("No Entro al segundo rando")
                        seg_General = True
                        fin = True
                        x1 = 1
                    else:
                        print("No Entro al primer rando")


            else:
                seg_jugador = True
            if seg_jugador == True:
                camino = self.dijkstra.getCamino(self.dijkstra, self.nodos[idJ], self.nodos[idF], self.ruta, self.nodos)
                fin = True
                seg_jugador = False
                x1 = 1
                seg_General = True

        return camino, fin, x1, seg_jugador, seg_General
