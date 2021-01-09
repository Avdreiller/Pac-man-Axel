import pygame

class MenuInicio(object):
    """description of class"""

    pygame.init()

    size = width, height = 820, 720
    white = 255, 255, 255

    screen = pygame.display.set_mode(size)

    fondo = pygame.image.load("recursos/fondos/fondo.jpg")
    pygame.display.set_caption("juego ball")

    fondo = pygame.transform.scale(fondo,(820,720))
    logorect = fondo.get_rect()

    pacmanicono = pygame.image.load("recursos/fondos/pacmancarga.png").convert_alpha()

    pacmanicono = pygame.transform.scale(pacmanicono,(300,199))
    pacmanicono_pos_x = 260
    pacmanicono_pos_y = 450


    

    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.quit: 
                sys.exit()
                run = false
    
        screen.fill(white)
        screen.blit(fondo, logorect)
        screen.blit(pacmanicono, (pacmanicono_pos_x, pacmanicono_pos_y))
        pygame.display.flip()

    pygame.quit()


