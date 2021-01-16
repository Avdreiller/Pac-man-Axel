import pygame
class Imagen(object):
    """description of class"""
    def __init__ (self):
        self.x = None
        self.y = None
        self.ancho = None
        self.alto = None
        self.imagen = None
    
    def __init__ (self, imagen, x, y, ancho, alto):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.imagen = imagen

    def comparar_cord(self, x1, y1):
        if x1 >= self.x and y1 >= self.y and x1 <= (self.x + self.ancho) and y1 <= (self.y + self.alto):
            return True
    def setImagen(self, nombre):
        self.imagen = pygame.image.load("recursos/"+nombre+".png").convert_alpha()
        self.imagen = pygame.transform.scale(self.imagen,(self.ancho,self.alto))



