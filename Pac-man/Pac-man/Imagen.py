import pygame
class Imagen(object):
    """description of class"""
    def __init__ (self):
        self.x = None
        self.y = None
        self.ancho = None
        self.alto = None
        self.nombre = None
        self.imagen = None
    
    def __init__ (self, nombre, x, y, ancho, alto):
        nombre = nombre
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.imagen = pygame.image.load("recursos/"+nombre+".png").convert_alpha()
        self.imagen = pygame.transform.scale(self.imagen,(ancho,alto))

    def comparar_cord(self, x1, y1):
        if x1 >= self.x and y1 >= self.y and x1 <= (self.x + self.ancho) and y1 <= (self.y + self.alto):
            return True


