import pygame, sys
import Juego
class Jugador(object):
    def pantalla(self):    
        j = Juego.Juego
        pygame.init()

        size = width, height = 820, 720
        black = 0, 0, 0

        screen = pygame.display.set_mode(size)

        fondo = pygame.image.load("recursos/fondos/fondo.jpg")
        pygame.display.set_caption("Pac Man")

        fondo = pygame.transform.scale(fondo,(820,720))

       
        cur_Mouse = []
        run=True

        bandera = False
       
        
        while run:
            var = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    run = False
            cont = 0
            if cont == 10:
                j.pantalla_juego(j)
                var = False
                run = False
            if var:
                screen.fill(black)
                pygame.display.flip()
        pygame.quit()


