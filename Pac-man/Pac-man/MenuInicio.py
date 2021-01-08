import pygame

class MenuInicio(object):
    """description of class"""

pygame.init()

size = width, height = 820, 720
white = 255, 255, 255

screen = pygame.display.set_mode(size)

fondo = pygame.image.load("recursos/fondos/fondo.jpg")
pygame.display.set_caption("Juego BALL")

fondo = pygame.transform.scale(fondo,(820,720))
logoRect = fondo.get_rect()

pacmanicono = pygame.image.load("recursos/fondos/pacmanCarga.png").convert_alpha()

pacmanicono = pygame.transform.scale(pacmanicono,(300,300))

pacmanicono_pos_x = 260
pacmanicono_pos_y = 450


    

run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            #sys.exit()
            run = False
    
    screen.fill(white)
    screen.blit(fondo, logoRect)
    screen.blit(pacmanicono, (pacmanicono_pos_x, pacmanicono_pos_y))
    pygame.display.flip()

pygame.quit()

