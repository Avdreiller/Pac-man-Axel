import pygame
class Imagenes(object):
    """description of class"""
    def __init__ (self):
        self.pacMan = None
        self.bola = None
        self.nada = None
        self.clyde = None

        self.interseccion = None
        self.interseccion = None
        self.muroSolo = None
        self.muroSolo = None
        self.finalIzquierdo = None
        self.finalIzquierdo = None
        self.finalDerecho = None
        self.finalDerecho = None
        self.finalSuperior = None
        self.finalSuperior = None
        self.finalInferior = None
        self.finalInferior = None
        self.muroIntermedioHorizontal = None
        self.muroIntermedioHorizontal = None
        self.muroIntermedioVertical = None
        self.muroIntermedioVertical = None
        self.esquinaSuperiorIzquierda = None
        self.esquinaSuperiorIzquierda = None
        self.esquinaInferiorDerecha = None
        self.esquinaInferiorDerecha = None
        self.esquinaInferiorIzquierda = None
        self.esquinaInferiorIzquierda = None
        self.esquinaSuperiorDerecha = None
        self.esquinaSuperiorDerecha = None
        self.interseccionSuperior = None
        self.interseccionSuperior = None
        self.interseccionDerecha = None
        self.interseccionDerecha = None
        self.interseccionIzquierda = None
        self.interseccionIzquierda = None
        self.interseccionInferior = None
        self.interseccionInferior = None

        self.nuevaPartida = None
        self.nuevaPartida = None
        self.cargarPartida = None
        self.cargarPartida = None
    
    def __init__ (self):
        self.pacMan = pygame.image.load("recursos/otros/PacMan.png").convert_alpha()
        #self.pacMan = pygame.transform.scale(self.pacMan,(ancho,alto))
        self.bola = pygame.image.load("recursos/otros/bolas.png").convert_alpha()
        #self.bola = pygame.transform.scale(self.bola,(ancho,alto))
        self.nada = pygame.image.load("recursos/otros/Nada.png").convert_alpha()
        self.powerPellets = pygame.image.load("recursos/otros/PowerPellets.png").convert_alpha()
        #self.nada = pygame.transform.scale(self.nada,(ancho,alto))
        self.blinky = pygame.image.load("recursos/otros/FantasmaR.png").convert_alpha()
        self.pinky = pygame.image.load("recursos/otros/FantasmaRs.png").convert_alpha()
        self.inky = pygame.image.load("recursos/otros/FantasmaC.png").convert_alpha()
        self.clyde = pygame.image.load("recursos/otros/FantasmaAn.png").convert_alpha()
        self.sad = pygame.image.load("recursos/otros/FantasmaSad.png").convert_alpha()
        self.sadGris = pygame.image.load("recursos/otros/FantasmaSadGris.png").convert_alpha()
        self.ojosD = pygame.image.load("recursos/otros/ojosDerecha.png").convert_alpha()
        #self.clyde = pygame.transform.scale(self.clyde,(ancho,alto))

        self.interseccion = pygame.image.load("recursos/muros/Intersección.png").convert_alpha()
        #self.interseccion = pygame.transform.scale(self.interseccion,(ancho,alto))
        self.muroSolo = pygame.image.load("recursos/muros/MuroSolo.png").convert_alpha()
        #self.muroSolo = pygame.transform.scale(self.muroSolo,(ancho,alto))
        self.finalIzquierdo = pygame.image.load("recursos/muros/FinalIzquierdo.png").convert_alpha()
        #self.finalIzquierdo = pygame.transform.scale(self.finalIzquierdo,(ancho,alto))
        self.finalDerecho = pygame.image.load("recursos/muros/FinalDerecho.png").convert_alpha()
        #self.finalDerecho = pygame.transform.scale(self.finalDerecho,(ancho,alto))
        self.finalSuperior = pygame.image.load("recursos/muros/FinalSuperior.png").convert_alpha()
        #self.finalSuperior = pygame.transform.scale(self.finalSuperior,(ancho,alto))
        self.finalInferior = pygame.image.load("recursos/muros/FinalInferior.png").convert_alpha()
        #self.finalInferior = pygame.transform.scale(self.finalInferior,(ancho,alto))
        self.muroIntermedioHorizontal = pygame.image.load("recursos/muros/MuroIntermedioHorizontal.png").convert_alpha()
        #self.muroIntermedioHorizontal = pygame.transform.scale(self.muroIntermedioHorizontal,(ancho,alto))
        self.muroIntermedioVertical = pygame.image.load("recursos/muros/MuroIntermedioVertical.png").convert_alpha()
        #self.muroIntermedioVertical = pygame.transform.scale(self.muroIntermedioVertical,(ancho,alto))
        self.esquinaSuperiorIzquierda = pygame.image.load("recursos/muros/EsquinaSuperiorIzquierda.png").convert_alpha()
        #self.esquinaSuperiorIzquierda = pygame.transform.scale(self.esquinaSuperiorIzquierda,(ancho,alto))
        self.esquinaInferiorDerecha = pygame.image.load("recursos/muros/EsquinaInferiorDerecha.png").convert_alpha()
        #self.esquinaInferiorDerecha = pygame.transform.scale(self.esquinaInferiorDerecha,(ancho,alto))
        self.esquinaInferiorIzquierda = pygame.image.load("recursos/muros/EsquinaInferiorIzquierda.png").convert_alpha()
        #self.esquinaInferiorIzquierda = pygame.transform.scale(self.esquinaInferiorIzquierda,(ancho,alto))
        self.esquinaSuperiorDerecha = pygame.image.load("recursos/muros/EsquinaSuperiorDerecha.png").convert_alpha()
        #self.esquinaSuperiorDerecha = pygame.transform.scale(self.esquinaSuperiorDerecha,(ancho,alto))
        self.interseccionSuperior = pygame.image.load("recursos/muros/IntersecciónSuperior.png").convert_alpha()
        #self.interseccionSuperior = pygame.transform.scale(self.interseccionSuperior,(ancho,alto))
        self.interseccionDerecha = pygame.image.load("recursos/muros/IntersecciónDerecha.png").convert_alpha()
        #self.interseccionDerecha = pygame.transform.scale(self.interseccionDerecha,(ancho,alto))
        self.interseccionIzquierda = pygame.image.load("recursos/muros/IntersecciónIzquierda.png").convert_alpha()
        #self.interseccionIzquierda = pygame.transform.scale(self.interseccionIzquierda,(ancho,alto))
        self.interseccionInferior = pygame.image.load("recursos/muros/IntersecciónInferior.png").convert_alpha()
        #self.interseccionInferior = pygame.transform.scale(self.interseccionInferior,(ancho,alto))

        self.nuevaPartida = pygame.image.load("recursos/botones/NuevaPartida.png").convert_alpha()
        #self.nuevaPartida = pygame.transform.scale(self.nuevaPartida,(ancho,alto))
        self.cargarPartida = pygame.image.load("recursos/botones/CargarPartida.png").convert_alpha()
        #self.cargarPartida = pygame.transform.scale(self.cargarPartida,(ancho,alto))


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
        return None