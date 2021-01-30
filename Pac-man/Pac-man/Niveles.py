import pygame, sys
import Imagen
import Imagenes
import Juego
import PantallaCarga
import Nodo
import Jugador
class Niveles(object):
    def Nivel(puntaje):    
        j = Juego.Juego
        
        lista_botones = []
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
        imagenes = Imagenes.Imagenes()

        
        btn_Nueva_Partida = Imagen.Imagen(imagenes.obtener_imagen_boton("NuevaPartida",200,50), 320, 200, 200, 50)
        lista_botones.append(btn_Nueva_Partida)
        btn_Cargar_Partida = Imagen.Imagen(imagenes.obtener_imagen_boton("CargarPartida",200,50), 320, 300, 200, 50)
        lista_botones.append(btn_Cargar_Partida)

        fuente = pygame.font.SysFont("Stencil", 25)
        fuente2 = pygame.font.SysFont("Stencil", 28)

        cur_Mouse = []
        run=True
        lista_niveles = []
        img_nivel_alto = 84
        img_nivel_ancho = 150
        i1 = 1
        n1 = 160
        n2 = 120
        for j in range(1, 300, 120 + 1):
            #j1 = 0
            for i in range(1, 480, 180+1):
                img = None
                if i1 == 1:
                    img = Imagen.Imagen(imagenes.obtener_imagen_nivel("theJocker",img_nivel_ancho,img_nivel_alto), i+n1, j+n2, img_nivel_ancho, img_nivel_alto)
                elif i1 == 2:
                    img = Imagen.Imagen(imagenes.obtener_imagen_nivel("simsoms",img_nivel_ancho,img_nivel_alto), i+n1, j+n2, img_nivel_ancho, img_nivel_alto)
                elif i1 == 3:
                    img = Imagen.Imagen(imagenes.obtener_imagen_nivel("iroman",img_nivel_ancho,img_nivel_alto), i+n1, j+n2, img_nivel_ancho, img_nivel_alto)
                elif i1 == 4:
                    img = Imagen.Imagen(imagenes.obtener_imagen_nivel("spirderman",img_nivel_ancho,img_nivel_alto), i+n1, j+n2, img_nivel_ancho, img_nivel_alto)
                elif i1 == 5:
                    img = Imagen.Imagen(imagenes.obtener_imagen_nivel("batman",img_nivel_ancho,img_nivel_alto), i+n1, j+n2, img_nivel_ancho, img_nivel_alto)
                elif i1 == 6:
                    img = Imagen.Imagen(imagenes.obtener_imagen_nivel("superman",img_nivel_ancho,img_nivel_alto), i+n1, j+n2, img_nivel_ancho, img_nivel_alto)
                elif i1 == 7:
                    img = Imagen.Imagen(imagenes.obtener_imagen_nivel("deadpool",img_nivel_ancho,img_nivel_alto), i+n1, j+n2, img_nivel_ancho, img_nivel_alto)
                elif i1 == 8:
                    img = Imagen.Imagen(imagenes.obtener_imagen_nivel("onepiece",img_nivel_ancho,img_nivel_alto), i+n1, j+n2, img_nivel_ancho, img_nivel_alto)
                elif i1 == 9:
                    img = Imagen.Imagen(imagenes.obtener_imagen_nivel("narutoshippuden",img_nivel_ancho,img_nivel_alto), i+n1, j+n2, img_nivel_ancho, img_nivel_alto)
                if img != None:
                    #screen.blit(img.imagen, (img.i, img.j))
                    lista_niveles.append(img)
                i1+=1
        img = Imagen.Imagen(imagenes.obtener_imagen_nivel("dragonball",img_nivel_ancho,img_nivel_alto), 342, 485, img_nivel_ancho, img_nivel_alto)
        lista_niveles.append(img)
        while run:
            var = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    run = False
                if pygame.mouse.get_pressed(3)==(1,0,0):
                    x1, y1 = event.pos
                    if(btn_Nueva_Partida.comparar_cord(x1,y1)):
                        #j.pantalla_juego(j)
                        p = PantallaCarga.PantallaCarga
                        p.pantalla(p,'J',0,0)
                        var = False
                        run = False
                    if(btn_Cargar_Partida.comparar_cord(x1,y1)):
                        #j.pantalla_juego(j)
                        #pj = Jugador.Jugador
                        #pj.pantalla(pj)
                        p = PantallaCarga.PantallaCarga
                        p.pantalla(p,'C',0,0)
                        var = False
                        run = False
                    if(lista_niveles[0].comparar_cord(x1,y1)):
                        #j.pantalla_juego(j)
                        #pj = Jugador.Jugador
                        #pj.pantalla(pj)
                        p = PantallaCarga.PantallaCarga
                        p.pantalla(p,'J',0,puntaje)
                        var = False
                        run = False
                    if(lista_niveles[1].comparar_cord(x1,y1)):
                        p = PantallaCarga.PantallaCarga
                        p.pantalla(p,'J',1,puntaje)
                        var = False
                        run = False
                    if(lista_niveles[2].comparar_cord(x1,y1)):
                        p = PantallaCarga.PantallaCarga
                        p.pantalla(p,'J',2,puntaje)
                        var = False
                        run = False
                    if(lista_niveles[3].comparar_cord(x1,y1)):
                        p = PantallaCarga.PantallaCarga
                        p.pantalla(p,'J',3,puntaje)
                        var = False
                        run = False
                    if(lista_niveles[4].comparar_cord(x1,y1)):
                        p = PantallaCarga.PantallaCarga
                        p.pantalla(p,'J',4,puntaje)
                        var = False
                        run = False
                    if(lista_niveles[5].comparar_cord(x1,y1)):
                        p = PantallaCarga.PantallaCarga
                        p.pantalla(p,'J',5,puntaje)
                        var = False
                        run = False
                    if(lista_niveles[6].comparar_cord(x1,y1)):
                        p = PantallaCarga.PantallaCarga
                        p.pantalla(p,'J',6,puntaje)
                        var = False
                        run = False
                    if(lista_niveles[7].comparar_cord(x1,y1)):
                        p = PantallaCarga.PantallaCarga
                        p.pantalla(p,'J',7,puntaje)
                        var = False
                        run = False
                    if(lista_niveles[8].comparar_cord(x1,y1)):
                        p = PantallaCarga.PantallaCarga
                        p.pantalla(p,'J',8,puntaje)
                        var = False
                        run = False
                    if(lista_niveles[9].comparar_cord(x1,y1)):
                        p = PantallaCarga.PantallaCarga
                        p.pantalla(p,'J',9,puntaje)
                        var = False
                        run = False
            if var:
                screen.fill(white)
                screen.blit(fondo, logorect)
                for x in lista_niveles:
                    screen.blit(x.imagen, (x.i, x.j))
                i1 = 1
                for j in range(1, 300, 120 + 1):
                    for i in range(1, 480, 180+1):
                        
                        mensaje = fuente2.render(str(i1), 1, (0, 0, 0))
                        screen.blit(mensaje, (i+n1, j+n2))    
                        mensaje = fuente.render(str(i1), 1, (0, 255, 0))
                        screen.blit(mensaje, (i+n1+2, j+n2+2))
                        
                        i1 += 1
                nivel = "10"
                mensaje = fuente2.render(nivel, 1, (0, 0, 0))
                screen.blit(mensaje, (342, 485))
                mensaje = fuente.render(nivel, 1, (0, 255, 0))
                screen.blit(mensaje, (344, 487))
                pygame.display.flip()
        pygame.quit()


