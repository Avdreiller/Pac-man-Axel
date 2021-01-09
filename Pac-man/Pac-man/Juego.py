import pygame
class Juego(object):

    pygame.init()

    AZUL = (0, 0, 255)
    BLACK = (0, 0, 0)
    tamCuadro = 21
 

    size = (820, 720)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Grid on PYGAME")
    clock = pygame.time.Clock()
    gameOver = False
    logo = pygame.image.load("recursos/muros/MuroSolo.png")
    logo = pygame.transform.scale(logo, (tamCuadro,tamCuadro))
    while not gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
        screen.fill(BLACK)
        for i in range(1, 500, tamCuadro + 1):
            for j in range(1, 500, tamCuadro + 1):
                #pygame.draw.rect(screen, AZUL, [i, j, tamCuadro, tamCuadro], 0)
                screen.blit(logo, (i+160, j+110))
        pygame.display.flip()
        clock.tick(1)
    pygame.quit()

