import pygame, sys
import Juego
import HiloCarga
class PantallaCarga(object):
    def pantalla(self,accion, nivel):    
        
        pygame.init()

        size = width, height = 820, 720
        black = 0, 0, 0

        screen = pygame.display.set_mode(size)

        pygame.display.set_caption("juego ball")

        
        validacion = []
        ruta = [[[]]]
        peso = [[[]]]
        lista_mapas = []
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
        run=True 
        while run:
            var = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    run = False
            if accion == 'J':
                if validacion[0] == True:
                    j = Juego.Juego()
                    j.pantalla_juego(ruta,peso,nivel)
                    var = False
                    run = False
            elif accion == 'C':
                cont = 0
                for x in range(10):
                    if validacion[x] == True:
                        cont+=1
                if cont == 10:
                    self.pantalla(self,'J',nivel)
                    var = False
                    run = False
            if var:
                screen.fill(black)
                pygame.display.flip()
        pygame.quit()
    def hilo(self,lista_mapas,validacion,n, accion, ruta, peso):
        a = HiloCarga.HiloCarga(lista_mapas,validacion,n, accion, ruta, peso)
        a.start()

