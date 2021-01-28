import pygame, sys
import Juego
from pygame.locals import *
import HiloCarga
import Imagen
import Imagenes
class PantallaCarga(object):
    def update(self, window,image,current_frame,frame_width,frame_height,frames,posx,posy):
        if current_frame >= frames - 1:
            current_frame = 0
        else:
            current_frame += 1
        new_area = pygame.Rect((current_frame * frame_width, 0, frame_width, frame_height))
        window.blit(image.subsurface(new_area), (posx, posy))
        return current_frame
    def pantalla(self,accion, nivel, puntos):    
        
        pygame.init()

        size = width, height = 820, 720
        black = 0, 0, 0

        screen = pygame.display.set_mode(size)

        pygame.display.set_caption("Pac Man")
        clock = pygame.time.Clock()
        imagenes = Imagenes.Imagenes()
        #fondo = Imagen.Imagen(imagenes.obtener_imagen_boton("NuevaPartida",200,50), 320, 200, 200, 50)
        #fondo = pygame.image.load("C:/Users/Andres/Desktop/dementores.jpg").convert()
        tux_pos_x = 0
        tux_pos_y = 500
        pacmanC= Imagen.Imagen(imagenes.obtener_imagen_carga("pacmanC",420,70), tux_pos_x, tux_pos_y, 420, 70)
        blinky = Imagen.Imagen(imagenes.obtener_imagen_carga("blinkyC",70,70), tux_pos_x, tux_pos_y, 70, 70)
        pinky = Imagen.Imagen(imagenes.obtener_imagen_carga("pinkyC",70,70), tux_pos_x, tux_pos_y, 70, 70)
        inky = Imagen.Imagen(imagenes.obtener_imagen_carga("inkyC",70,70), tux_pos_x, tux_pos_y, 70, 70)
        clyde = Imagen.Imagen(imagenes.obtener_imagen_carga("clydeC",70,70), tux_pos_x, tux_pos_y, 70, 70)
        #fondo = pygame.transform.scale(fondo,(1080,720))
        validacion = []
        ruta = [[]]
        peso = [[]]
        lista_mapas = []

        current_frame = 0
        frames = 6
        frame_width = 70
        frame_height = 70

        #for x in range(10):
        if accion == 'J':
            validacion = [False]
            self.hilo(self,lista_mapas,validacion,nivel,accion, ruta, peso)
        elif accion == 'C':
            for x in range(10):
                validacion.append(False)
            self.hilo(self,lista_mapas,validacion,0,'C', ruta, peso)
            self.hilo(self,lista_mapas,validacion,1,'C', ruta, peso)
            self.hilo(self,lista_mapas,validacion,2,'C', ruta, peso)
            self.hilo(self,lista_mapas,validacion,3,'C', ruta, peso)
            self.hilo(self,lista_mapas,validacion,4,'C', ruta, peso)
            self.hilo(self,lista_mapas,validacion,5,'C', ruta, peso)
            self.hilo(self,lista_mapas,validacion,6,'C', ruta, peso)
            self.hilo(self,lista_mapas,validacion,7,'C', ruta, peso)
            self.hilo(self,lista_mapas,validacion,8,'C', ruta, peso)
            self.hilo(self,lista_mapas,validacion,9,'C', ruta, peso)
        screen.blit(pacmanC.imagen, (tux_pos_x, tux_pos_y))
        screen.blit(blinky.imagen, (tux_pos_x+80, tux_pos_y))
        screen.blit(pinky.imagen, (tux_pos_x+160, tux_pos_y))
        screen.blit(inky.imagen, (tux_pos_x+240, tux_pos_y))
        screen.blit(clyde.imagen, (tux_pos_x+320, tux_pos_y))
        pygame.display.flip()
        run=True 
        while run:
            var = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    run = False
            if accion == 'J':
                if validacion[0] == True:
                    j = Juego.Juego(puntos)
                    j.pantalla_juego(ruta,peso,nivel)
                    var = False
                    run = False
            elif accion == 'C':
                cont = 0
                for x in range(10):
                    if validacion[x] == True:
                        cont+=1
                if cont == 10:
                    self.pantalla(self,'J',nivel,puntos)
                    var = False
                    run = False
            if var:
                screen.fill(black)
                tux_pos_x = tux_pos_x + 7
                if tux_pos_x > 820+320:
                    tux_pos_x = 0
                screen.blit(clyde.imagen, (tux_pos_x, tux_pos_y))
                screen.blit(inky.imagen, (tux_pos_x-80, tux_pos_y))
                screen.blit(pinky.imagen, (tux_pos_x-160, tux_pos_y))
                screen.blit(blinky.imagen, (tux_pos_x-240, tux_pos_y))
                current_frame = self.update(self,screen,pacmanC.imagen,current_frame,frame_width,frame_height,frames,tux_pos_x-320,tux_pos_y)
                #screen.blit(pacmanC1.imagen, (tux_pos_x-320, tux_pos_y))
                #screen.blit(image, (100, 25))
                pygame.display.flip()
                clock.tick(20)

        pygame.quit()
    def hilo(self,lista_mapas,validacion,n, accion, ruta, peso):
        a = HiloCarga.HiloCarga(lista_mapas,validacion,n, accion, ruta, peso)
        a.start()

