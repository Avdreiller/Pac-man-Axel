import pygame
class Imagenes(object):
    """description of class"""
  
    
    def __init__ (self):
        self.pacMan = pygame.image.load("recursos/otros/PacMan.png").convert_alpha()
        self.bola = pygame.image.load("recursos/otros/bolas.png").convert_alpha()
        self.nada = pygame.image.load("recursos/otros/Nada.png").convert_alpha()
        self.powerPellets = pygame.image.load("recursos/otros/PowerPellets.png").convert_alpha()
        self.tres = pygame.image.load("recursos/otros/tres.png").convert_alpha()
        self.blinky = pygame.image.load("recursos/otros/FantasmaR.png").convert_alpha()
        self.pinky = pygame.image.load("recursos/otros/FantasmaRs.png").convert_alpha()
        self.inky = pygame.image.load("recursos/otros/FantasmaC.png").convert_alpha()
        self.clyde = pygame.image.load("recursos/otros/FantasmaAn.png").convert_alpha()

        self.blinkyC = pygame.image.load("recursos/pantallaCarga/Blinky.png").convert_alpha()
        self.pinkyC = pygame.image.load("recursos/pantallaCarga/Pinky.png").convert_alpha()
        self.inkyC = pygame.image.load("recursos/pantallaCarga/Inky.png").convert_alpha()
        self.clydeC = pygame.image.load("recursos/pantallaCarga/Clyde.png").convert_alpha()
        self.pacManC = pygame.image.load("recursos/pantallaCarga/Pacman.png").convert_alpha()
        self.pacManC1 = pygame.image.load("recursos/pantallaCarga/PacMan1.png").convert_alpha()
        self.pacManC2 = pygame.image.load("recursos/pantallaCarga/PacMan2.png").convert_alpha()
        self.pacManC3 = pygame.image.load("recursos/pantallaCarga/PacMan3.png").convert_alpha()
        self.pacManC4 = pygame.image.load("recursos/pantallaCarga/PacMan4.png").convert_alpha()

        self.sad = pygame.image.load("recursos/otros/FantasmaSad.png").convert_alpha()
        self.sadGris = pygame.image.load("recursos/otros/FantasmaSadGris.png").convert_alpha()
        self.ojosD = pygame.image.load("recursos/otros/ojosDerecha.png").convert_alpha()

        self.interseccion = pygame.image.load("recursos/muros/Intersección.png").convert_alpha()
        self.muroSolo = pygame.image.load("recursos/muros/MuroSolo.png").convert_alpha()
        self.rayo = pygame.image.load("recursos/muros/Rayo.png").convert_alpha()
        self.finalIzquierdo = pygame.image.load("recursos/muros/FinalIzquierdo.png").convert_alpha()
        self.finalDerecho = pygame.image.load("recursos/muros/FinalDerecho.png").convert_alpha()
        self.finalSuperior = pygame.image.load("recursos/muros/FinalSuperior.png").convert_alpha()
        self.finalInferior = pygame.image.load("recursos/muros/FinalInferior.png").convert_alpha()
        self.muroIntermedioHorizontal = pygame.image.load("recursos/muros/MuroIntermedioHorizontal.png").convert_alpha()
        self.muroIntermedioVertical = pygame.image.load("recursos/muros/MuroIntermedioVertical.png").convert_alpha()
        self.esquinaSuperiorIzquierda = pygame.image.load("recursos/muros/EsquinaSuperiorIzquierda.png").convert_alpha()
        self.esquinaInferiorDerecha = pygame.image.load("recursos/muros/EsquinaInferiorDerecha.png").convert_alpha()
        self.esquinaInferiorIzquierda = pygame.image.load("recursos/muros/EsquinaInferiorIzquierda.png").convert_alpha()
        self.esquinaSuperiorDerecha = pygame.image.load("recursos/muros/EsquinaSuperiorDerecha.png").convert_alpha()
        self.interseccionSuperior = pygame.image.load("recursos/muros/IntersecciónSuperior.png").convert_alpha()
        self.interseccionDerecha = pygame.image.load("recursos/muros/IntersecciónDerecha.png").convert_alpha()
        self.interseccionIzquierda = pygame.image.load("recursos/muros/IntersecciónIzquierda.png").convert_alpha()
        self.interseccionInferior = pygame.image.load("recursos/muros/IntersecciónInferior.png").convert_alpha()

        self.nuevaPartida = pygame.image.load("recursos/botones/NuevaPartida.png").convert_alpha()
        self.cargarPartida = pygame.image.load("recursos/botones/CargarPartida.png").convert_alpha()
        self.speed = pygame.image.load("recursos/botones/Speed.png").convert_alpha()
        self.nspeed = pygame.image.load("recursos/botones/NoSpeed.png").convert_alpha()
        self.speedA = pygame.image.load("recursos/botones/SpeedActivo.png").convert_alpha()
        self.configuracion_juego = pygame.image.load("recursos/botones/Configuracion.png").convert_alpha()
        self.resaltarB = pygame.image.load("recursos/botones/Resaltador.png").convert_alpha()
        self.resaltar2 = pygame.image.load("recursos/botones/Resaltador2.png").convert_alpha()

        self.batman = pygame.image.load("recursos/niveles/batman.jpg").convert_alpha()
        self.deadpool = pygame.image.load("recursos/niveles/deadpool.jpg").convert_alpha()
        self.dragonball  = pygame.image.load("recursos/niveles/dragonball .jpg").convert_alpha()
        self.iroman = pygame.image.load("recursos/niveles/iroman.jpg").convert_alpha()
        self.narutoshippuden = pygame.image.load("recursos/niveles/narutoshippuden.jpg").convert_alpha()
        self.onepiece = pygame.image.load("recursos/niveles/onepiece.jpg").convert_alpha()
        self.simsoms = pygame.image.load("recursos/niveles/simsoms.jpg").convert_alpha()
        self.spirderman = pygame.image.load("recursos/niveles/spirderman.jpg").convert_alpha()
        self.superman = pygame.image.load("recursos/niveles/superman.jpg").convert_alpha()
        self.theJocker = pygame.image.load("recursos/niveles/theJocker.jpg").convert_alpha()

        self.batman_Fondo = pygame.image.load("recursos/fondos/niveles/batman.jpg").convert_alpha()
        self.deadpool_Fondo = pygame.image.load("recursos/fondos/niveles/deadpool.jpg").convert_alpha()
        self.dragonball_Fondo  = pygame.image.load("recursos/fondos/niveles/dragonball .jpg").convert_alpha()
        self.iroman_Fondo = pygame.image.load("recursos/fondos/niveles/iroman.jpg").convert_alpha()
        self.narutoshippuden_Fondo = pygame.image.load("recursos/fondos/niveles/narutoshippuden.jpg").convert_alpha()
        self.simsoms_Fondo = pygame.image.load("recursos/fondos/niveles/simsoms.jpg").convert_alpha()
        self.spirderman_Fondo = pygame.image.load("recursos/fondos/niveles/spirderman.jpg").convert_alpha()
        self.superman_Fondo = pygame.image.load("recursos/fondos/niveles/superman.jpg").convert_alpha()
        self.theJocker_Fondo = pygame.image.load("recursos/fondos/niveles/theJocker.jpg").convert_alpha()
        self.onepiece_Fondo = pygame.image.load("recursos/fondos/niveles/onepiece.jpg").convert_alpha()
        self.panel = pygame.image.load("recursos/otros/Panel.png").convert_alpha()
        self.gameover = pygame.image.load("recursos/fondos/game_over.png").convert_alpha()



    def obtener_imagen_fondo(self, nombre,ancho, alto):
        if nombre == "batmanF":
            self.batman_Fondo = pygame.transform.scale(self.batman_Fondo,(ancho,alto))
            return self.batman_Fondo
        elif nombre == "deadpoolF":
            self.deadpool_Fondo = pygame.transform.scale(self.deadpool_Fondo,(ancho,alto))
            return self.deadpool_Fondo
        elif nombre == "dragonballF":
            self.dragonball_Fondo = pygame.transform.scale(self.dragonball_Fondo,(ancho,alto))
            return self.dragonball_Fondo
        elif nombre == "iromanF":
            self.iroman_Fondo = pygame.transform.scale(self.iroman_Fondo,(ancho,alto))
            return self.iroman_Fondo
        elif nombre == "narutoshippudenF":
            self.narutoshippuden_Fondo = pygame.transform.scale(self.narutoshippuden_Fondo,(ancho,alto))
            return self.narutoshippuden_Fondo
        elif nombre == "onepieceF":
            self.onepiece_Fondo = pygame.transform.scale(self.onepiece_Fondo,(ancho,alto))
            return self.onepiece_Fondo
        elif nombre == "simsomsF":
            self.simsoms_Fondo = pygame.transform.scale(self.simsoms_Fondo,(ancho,alto))
            return self.simsoms_Fondo
        elif nombre == "spirdermanF":
            self.spirderman_Fondo = pygame.transform.scale(self.spirderman_Fondo,(ancho,alto))
            return self.spirderman_Fondo
        elif nombre == "supermanF":
            self.superman_Fondo = pygame.transform.scale(self.superman_Fondo,(ancho,alto))
            return self.superman_Fondo
        elif nombre == "theJockerF":
            self.theJocker_Fondo = pygame.transform.scale(self.theJocker_Fondo,(ancho,alto))
            return self.theJocker_Fondo
        elif nombre == "panel":
            self.panel = pygame.transform.scale(self.panel,(ancho,alto))
            return self.panel
        elif nombre == "gameover":
            self.gameover = pygame.transform.scale(self.gameover,(ancho,alto))
            return self.gameover
        
        
        return None
    def obtener_imagen(self, nombre,ancho, alto):
        if nombre == "pacman":
            self.pacMan = pygame.transform.scale(self.pacMan,(ancho,alto))
            return self.pacMan
        elif nombre == "bola":
            self.bola = pygame.transform.scale(self.bola,(ancho,alto))
            return self.bola
        elif nombre == "nada":
            self.nada = pygame.transform.scale(self.nada,(ancho,alto))
            return self.nada
        elif nombre == "power":
            self.powerPellets = pygame.transform.scale(self.powerPellets,(ancho,alto))
            return self.powerPellets
        elif nombre == "tres":
            self.tres = pygame.transform.scale(self.tres,(ancho,alto))
            return self.tres
        return None
    def obtener_imagen_fantasma(self, nombre,ancho, alto):
        if nombre == "blinky":
            self.blinky = pygame.transform.scale(self.blinky,(ancho,alto))
            return self.blinky
        elif nombre == "pinky":
            self.pinky = pygame.transform.scale(self.pinky,(ancho,alto))
            return self.pinky
        elif nombre == "inky":
            self.inky = pygame.transform.scale(self.inky,(ancho,alto))
            return self.inky
        elif nombre == "clyde":
            self.clyde = pygame.transform.scale(self.clyde,(ancho,alto))
            return self.clyde
        elif nombre == "sad":
            self.sad = pygame.transform.scale(self.sad,(ancho,alto))
            return self.sad
        elif nombre == "sadGris":
            self.sadGris = pygame.transform.scale(self.sadGris,(ancho,alto))
            return self.sadGris
        elif nombre == "ojosD":
            self.ojosD = pygame.transform.scale(self.ojosD,(ancho,alto))
            return self.ojosD
        return None

    def obtener_imagen_muro(self, nombre,ancho, alto):
        if nombre == "Intersección":
            self.interseccion = pygame.transform.scale(self.interseccion,(ancho,alto))
            return self.interseccion
        elif nombre == "MuroSolo":
            self.muroSolo = pygame.transform.scale(self.muroSolo,(ancho,alto))
            return self.muroSolo
        elif nombre == "Rayo":
            self.rayo = pygame.transform.scale(self.rayo,(ancho,alto))
            return self.rayo
        return None

    def obtener_imagen_muro_final(self, nombre, ancho, alto):
        if nombre == "FinalIzquierdo":
            self.finalIzquierdo = pygame.transform.scale(self.finalIzquierdo,(ancho,alto))
            return self.finalIzquierdo
        elif nombre == "FinalDerecho":
            self.finalDerecho = pygame.transform.scale(self.finalDerecho,(ancho,alto))
            return self.finalDerecho
        elif nombre == "FinalSuperior":
            self.finalSuperior = pygame.transform.scale(self.finalSuperior,(ancho,alto))
            return self.finalSuperior
        elif nombre == "FinalInferior":
            self.finalInferior = pygame.transform.scale(self.finalInferior,(ancho,alto))
            return self.finalInferior
        return None

    def obtener_imagen_muro_intermedio(self, nombre, ancho, alto):
        if nombre == "MuroIntermedioHorizontal":
            self.muroIntermedioHorizontal = pygame.transform.scale(self.muroIntermedioHorizontal,(ancho,alto))
            return self.muroIntermedioHorizontal
        elif nombre == "MuroIntermedioVertical":
            self.muroIntermedioVertical = pygame.transform.scale(self.muroIntermedioVertical,(ancho,alto))
            return self.muroIntermedioVertical
        return None

    def obtener_imagen_muro_esquina(self, nombre, ancho, alto):
        if nombre == "EsquinaSuperiorIzquierda":
            self.esquinaSuperiorIzquierda = pygame.transform.scale(self.esquinaSuperiorIzquierda,(ancho,alto))
            return self.esquinaSuperiorIzquierda
        elif nombre == "EsquinaInferiorDerecha":
            self.esquinaInferiorDerecha = pygame.transform.scale(self.esquinaInferiorDerecha,(ancho,alto))
            return self.esquinaInferiorDerecha
        elif nombre == "EsquinaInferiorIzquierda":
            self.esquinaInferiorIzquierda = pygame.transform.scale(self.esquinaInferiorIzquierda,(ancho,alto))
            return self.esquinaInferiorIzquierda
        elif nombre == "EsquinaSuperiorDerecha":
            self.esquinaSuperiorDerecha = pygame.transform.scale(self.esquinaSuperiorDerecha,(ancho,alto))
            return self.esquinaSuperiorDerecha 
        return None

    def obtener_imagen_muro_interseccion(self, nombre, ancho, alto):
        if nombre == "InterseccionSuperior":
            self.interseccionSuperior = pygame.transform.scale(self.interseccionSuperior,(ancho,alto))
            return self.interseccionSuperior
        elif nombre == "InterseccionDerecha":
            self.interseccionDerecha = pygame.transform.scale(self.interseccionDerecha,(ancho,alto))
            return self.interseccionDerecha
        elif nombre == "InterseccionIzquierda":
            self.interseccionIzquierda = pygame.transform.scale(self.interseccionIzquierda,(ancho,alto))
            return self.interseccionIzquierda
        elif nombre == "InterseccionInferior":
            self.interseccionInferior = pygame.transform.scale(self.interseccionInferior,(ancho,alto))
            return self.interseccionInferior 
        return None

    def obtener_imagen_boton(self, nombre, ancho, alto):
        if nombre == "NuevaPartida":
            self.nuevaPartida = pygame.transform.scale(self.nuevaPartida,(ancho,alto))
            return self.nuevaPartida
        elif nombre == "CargarPartida":
            self.cargarPartida = pygame.transform.scale(self.cargarPartida,(ancho,alto))
            return self.cargarPartida
        elif nombre == "speed":
            self.speed = pygame.transform.scale(self.speed,(ancho,alto))
            return self.speed
        elif nombre == "nspeed":
            self.nspeed = pygame.transform.scale(self.nspeed,(ancho,alto))
            return self.nspeed
        elif nombre == "speedA":
            self.speedA = pygame.transform.scale(self.speedA,(ancho,alto))
            return self.speedA
        elif nombre == "configuracionJ":
            self.configuracion_juego = pygame.transform.scale(self.configuracion_juego,(ancho,alto))
            return self.configuracion_juego
        elif nombre == "resaltarB":
            self.resaltarB = pygame.transform.scale(self.resaltarB,(ancho,alto))
            return self.resaltarB
        elif nombre == "resaltar2":
            self.resaltar2 = pygame.transform.scale(self.resaltar2,(ancho,alto))
            return self.resaltar2
        
        return None

    def obtener_imagen_carga(self, nombre, ancho, alto):
        if nombre == "pacmanC":
            self.pacManC = pygame.transform.scale(self.pacManC,(ancho,alto))
            return self.pacManC
        if nombre == "pacmanC1":
            self.pacManC1 = pygame.transform.scale(self.pacManC1,(ancho,alto))
            return self.pacManC1
        elif nombre == "pacmanC2":
            self.pacManC2 = pygame.transform.scale(self.pacManC2,(ancho,alto))
            return self.pacManC2
        elif nombre == "pacmanC3":
            self.pacManC3 = pygame.transform.scale(self.pacManC3,(ancho,alto))
            return self.pacManC3
        elif nombre == "pacmanC4":
            self.pacManC4 = pygame.transform.scale(self.pacManC4,(ancho,alto))
            return self.pacManC4
        elif nombre == "blinkyC":
            self.blinkyC = pygame.transform.scale(self.blinkyC,(ancho,alto))
            return self.blinkyC
        elif nombre == "pinkyC":
            self.pinkyC = pygame.transform.scale(self.pinkyC,(ancho,alto))
            return self.pinkyC
        elif nombre == "inkyC":
            self.inkyC = pygame.transform.scale(self.inkyC,(ancho,alto))
            return self.inkyC
        elif nombre == "clydeC":
            self.clydeC = pygame.transform.scale(self.clydeC,(ancho,alto))
            return self.clydeC

    def obtener_imagen_nivel(self, nombre, ancho, alto):
        if nombre == "batman":
            self.batman = pygame.transform.scale(self.batman,(ancho,alto))
            return self.batman
        elif nombre == "deadpool":
            self.deadpool = pygame.transform.scale(self.deadpool,(ancho,alto))
            return self.deadpool
        elif nombre == "dragonball":
            self.dragonball = pygame.transform.scale(self.dragonball,(ancho,alto))
            return self.dragonball
        elif nombre == "iroman":
            self.iroman = pygame.transform.scale(self.iroman,(ancho,alto))
            return self.iroman
        elif nombre == "narutoshippuden":
            self.narutoshippuden = pygame.transform.scale(self.narutoshippuden,(ancho,alto))
            return self.narutoshippuden
        elif nombre == "onepiece":
            self.onepiece = pygame.transform.scale(self.onepiece,(ancho,alto))
            return self.onepiece
        elif nombre == "simsoms":
            self.simsoms = pygame.transform.scale(self.simsoms,(ancho,alto))
            return self.simsoms
        elif nombre == "spirderman":
            self.spirderman = pygame.transform.scale(self.spirderman,(ancho,alto))
            return self.spirderman
        elif nombre == "superman":
            self.superman = pygame.transform.scale(self.superman,(ancho,alto))
            return self.superman
        elif nombre == "theJocker":
            self.theJocker = pygame.transform.scale(self.theJocker,(ancho,alto))
            return self.theJocker
        return None
